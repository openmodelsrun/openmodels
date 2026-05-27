#!/usr/bin/env python3
"""
Registry Validation Script

Usage:
    python validate_registry.py
"""

import sys
import json
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from jsonschema import validate, ValidationError as JsonSchemaValidationError, Draft7Validator


@dataclass
class ValidationError:
    """Represents a validation error for a specific field"""
    field: str
    message: str
    expected: str
    actual: str


@dataclass
class ValidationResult:
    """Result of validating a single file"""
    valid: bool
    errors: List[ValidationError] = field(default_factory=list)


@dataclass
class ValidationReport:
    """Complete validation report for the registry"""
    success: bool
    total_files: int = 0
    valid_files: int = 0
    invalid_files: int = 0
    errors: Dict[str, List[ValidationError]] = field(default_factory=dict)
    duplicate_ids: List[str] = field(default_factory=list)
    referential_errors: List[str] = field(default_factory=list)


class RegistryValidator:
    """Validates YAML files in the OpenModels registry"""
    
    def __init__(self, registry_path: Optional[Path] = None):
        """
        Initialize the validator
        
        Args:
            registry_path: Path to the registry root (defaults to current directory)
        """
        self.registry_path = registry_path or Path.cwd()
        self.schemas_path = self.registry_path / 'schemas'
        
        # Load JSON schemas
        self.model_schema = self._load_schema('model.schema.json')
        self.provider_schema = self._load_schema('provider.schema.json')
        self.mapping_schema = self._load_schema('mapping.schema.json')
        
        # Create validators
        self.model_validator = Draft7Validator(self.model_schema)
        self.provider_validator = Draft7Validator(self.provider_schema)
        self.mapping_validator = Draft7Validator(self.mapping_schema)
    
    def _load_schema(self, schema_filename: str) -> Dict[str, Any]:
        """Load a JSON schema from file"""
        schema_path = self.schemas_path / schema_filename
        if not schema_path.exists():
            raise FileNotFoundError(f"Schema not found: {schema_path}")
        
        with open(schema_path, 'r') as f:
            return json.load(f)
    
    def check_yaml_syntax(self, file_path: Path) -> bool:
        """
        Check if a YAML file has valid syntax
        
        Args:
            file_path: Path to the YAML file
            
        Returns:
            True if YAML is parseable, False otherwise
        """
        try:
            with open(file_path, 'r') as f:
                yaml.safe_load(f)
            return True
        except yaml.YAMLError as e:
            print(f"YAML syntax error in {file_path}: {e}")
            return False
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return False
    
    def check_schema(self, file_path: Path, schema_type: str) -> ValidationResult:
        """
        Validate a YAML file against its JSON schema
        
        Args:
            file_path: Path to the YAML file
            schema_type: Type of schema ('model', 'provider', or 'mapping')
            
        Returns:
            ValidationResult with validation status and errors
        """
        # First check YAML syntax
        if not self.check_yaml_syntax(file_path):
            return ValidationResult(
                valid=False,
                errors=[ValidationError(
                    field='root',
                    message='Invalid YAML syntax',
                    expected='valid YAML',
                    actual='parse error'
                )]
            )
        
        # Load YAML content
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            return ValidationResult(
                valid=False,
                errors=[ValidationError(
                    field='root',
                    message=str(e),
                    expected='valid YAML',
                    actual='parse error'
                )]
            )
        
        # Select appropriate validator
        if schema_type == 'model':
            validator = self.model_validator
        elif schema_type == 'provider':
            validator = self.provider_validator
        elif schema_type == 'mapping':
            validator = self.mapping_validator
        else:
            raise ValueError(f"Unknown schema type: {schema_type}")
        
        # Validate against schema
        errors = []
        for error in validator.iter_errors(data):
            # Convert jsonschema error to our ValidationError format
            field = '.'.join(str(p) for p in error.path) if error.path else 'root'
            
            # Build human-readable message
            message = error.message
            
            # Determine expected value
            expected = 'valid value'
            if error.validator == 'type':
                expected = f"type: {error.validator_value}"
            elif error.validator == 'enum':
                expected = f"one of: {', '.join(error.validator_value)}"
            elif error.validator == 'required':
                missing_prop = error.message.split("'")[1] if "'" in error.message else 'unknown'
                expected = f"required field: {missing_prop}"
                field = missing_prop
            elif error.validator == 'pattern':
                expected = f"pattern: {error.validator_value}"
            elif error.validator in ('minimum', 'maximum', 'minLength', 'maxLength', 'minItems', 'maxItems'):
                expected = f"{error.validator}: {error.validator_value}"
            elif error.validator == 'format':
                expected = f"format: {error.validator_value}"
            
            # Determine actual value
            actual = 'invalid value'
            if error.instance is not None:
                if isinstance(error.instance, (dict, list)):
                    actual = f"type: {'array' if isinstance(error.instance, list) else 'object'}"
                else:
                    actual = str(error.instance)
            
            errors.append(ValidationError(
                field=field,
                message=message,
                expected=expected,
                actual=actual
            ))
        
        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors
        )
    
    def check_duplicate_ids(self) -> List[str]:
        """
        Find duplicate model or provider IDs across all files
        
        Returns:
            List of duplicate IDs found
        """
        duplicates = []
        
        # Check model IDs
        model_ids = {}
        models_dir = self.registry_path / 'models'
        if models_dir.exists():
            for yaml_file in models_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'id' in data:
                            model_id = data['id']
                            if model_id in model_ids:
                                if model_id not in duplicates:
                                    duplicates.append(f"Duplicate model ID: {model_id} (found in {model_ids[model_id]} and {yaml_file})")
                            else:
                                model_ids[model_id] = yaml_file
                except Exception as e:
                    print(f"Error reading {yaml_file}: {e}")
        
        # Check provider IDs
        provider_ids = {}
        providers_dir = self.registry_path / 'providers'
        if providers_dir.exists():
            for yaml_file in providers_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'id' in data:
                            provider_id = data['id']
                            if provider_id in provider_ids:
                                if provider_id not in duplicates:
                                    duplicates.append(f"Duplicate provider ID: {provider_id} (found in {provider_ids[provider_id]} and {yaml_file})")
                            else:
                                provider_ids[provider_id] = yaml_file
                except Exception as e:
                    print(f"Error reading {yaml_file}: {e}")
        
        return duplicates
    
    def check_referential_integrity(self) -> List[str]:
        """
        Verify that mappings reference existing model_id and provider_id values
        
        Returns:
            List of referential integrity errors
        """
        errors = []
        
        # Collect all valid model IDs
        model_ids = set()
        models_dir = self.registry_path / 'models'
        if models_dir.exists():
            for yaml_file in models_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'id' in data:
                            model_ids.add(data['id'])
                except Exception as e:
                    print(f"Error reading {yaml_file}: {e}")
        
        # Collect all valid provider IDs and their declared regions
        provider_ids = set()
        provider_regions = {}
        providers_dir = self.registry_path / 'providers'
        if providers_dir.exists():
            for yaml_file in providers_dir.glob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data and 'id' in data:
                            provider_id = data['id']
                            provider_ids.add(provider_id)
                            provider_regions[provider_id] = set(data.get('regions', []))
                except Exception as e:
                    print(f"Error reading {yaml_file}: {e}")
        
        # Check all mappings
        mappings_dir = self.registry_path / 'mappings'
        if mappings_dir.exists():
            for yaml_file in mappings_dir.rglob('*.yaml'):
                try:
                    with open(yaml_file, 'r') as f:
                        data = yaml.safe_load(f)
                        if data:
                            # Check model_id reference
                            if 'model_id' in data:
                                model_id = data['model_id']
                                if model_id not in model_ids:
                                    errors.append(f"Mapping {yaml_file} references non-existent model_id: {model_id}")
                            
                            # Check provider_id reference
                            if 'provider_id' in data:
                                provider_id = data['provider_id']
                                if provider_id not in provider_ids:
                                    errors.append(f"Mapping {yaml_file} references non-existent provider_id: {provider_id}")
                                elif 'available_regions' in data:
                                    available_regions = set(data['available_regions'])
                                    invalid_regions = available_regions - provider_regions[provider_id]
                                    if invalid_regions and 'global' not in provider_regions[provider_id]:
                                        errors.append(
                                            f"Mapping {yaml_file} has available_regions not declared by provider "
                                            f"{provider_id}: {', '.join(sorted(invalid_regions))}"
                                        )
                except Exception as e:
                    print(f"Error reading {yaml_file}: {e}")
        
        return errors
    
    def validate_all(self) -> ValidationReport:
        """
        Validate all YAML files in the registry
        
        Returns:
            ValidationReport with complete validation results
        """
        report = ValidationReport(success=True)
        
        # Validate models
        models_dir = self.registry_path / 'models'
        if models_dir.exists():
            for yaml_file in models_dir.glob('*.yaml'):
                report.total_files += 1
                result = self.check_schema(yaml_file, 'model')
                if result.valid:
                    report.valid_files += 1
                else:
                    report.invalid_files += 1
                    report.success = False
                    report.errors[str(yaml_file)] = result.errors
        
        # Validate providers
        providers_dir = self.registry_path / 'providers'
        if providers_dir.exists():
            for yaml_file in providers_dir.glob('*.yaml'):
                report.total_files += 1
                result = self.check_schema(yaml_file, 'provider')
                if result.valid:
                    report.valid_files += 1
                else:
                    report.invalid_files += 1
                    report.success = False
                    report.errors[str(yaml_file)] = result.errors
        
        # Validate mappings
        mappings_dir = self.registry_path / 'mappings'
        if mappings_dir.exists():
            for yaml_file in mappings_dir.rglob('*.yaml'):
                report.total_files += 1
                result = self.check_schema(yaml_file, 'mapping')
                if result.valid:
                    report.valid_files += 1
                else:
                    report.invalid_files += 1
                    report.success = False
                    report.errors[str(yaml_file)] = result.errors
        
        # Check for duplicate IDs
        report.duplicate_ids = self.check_duplicate_ids()
        if report.duplicate_ids:
            report.success = False
        
        # Check referential integrity
        report.referential_errors = self.check_referential_integrity()
        if report.referential_errors:
            report.success = False
        
        return report


def format_report_for_github(report: ValidationReport) -> str:
    """
    Format validation report for GitHub PR comment
    
    Args:
        report: ValidationReport to format
        
    Returns:
        Formatted markdown string
    """
    lines = []
    
    if report.success:
        lines.append("✅ **Validation Passed**")
        lines.append(f"\nValidated {report.total_files} files successfully.")
    else:
        lines.append("❌ **Validation Failed**")
        lines.append(f"\n**Summary:** {report.invalid_files} of {report.total_files} files failed validation.")
        
        # Schema validation errors
        if report.errors:
            lines.append("\n### Schema Validation Errors\n")
            for file_path, errors in report.errors.items():
                lines.append(f"**{file_path}**")
                for error in errors:
                    lines.append(f"- **{error.field}**: {error.message}")
                    lines.append(f"  - Expected: {error.expected}")
                    lines.append(f"  - Actual: {error.actual}")
                lines.append("")
        
        # Duplicate ID errors
        if report.duplicate_ids:
            lines.append("### Duplicate ID Errors\n")
            for duplicate in report.duplicate_ids:
                lines.append(f"- {duplicate}")
            lines.append("")
        
        # Referential integrity errors
        if report.referential_errors:
            lines.append("### Referential Integrity Errors\n")
            for error in report.referential_errors:
                lines.append(f"- {error}")
            lines.append("")
    
    return "\n".join(lines)


def main():
    """Main entry point for the validation script"""
    print("OpenModels Registry Validator")
    print("=" * 50)
    
    # Initialize validator
    validator = RegistryValidator()
    
    # Run validation
    print("Validating registry...")
    report = validator.validate_all()
    
    # Print report
    print("\n" + format_report_for_github(report))
    
    # Exit with appropriate code
    sys.exit(0 if report.success else 1)


if __name__ == '__main__':
    main()
