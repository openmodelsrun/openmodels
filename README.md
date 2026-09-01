# OpenModels Registry

The open-source registry of LLM models, inference providers, and provider-model mappings. Community-maintained, schema-validated, and machine-readable.

**Current stats:** 149 models · 52 providers · 222 mappings

## Overview

OpenModels is a structured, version-controlled registry that serves as the single source of truth for LLM model metadata, inference provider details, and provider-model mappings (including pricing and rate limits). All data is stored as human-readable YAML files and validated against JSON Schemas on every pull request.

## Coverage

| Vendor | Models |
|--------|--------|
| OpenAI | GPT-5.6 Terra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-5.4 Mini, GPT-OSS 120B, GPT-OSS 20B, GPT-5.4, GPT-5.5 Pro, GPT-5, GPT-4 |
| Anthropic | Claude Opus 5, Claude Sonnet 5, Claude Mythos 5, Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 4.6, Claude Opus 4.6, Claude Sonnet 4.5, Claude Haiku 4.5, Claude 3 Opus |
| Google | Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash Cyber, Gemini 3.5 Pro, DiffusionGemma, Gemma 4 12B, Gemini 3 Flash, Gemini 3.5 Flash, Gemini 3.1 Flash-Lite, Gemma 4 (E2B/E4B/26B/31B), Gemini 3.1 Pro, Gemini 2.5 Pro, Gemini 2.5 Flash, Gemma 3 (1B/4B/12B/27B) |
| xAI | Grok 4.6, Grok 4.5, Grok 4.3, Grok 4.20, Grok 4.1 Fast, Grok 4 |
| DeepSeek | DeepSeek V4 Flash Vision Exp, DeepSeek V4 Pro, DeepSeek V4 Flash, DeepSeek V4, DeepSeek R1, DeepSeek V3 |
| Meta | Muse Spark 1.1, Muse Spark, Llama 4 Scout, Llama 4 Maverick, Llama 3.3 70B, Llama 3.2 (3B/11B/90B), Llama 3.1 8B |
| Mistral | Mistral Small 4, Mistral Medium 3.5, Mistral Large 3, Devstral 2, Mistral Small 3.1, Codestral |
| Alibaba | Qwen 3.8 Flash, Qwen3.8-Flash-Next, Qwen 3.8 Max, Qwen 3.8 2.4T-A95B, Qwen 3.8 27B, Qwen Flash Character, Qwen 3.7 Plus, Qwen 3.7 Max, Qwen 3.6 (27B, 35B-A3B, Plus), Qwen 3.6, Qwen3 Coder, Qwen3 235B, Qwen3 32B, QwQ-32B |
| Moonshot | Kimi K3, Kimi K2.7 Code, Kimi K2.6 |
| Cohere | Command A+, Command A, Command R7B |
| Cohere For AI | Tiny Aya, Aya Expanse 32B |
| Zhipu | GLM-5.3-Flash, GLM-5.3, GLM-5.2, GLM-5.1, GLM-4.7 |
| MiniMax | M3, M2.7 |
| Sarvam AI | Sarvam-M, Sarvam-105B, Sarvam-30B, Sarvam-1 |
| Sakana AI | Sakana Fugu Ultra, Sakana Fugu |
| Motif Technologies | Motif 3 Beta |
| Thinking Machines Lab | Inkling |
| OpenBMB | MiniCPM-V 4.6 |
| NVIDIA | Nemotron 3 Ultra, Nemotron 3 Super 120B, Nemotron Nano 9B |
| Microsoft | Phi-4 Mini, Phi-4 |
| Yandex | YandexGPT 5 Lite |
| Sber | GigaChat 3.1 Ultra, GigaChat 3.1 Lightning |
| ISSAI | KazLLM 1.0 70B |
| Astana Hub | AlemLLM |
| IBM | Granite 4.2 30B, Granite 4.2 8B, Granite 4.2 3B, Granite Speech 5.0 TurboCTC, Granite 4.1 30B, Granite 4.1 8B |
| Xiaomi | MiMo-V2.5-Pro |
| MTS AI | Cotype Nano |
| Tencent | Hy4 Preview, Hy3 Preview |
| Poolside | Laguna M.1 |
| AI21 Labs | Jamba Large 1.7 |
| TII | Falcon-H1, Falcon 3 10B |
| 01.AI | Yi-Lightning |
| Writer | Palmyra X5 |
| Databricks | DBRX |
| Snowflake | Arctic |
| Stability AI | StableLM 2 12B |
| Uzbek LLM Lab | Alloma 8B Instruct |
| InclusionAI | Ring-2.6-1T |
| Upstage | Solar Pro 3 |
| LLM360/MBZUAI | K2 Think |
| OpenAI (Audio) | Whisper |
| VNGRS | Kumru 7B |
| Trendyol | Trendyol LLM 8B T1 |
| WiroAI | WiroAI Turkish LLM 9B |

### Providers

01.AI · AI21 Labs · Alibaba Model Studio · Amazon Bedrock · Anthropic · Anyscale · Azure AI · Baseten · Cerebras · Cloudflare Workers AI · Cohere · Deep Infra · DeepSeek · Featherless · Fireworks · Google AI Studio · Google (Vertex AI) · Groq · Hugging Face Inference · Hyperbolic · IBM watsonx.ai · InclusionAI · Inference.net · Lambda · Meta · MiniMax · Mistral · Modal · Moonshot · Nebius · NLP Cloud · Novita · NVIDIA NIM · OpenAI · OpenRouter · Perplexity · Reka AI · Replicate · Sakana AI · SambaNova · Sarvam AI · Sber · Scaleway · SiliconFlow · Snowflake Cortex AI · Tinker · Together AI · Upstage · xAI · Xiaomi MiMo · Yandex Cloud · Zhipu AI

## Structure

```
openmodels/
├── models/               # Canonical model definitions (YAML)
├── providers/            # Inference provider definitions (YAML)
├── mappings/             # Provider-model mappings with pricing (YAML)
│   ├── anthropic/
│   ├── openai/
│   ├── together-ai/
│   └── ...
├── schemas/              # JSON Schema definitions for validation
│   ├── model.schema.json
│   ├── provider.schema.json
│   └── mapping.schema.json
├── validate_registry.py  # Validation script
└── requirements.txt      # Python dependencies
```

## Contributing

We welcome contributions from the community. You can add new models, providers, or mappings by opening a pull request.

### Quick Start

1. Fork this repository
2. Create a new branch for your changes
3. Add or update YAML files (see templates below)
4. Run validation locally to check your changes
5. Open a pull request

### Adding a Model

Create a new file at `models/{model-id}.yaml`:

```yaml
id: my-new-model           # Unique ID (kebab-case, lowercase)
name: My New Model          # Display name
description: A brief description of the model and its capabilities.
capabilities:               # What the model can do
  - chat
  - completion
  - function-calling
  - code-generation
modalities:                 # Input/output modalities
  - text
  - code
context_window: 128000      # Max context window in tokens
licensing: apache-2.0       # License (e.g., proprietary, apache-2.0, mit)
created_at: "2025-01-01T00:00:00.000Z"
updated_at: "2025-01-01T00:00:00.000Z"
```

**Required fields:** id, name, description, capabilities, modalities, context_window, licensing, created_at, updated_at

### Adding a Provider

Create a new file at `providers/{provider-id}.yaml`:

```yaml
id: my-provider             # Unique ID (kebab-case, lowercase)
name: My Provider           # Display name
description: Description of the inference provider.
api_base_url: https://api.myprovider.com/v1
auth_type: api-key          # One of: bearer, api-key, oauth2
regions:                    # Deployment regions
  - us-east-1
  - eu-west-1
compatibility: openai       # API compatibility (openai, anthropic, custom)
created_at: "2025-01-01T00:00:00.000Z"
updated_at: "2025-01-01T00:00:00.000Z"
```

**Required fields:** id, name, description, api_base_url, auth_type, regions, compatibility, created_at, updated_at

### Adding a Mapping

Create a new file at `mappings/{provider-id}/{model-id}.yaml`:

```yaml
model_id: deepseek-v3           # Must reference an existing model
provider_id: together-ai        # Must reference an existing provider
provider_model_name: deepseek-ai/DeepSeek-V3  # Provider's internal model name
pricing:
  input_per_million: 0.90       # Price per 1M input tokens (required)
  output_per_million: 0.90      # Price per 1M output tokens (required)
  currency: USD                 # ISO 4217 currency code (required)
rate_limits:
  requests_per_minute: 600
  tokens_per_minute: 1000000
context_window_override: null   # Override model's default (or null)
available_regions:              # Subset of provider's regions
  - us-east-1
created_at: "2025-01-01T00:00:00.000Z"
updated_at: "2025-01-01T00:00:00.000Z"
```

**Required fields:** model_id, provider_id, provider_model_name, pricing, rate_limits, available_regions, created_at, updated_at

### Extensible Pricing Model

The pricing structure supports optional fields for specialized pricing dimensions:

| Field | Description |
|-------|-------------|
| `input_per_million` | Price per 1M input tokens (required) |
| `output_per_million` | Price per 1M output tokens (required) |
| `currency` | ISO 4217 currency code (required) |
| `cache_write_per_million` | Price per 1M tokens written to cache |
| `cache_read_per_million` | Price per 1M tokens read from cache |
| `image_per_unit` | Price per image unit (vision models) |
| `audio_per_second` | Price per second of audio |
| `reasoning_tokens_per_million` | Price per 1M reasoning tokens |
| `search_grounding_per_query` | Price per search grounding query |

See `mappings/.example-extended-pricing.yaml` for a complete example.

### ID Format Rules

- Use **kebab-case** (lowercase letters, numbers, and hyphens only)
- Must be unique across all files of the same type
- Examples: `deepseek-v3`, `together-ai`, `gpt-5-4-mini`

### Validation

All pull requests are automatically validated by GitHub Actions. The validation checks:

- **YAML Syntax** — All YAML files must be parseable
- **Schema Validation** — Files must conform to their JSON Schema (`schemas/`)
- **Duplicate IDs** — Model and provider IDs must be unique
- **Referential Integrity** — Mappings must reference existing models and providers

### Running Validation Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the validation script
python validate_registry.py
```

Example output on success:
```
✅ Validation Passed
Validated 135 files successfully.
```

Example output on failure:
```
❌ Validation Failed

Summary: 2 of 135 files failed validation.

Schema Validation Errors:
  models/invalid-model.yaml
  - context_window: -1000 is less than the minimum of 1
```

## Schemas

JSON Schema definitions in `schemas/` enforce the structure of all YAML files:

- `model.schema.json` — Model definition schema
- `provider.schema.json` — Provider definition schema
- `mapping.schema.json` — Mapping definition schema

## GitHub Actions

The validation workflow triggers on pull requests that modify:
- `models/**`, `providers/**`, `mappings/**`
- `schemas/**`
- `validate_registry.py`, `requirements.txt`

The workflow will:
1. Install Python dependencies
2. Run the validation script
3. Post validation results as a PR comment
4. Block the PR if validation fails

On merge to `main`, the ingestion workflow automatically loads updated data into the platform database.

## API & Platform

The OpenModels platform provides a REST API and web interface for querying registry data, comparing providers, and viewing telemetry (health, latency, uptime).

- **API Documentation:** Available at `/api/docs` (Swagger UI) and `/api/docs/openapi.json` (OpenAPI spec)
- **Web Interface:** Browse models, compare providers, and view real-time telemetry
- **Registry Repository:** [github.com/openmodelsrun/openmodels](https://github.com/openmodelsrun/openmodels)
- **Documentation Site:** [github.com/openmodelsrun/docs](https://github.com/openmodelsrun/docs)

## License

This registry is open source. See the repository for license details.
