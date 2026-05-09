# Changelog

All notable changes to the OpenModels Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-05-09

### Changed
- Registry schema version bumped to 0.3.0 in sync with platform release

## [0.2.0] - 2026-05-08

### Fixed
- CI workflow now correctly captures validation script exit code (was always 0 due to pipe)

### Added
- Initial registry structure with models, providers, and mappings directories
- JSON Schema definitions for model, provider, and mapping validation
- Python validation script with schema, duplicate ID, and referential integrity checks
- GitHub Actions workflow for automated PR validation with comment reporting
- Extended pricing model support (cache, image, audio, reasoning, search grounding)
- Example mapping file demonstrating extensible pricing dimensions
- VERSION file for tracking registry schema version
- CHANGELOG.md for documenting changes

## [0.1.0] - 2025-01-01

### Added
- Initial project setup
- Base JSON schemas (model.schema.json, provider.schema.json, mapping.schema.json)

[Unreleased]: https://github.com/openmodels/openmodels/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/openmodels/openmodels/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/openmodels/openmodels/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/openmodels/openmodels/releases/tag/v0.1.0
