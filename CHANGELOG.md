# Changelog

All notable changes to the OpenModels Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.8.1] - 2026-05-28

### Added
- **Claude Opus 4.8** (Anthropic, US) — Anthropic's latest flagship model building on Opus 4.7 with improvements across coding, agentic skills, reasoning, and knowledge work. Enhanced honesty, better tool use efficiency, and dynamic workflows support. 300K context.
- Mapping: Claude Opus 4.8 on Anthropic ($15/$75 per 1M tokens, with cache pricing)

## [0.8.0] - 2026-05-27

### Added
- 16 new provider-model mappings (total: 151)

### Changed
- `meta/muse-spark` mapping: regions updated from `us-east-1`, `us-west-2` to `global`
- `alibaba-model-studio` provider: added `ap-east-1` (Hong Kong) region

### Improved
- `validate_registry.py`: added referential integrity check — mapping `available_regions` must exist in the provider's declared regions
- `validate_registry.py`: `global` in provider regions acts as wildcard, allowing any region in mappings

## [0.7.9] - 2026-05-25

### Added
- **Ring-2.6-1T** (InclusionAI / Ant Group, China) — trillion-parameter MoE reasoning model with ~63B active params, hybrid linear + MLA attention, 128K context, adaptive reasoning-effort modes, MIT license
- **New provider: InclusionAI** — Ant Group's AI research lab with ZenMux inference platform (OpenAI-compatible API)

### Changed
- Total coverage: 98 models · 48 providers · 135 mappings

## [0.7.8] - 2026-05-25

### Added
- **9 new models:**
  - Jamba Large 1.7 (AI21 Labs, Israel) — hybrid SSM-Transformer MoE, 256K context, enterprise-grade
  - Yi-Lightning (01.AI, China) — MoE architecture, top Chatbot Arena in Chinese/Math/Code
  - Falcon-H1 (TII, UAE) — hybrid Mamba-Transformer, outperforms Llama/Qwen in 30-70B range
  - Falcon 3 10B (TII, UAE) — #1 on HuggingFace leaderboard under 13B params
  - Palmyra X5 (Writer, USA) — 1M context window, adaptive reasoning, enterprise agents
  - DBRX (Databricks, USA) — 132B MoE (36B active), open-source enterprise model
  - Snowflake Arctic (Snowflake, USA) — 480B MoE (17B active), Apache 2.0, SQL/code specialist
  - StableLM 2 12B (Stability AI, UK) — 12.1B decoder, 2T tokens multilingual training
  - Alloma 8B Instruct (Uzbek LLM Lab, Uzbekistan) — first Uzbek-optimized LLM with custom tokenizer
- **5 new providers:**
  - AI21 Labs — Jamba model family with hybrid SSM-Transformer architecture
  - Reka AI — multimodal models (text/image/video/audio) with Flash and Edge variants
  - Lambda — GPU cloud and managed inference API for open-source models
  - Snowflake Cortex AI — Arctic models integrated with Snowflake data platform
  - 01.AI — Yi model family with strong Chinese/multilingual capabilities
- New countries represented: Israel (IL), UAE (AE), Uzbekistan (UZ), UK (GB)

### Changed
- Total coverage: 97 models · 47 providers · 135 mappings

## [0.7.7] - 2026-05-24

### Added
- **Country of origin** field (`country`) added to all 88 models using ISO 3166-1 alpha-2 codes
- Countries represented: US, CN, FR, KR, AE, RU, KZ
- Model schema updated with optional `country` field

### Changed
- Total coverage: 88 models · 42 providers · 135 mappings

## [0.7.6] - 2026-05-23

### Added
- **Solar Pro 3** — Upstage's 102B MoE language model (12B active params) with 128K context. Optimized for Korean with English and Japanese support. Strong reasoning, structured output, and agentic workflows.
- **K2 Think** — LLM360/MBZUAI's 32B open-weights reasoning model (Apache 2.0). Trained with RL and verifiable rewards for math, science, and code. ~2000 tok/s on Cerebras WSE.
- New provider: **Upstage** — Korean AI company with OpenAI-compatible API
- Mappings: Solar Pro 3 on Upstage ($0.15/$0.60 per 1M tokens)
- Mappings: Solar Pro 3 on OpenRouter ($0.15/$0.60 per 1M tokens)
- Mappings: K2 Think on Cerebras ($0.60/$0.60 per 1M tokens)

### Changed
- Total coverage: 88 models · 42 providers · 136 mappings

## [0.7.5] - 2026-05-21

### Added
- **Qwen 3.7 Max** — Alibaba's flagship proprietary model for advanced agentic coding, complex reasoning, and long-horizon task execution. Ranked #13 in Arena AI Text, #7 in Math, #10 in Coding. Supports 1000+ tool integrations and 35-hour sustained autonomous operation.
- **Qwen 3.7 Plus** — Alibaba's multimodal variant optimized for vision understanding. Ranked #5 globally in Arena AI Vision leaderboard.
- Mappings: Qwen 3.7 Max on Alibaba Model Studio ($1.30/$7.80 per 1M tokens)
- Mappings: Qwen 3.7 Plus on Alibaba Model Studio ($0.80/$2.40 per 1M tokens)

### Changed
- Total coverage: 86 models · 41 providers · 133 mappings

## [0.7.4] - 2026-05-19

### Added
- **Gemini 3 Flash** — Google's balanced model combining Gemini 3 Pro reasoning with Flash-line latency and cost efficiency. 1M context, configurable thinking levels, streaming function calling.
- **Gemini 3.1 Flash-Lite** — Google's most cost-efficient model optimized for high-volume, low-latency tasks. 2.5x faster TTFT vs Gemini 2.5 Flash, 1M context, full multimodal support.
- Mappings: Gemini 3 Flash on Google Vertex AI and Google AI Studio ($0.50/$3.00 per 1M tokens)
- Mappings: Gemini 3.1 Flash-Lite on Google Vertex AI and Google AI Studio ($0.25/$1.50 per 1M tokens)

### Changed
- Total coverage: 84 models · 41 providers · 131 mappings

## [0.7.3] - 2026-05-12

### Added
- **MiniCPM-V 4.6** — OpenBMB's ultra-efficient 1B multimodal model (vision + video), edge-deployable, 256K context
- **Aya Expanse 32B** — Cohere For AI's 32B multilingual model, 23 languages, 8K context
- **Tiny Aya** — Cohere For AI's compact 3.35B multilingual model, 70+ languages, edge-optimized

### Changed
- Total coverage: 82 models · 41 providers · 127 mappings

## [0.7.2] - 2026-05-12

### Added
- **Hy3 Preview** — Tencent's 295B MoE / 21B active, fast+slow thinking, 256K context, open-weight
- **Laguna M.1** — Poolside AI's 225B MoE / 23B active, agentic coding flagship, 128K context
- Mappings: Hy3 Preview on SiliconFlow and OpenRouter, Laguna M.1 on OpenRouter

### Changed
- Total coverage: 79 models · 41 providers · 126 mappings

## [0.7.1] - 2026-05-12

### Added
- **4 new models:**
  - MiMo-V2.5-Pro (Xiaomi's 1.02T MoE flagship with 1M context, MIT license)
  - Granite 4.1 8B (IBM's dense 8B model, 131K context, Apache 2.0)
  - Granite 4.1 30B (IBM's dense 30B model, 512K context, Apache 2.0)
  - Cotype Nano (MTS AI's lightweight 1.5B model for Russian/English, Apache 2.0)
- **2 new providers:**
  - Xiaomi MiMo (OpenAI-compatible API for MiMo model family)
  - IBM watsonx.ai (enterprise AI platform with Granite models)
- **5 new mappings:**
  - MiMo-V2.5-Pro on OpenRouter ($1/$3 per 1M tokens)
  - MiMo-V2.5-Pro on Xiaomi direct API
  - Granite 4.1 8B on OpenRouter ($0.05/$0.10 per 1M tokens)
  - Granite 4.1 8B on IBM watsonx
  - Granite 4.1 30B on IBM watsonx
- **Vendor logo mappings** for IBM, Xiaomi MiMo, MTS AI (Cotype), GigaChat, Yandex, ISSAI (KazLLM)
- **Provider logo aliases** for IBM watsonx, NLP Cloud, Xiaomi, Yandex Cloud

### Changed
- Total coverage: 77 models · 41 providers · 123 mappings

## [0.7.0] - 2026-05-11

### Added
- **9 new providers** — Amazon Bedrock, Azure AI, Replicate, Anyscale, SiliconFlow, Hugging Face Inference, Perplexity, Yandex Cloud, Sber
- **11 new models:**
  - GPT-5.5 (OpenAI's most capable model for complex real-world work)
  - Muse Spark (Meta Superintelligence Labs' first model with agentic capabilities)
  - Codestral (Mistral's specialized code generation model)
  - Qwen 3.6 35B-A3B, Qwen 3.6 27B, Qwen 3.6 Plus (Alibaba's latest generation)
  - YandexGPT 5 Lite (Yandex's 8B open-weight model for Russian/English)
  - GigaChat 3.1 Ultra, GigaChat 3.1 Lightning (Sber's MoE models)
  - ISSAI KazLLM 1.0 70B (Kazakh language model from Nazarbayev University)
  - AlemLLM (Kazakhstan's 247B MoE flagship from Astana Hub)
- **27 new mappings** expanding coverage of existing models across new providers (Amazon Bedrock, Azure AI, SiliconFlow, Hugging Face, Replicate, Anyscale, Perplexity, Fireworks, Groq)

### Changed
- Total coverage: 70+ models · 37+ providers · 130+ mappings
- Registry version bumped to 0.7.0

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

[Unreleased]: https://github.com/openmodels/openmodels/compare/v0.8.1...HEAD
[0.8.1]: https://github.com/openmodels/openmodels/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/openmodels/openmodels/compare/v0.7.9...v0.8.0
[0.7.9]: https://github.com/openmodels/openmodels/compare/v0.7.8...v0.7.9
[0.7.8]: https://github.com/openmodels/openmodels/compare/v0.7.7...v0.7.8
[0.7.7]: https://github.com/openmodels/openmodels/compare/v0.7.6...v0.7.7
[0.7.6]: https://github.com/openmodels/openmodels/compare/v0.7.5...v0.7.6
[0.7.5]: https://github.com/openmodels/openmodels/compare/v0.7.4...v0.7.5
[0.7.4]: https://github.com/openmodels/openmodels/compare/v0.7.3...v0.7.4
[0.7.3]: https://github.com/openmodels/openmodels/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/openmodels/openmodels/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/openmodels/openmodels/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/openmodels/openmodels/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/openmodels/openmodels/compare/v0.4.0...v0.6.0
[0.4.0]: https://github.com/openmodels/openmodels/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/openmodels/openmodels/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/openmodels/openmodels/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/openmodels/openmodels/releases/tag/v0.1.0
