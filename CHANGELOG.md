# Changelog

All notable changes to the OpenModels Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.6.0] - 2026-05-11

### Added
- **Registry expanded to 50+ models** — added Llama family (3.1 8B, 3.2 3B/11B/90B, 3.3 70B, 4 Scout, 4 Maverick), Gemma 3 (1B/4B/12B/27B), Gemma 4 (E2B/E4B/26B/31B), Qwen3 (32B, 235B, Coder), QwQ-32B, Mistral Small 3.1, Phi-4, Phi-4 Mini, Whisper (audio modality), GPT-OSS (120B, 20B)
- **Registry expanded to 26+ providers** — added SambaNova, Scaleway, Nebius, Hyperbolic, Fireworks, Baseten, Novita, NLP Cloud, Alibaba Model Studio, Modal, Inference.net with verified API endpoints
- **100+ provider-model mappings** with pricing data for all new providers
- Whisper model definition with audio modality support

### Changed
- Total coverage: 50+ models · 26+ providers · 100+ mappings

## [0.4.0] - 2026-05-09

### Added
- **44 model definitions** covering all major LLM families as of May 2026:
  - OpenAI: GPT-4, GPT-5, GPT-5.4, GPT-5.4 Mini, GPT-5.5, GPT-5.5 Pro, GPT-OSS 20B, GPT-OSS 120B
  - Anthropic: Claude 3 Opus, Claude Haiku 4.5, Claude Sonnet 4.5, Claude Sonnet 4.6, Claude Opus 4.6, Claude Opus 4.7
  - Google: Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 3.1 Pro, Gemma 4 31B
  - xAI: Grok 4, Grok 4.1 Fast, Grok 4.20, Grok 4.3
  - DeepSeek: DeepSeek V3, DeepSeek R1, DeepSeek V4, DeepSeek V4 Pro, DeepSeek V4 Flash
  - Meta: Llama 3.3 70B, Llama 4 Scout, Llama 4 Maverick
  - Mistral: Mistral Medium 3.5, Mistral Large 3, Mistral Small 4, Devstral 2
  - NVIDIA: Nemotron 3 Super 120B, Nemotron Nano 9B
  - Moonshot: Kimi K2.6
  - Cohere: Command A, Command R7B
  - Alibaba: Qwen3 Coder, Qwen 3.6
  - Zhipu: GLM-4.7, GLM-5.1
  - MiniMax: M2.7
- **19 provider definitions** with verified API endpoints and auth types:
  - Anthropic, Cerebras, Cloudflare Workers AI, Cohere, Deep Infra, DeepSeek, Google AI Studio, Google (Vertex AI), Groq, Meta, MiniMax, Mistral, Moonshot, NVIDIA NIM, OpenAI, OpenRouter, Together AI, xAI, Zhipu AI
- **72 provider-model mappings** with pricing sourced from official documentation
- NVIDIA NIM free endpoint mappings for open-weight models
- Deep Infra serverless inference mappings with competitive pricing
- Pricing data verified against official sources (OpenAI, Anthropic, xAI, Mistral, Google, DeepSeek, NVIDIA docs)

### Changed
- Registry schema version bumped to 0.4.0
- Updated GPT-4 and Claude 3 Opus `updated_at` timestamps

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

[Unreleased]: https://github.com/openmodels/openmodels/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/openmodels/openmodels/compare/v0.4.0...v0.6.0
[0.4.0]: https://github.com/openmodels/openmodels/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/openmodels/openmodels/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/openmodels/openmodels/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/openmodels/openmodels/releases/tag/v0.1.0
