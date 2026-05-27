# OpenModels Registry

The open-source registry of LLM models, inference providers, and provider-model mappings. Community-maintained, schema-validated, and machine-readable.

**Current stats:** 98 models · 48 providers · 151 mappings

## Overview

OpenModels is a structured, version-controlled registry that serves as the single source of truth for LLM model metadata, inference provider details, and provider-model mappings (including pricing and rate limits). All data is stored as human-readable YAML files and validated against JSON Schemas on every pull request.

## Coverage

| Vendor | Models |
|--------|--------|
| OpenAI | GPT-4, GPT-5, GPT-5.4, GPT-5.4 Mini, GPT-5.5, GPT-5.5 Pro, GPT-OSS 20B, GPT-OSS 120B |
| Anthropic | Claude 3 Opus, Claude Haiku 4.5, Claude Sonnet 4.5, Claude Sonnet 4.6, Claude Opus 4.6, Claude Opus 4.7 |
| Google | Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash-Lite, Gemma 3 (1B/4B/12B/27B), Gemma 4 (E2B/E4B/26B/31B) |
| xAI | Grok 4, Grok 4.1 Fast, Grok 4.20, Grok 4.3 |
| DeepSeek | DeepSeek V3, DeepSeek R1, DeepSeek V4, DeepSeek V4 Pro, DeepSeek V4 Flash |
| Meta | Llama 3.1 8B, Llama 3.2 (3B/11B/90B), Llama 3.3 70B, Llama 4 Scout, Llama 4 Maverick, Muse Spark |
| Mistral | Mistral Medium 3.5, Mistral Large 3, Mistral Small 3.1, Mistral Small 4, Devstral 2, Codestral |
| Microsoft | Phi-4, Phi-4 Mini |
| Alibaba | Qwen3 32B, Qwen3 235B, Qwen3 Coder, QwQ-32B, Qwen 3.6 (35B-A3B, 27B, Plus), Qwen 3.7 (Max, Plus) |
| NVIDIA | Nemotron 3 Super 120B, Nemotron Nano 9B |
| Moonshot | Kimi K2.6 |
| Cohere | Command A, Command R7B |
| Zhipu | GLM-4.7, GLM-5.1 |
| MiniMax | M2.7 |
| Yandex | YandexGPT 5 Lite |
| Sber | GigaChat 3.1 Ultra, GigaChat 3.1 Lightning |
| ISSAI | KazLLM 1.0 70B |
| Astana Hub | AlemLLM |
| IBM | Granite 4.1 8B, Granite 4.1 30B |
| Xiaomi | MiMo-V2.5-Pro |
| MTS AI | Cotype Nano |
| Tencent | Hy3 Preview |
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

### Providers

01.AI · AI21 Labs · Alibaba Model Studio · Amazon Bedrock · Anthropic · Anyscale · Azure AI · Baseten · Cerebras · Cloudflare Workers AI · Cohere · Deep Infra · DeepSeek · Fireworks · Google AI Studio · Google (Vertex AI) · Groq · Hugging Face Inference · Hyperbolic · IBM watsonx.ai · InclusionAI · Inference.net · Lambda · Meta · MiniMax · Mistral · Modal · Moonshot · Nebius · NLP Cloud · Novita · NVIDIA NIM · OpenAI · OpenRouter · Perplexity · Reka AI · Replicate · SambaNova · Sber · Scaleway · SiliconFlow · Snowflake Cortex AI · Together AI · Upstage · xAI · Xiaomi MiMo · Yandex Cloud · Zhipu AI

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
