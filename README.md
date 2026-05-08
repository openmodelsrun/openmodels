# OpenModels Registry

This repository contains the OpenModels registry - a collection of YAML files defining LLM models, inference providers, and their mappings.

## Structure

```
openmodels/
├── models/           # Canonical model definitions
├── providers/        # Inference provider definitions
├── mappings/         # Provider-model mappings with pricing
├── schemas/          # JSON Schema definitions
└── validate_registry.py  # Validation script
```

## Validation

All registry submissions are automatically validated on pull requests using the `validate_registry.py` script.

### Running Validation Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the validation script:
   ```bash
   python validate_registry.py
   ```

### What Gets Validated

The validation script checks:

- **YAML Syntax**: All YAML files must be parseable
- **Schema Validation**: Files must conform to their respective JSON schemas
- **Duplicate IDs**: Model and provider IDs must be unique
- **Referential Integrity**: Mappings must reference existing models and providers

### Validation Output

The script outputs a detailed report showing:
- Total files validated
- Schema validation errors with field paths
- Duplicate ID errors
- Referential integrity errors

Example output:
```
✅ **Validation Passed**

Validated 10 files successfully.
```

Or on failure:
```
❌ **Validation Failed**

**Summary:** 2 of 10 files failed validation.

### Schema Validation Errors

**models/invalid-model.yaml**
- **context_window**: -1000 is less than the minimum of 1
  - Expected: minimum: 1
  - Actual: -1000
```

## Contributing

See the [contribution guide](../docs/contributing/) for instructions on adding models, providers, and mappings to the registry.

## Schemas

JSON Schema definitions are located in the `schemas/` directory:

- `model.schema.json` - Model definition schema
- `provider.schema.json` - Provider definition schema
- `mapping.schema.json` - Mapping definition schema

### Extensible Pricing Model

The pricing structure in mappings is designed to be extensible to support future pricing dimensions:

**Required fields:**
- `input_per_million` - Price per 1M input tokens
- `output_per_million` - Price per 1M output tokens
- `currency` - ISO 4217 currency code (e.g., "USD")

**Optional extensible fields:**
- `cache_write_per_million` - Price per 1M tokens written to cache (prompt caching)
- `cache_read_per_million` - Price per 1M tokens read from cache
- `image_per_unit` - Price per image unit (for vision models)
- `audio_per_second` - Price per second of audio (for audio models)
- `reasoning_tokens_per_million` - Price per 1M reasoning tokens (for reasoning models)
- `search_grounding_per_query` - Price per search grounding query

**Example:**
```yaml
pricing:
  input_per_million: 15.0
  output_per_million: 75.0
  currency: USD
  cache_write_per_million: 3.75
  cache_read_per_million: 1.50
  image_per_unit: 0.048
```

See `mappings/.example-extended-pricing.yaml` for a complete example.

## GitHub Actions

The validation workflow runs automatically on pull requests that modify:
- `models/**`
- `providers/**`
- `mappings/**`
- `schemas/**`
- `validate_registry.py`
- `requirements.txt`

The workflow will:
1. Install Python dependencies
2. Run the validation script
3. Post validation results as a PR comment
4. Block the PR if validation fails
