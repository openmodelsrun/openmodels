# Changelog

All notable changes to the OpenModels Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Claude Sonnet 5** (Anthropic, US) — most capable Sonnet-class model with a 1M-token context window, adaptive thinking with selectable reasoning effort, and text/image/file inputs. Introductory pricing $2/$10 per 1M tokens (through 2026-08-31), then $3/$15. Added Anthropic mapping.

## [1.0.0] - 2026-06-24

First stable release of the OpenModels Registry. The schema, file layout, and validation rules are now considered stable.

### Added
- **Sakana Fugu** and **Sakana Fugu Ultra** (Sakana AI, Japan) — first **Japan (jp) representation**. Multi-agent orchestration models delivered as a single OpenAI-compatible API; Fugu is a language model trained to call a pool of specialist LLMs (and recursive instances of itself), handling selection, delegation, verification, and synthesis. Built on Sakana AI's TRINITY and Conductor research. Ultra is the higher-quality tier (reported 93.2 LiveCodeBench, 73.7 SWE-Bench Pro, 82.1 TerminalBench).
- **New provider: Sakana AI** (Japan) — OpenAI-compatible API for the Fugu family (ap-northeast-1, global)
- **2 new mappings** — Sakana Fugu ($2/$12 per 1M tokens) and Sakana Fugu Ultra ($5/$30 per 1M tokens) on Sakana

### Changed
- New country represented: Japan (JP)
- Total coverage: 117 models · 51 providers · 185 mappings

## [0.9.0] - 2026-06-19

### Added
- **GLM-5.2** (Z.ai / formerly Zhipu AI, China) — flagship open-weight coding model with a 1M-token context window. Mixture-of-Experts with 753B total / ~40B active parameters and two cost-balancing reasoning modes. Tops several coding benchmarks at a fraction of the cost of comparable proprietary models. MIT-licensed weights.
- **First India (in) representation** — four models from Sarvam AI:
  - **Sarvam-105B** — sovereign 105B MoE (~9B active) trained on 12T tokens across 22 Indian languages, 128 sparse experts with Multi-head Latent Attention, 128K context, custom low-fertility Indic tokenizer
  - **Sarvam-30B** — 30B MoE reasoning model (2.4B active) trained from scratch, optimized for real-time deployment, 128K context
  - **Sarvam-M** — 24B instruction-tuned derivative of Mistral-Small-3.1-24B, post-trained on English + 11 Indic languages, 131K context
  - **Sarvam-1** — compact 2B model for 10 Indic languages, edge-deployable, Apache 2.0
- **Command A+** (Cohere, US) — enterprise flagship building on Command A with stronger reasoning, agentic tool use, and multilingual performance; 256K context
- **New provider: Sarvam AI** (India) — OpenAI-compatible API for the Sarvam model family, hosted on India-based infrastructure (ap-south-1)
- **8 new mappings:**
  - GLM-5.2 on Zhipu ($0.60/$2.00 per 1M tokens)
  - GLM-5.2 on OpenRouter ($0.60/$2.00 per 1M tokens)
  - Sarvam-M on Sarvam ($0.50/$1.50 per 1M tokens) and OpenRouter ($0.25/$0.75 per 1M tokens)
  - Sarvam-105B, Sarvam-30B, and Sarvam-1 on Sarvam
  - Command A+ on Cohere ($2.50/$10.00 per 1M tokens)

### Changed
- New country represented: India (IN)
- Total coverage: 115 models · 50 providers · 183 mappings

## [0.8.8] - 2026-06-12

### Added
- **Kimi K2.7 Code** (Moonshot AI, China) — open-source, coding-focused model in the Kimi K2 family, built for reliable end-to-end programming over long contexts. 1-trillion-parameter model that cuts reasoning token usage ~30% vs K2.6 while improving coding and agent performance (+21.8% Kimi Code Bench v2, +11.0% Program Bench, +31.5% MLS Bench Lite). Modified MIT License, 1M context window.
- **3 new mappings:**
  - Kimi K2.7 Code on Moonshot ($1.00/$3.00 per 1M tokens)
  - Kimi K2.7 Code on Hugging Face Inference ($0.60/$2.40 per 1M tokens)
  - Kimi K2.7 Code on OpenRouter ($0.60/$2.40 per 1M tokens)

### Changed
- Total coverage: 109 models · 49 providers · 175 mappings

## [0.8.7] - 2026-06-12

### Added
- **Claude Fable 5** (Anthropic, US) — first publicly available Mythos-class model, exceeding any model Anthropic has previously made generally available. State-of-the-art on nearly all tested benchmarks with exceptional software engineering, knowledge work, vision, and scientific research; its lead grows on longer, more complex tasks. Ships with safeguards that route sensitive cybersecurity, biology, chemistry, and distillation queries to Opus 4.8. 300K context window.
- **Claude Mythos 5** (Anthropic, US) — the same underlying model as Fable 5 with safeguards lifted in some areas. Strongest cybersecurity capabilities of any model in the world. Access restricted to trusted cyberdefenders and infrastructure providers via Project Glasswing. 300K context window.
- **DiffusionGemma** (Google, US) — experimental diffusion-based member of the Gemma 4 open family. Denoises a canvas of placeholder tokens to generate up to 256 tokens in parallel rather than autoregressively, delivering ~4x throughput of similarly sized Gemma models on local hardware. MoE with 26B total / 3.8B active parameters, Apache 2.0, 256K context window.
- **3 new mappings:**
  - Claude Fable 5 on Anthropic ($15/$75 per 1M tokens, with cache pricing)
  - DiffusionGemma on Hugging Face Inference ($0.15/$0.15 per 1M tokens)
  - DiffusionGemma on Google AI Studio (free tier)

### Changed
- Total coverage: 108 models · 49 providers · 172 mappings

## [0.8.6] - 2026-06-04

### Added
- **Nemotron 3 Ultra** (NVIDIA, US) — flagship open 550B-parameter MoE model with 55B active parameters. Hybrid Mamba-Transformer architecture with LatentMoE routing, multi-token prediction, and NVFP4 precision. Built for frontier reasoning and orchestration in long-running agentic systems. 5x higher throughput and 30% lower cost-to-task-completion vs comparable open models. 1M+ context window (95% on Ruler@1M). Licensed under OpenMDW-1.1 (Linux Foundation).
- **4 new mappings:**
  - Nemotron 3 Ultra on NVIDIA NIM (free)
  - Nemotron 3 Ultra on DeepInfra ($0.40/$1.60 per 1M tokens)
  - Nemotron 3 Ultra on Together AI ($0.50/$1.50 per 1M tokens)
  - Nemotron 3 Ultra on OpenRouter ($0.40/$1.60 per 1M tokens)

### Changed
- Total coverage: 105 models · 49 providers · 169 mappings

## [0.8.5] - 2026-06-04

### Added
- **Gemma 4 12B** (Google, US) — encoder-free unified multimodal model with 12B parameters. Natively processes text, image, audio, and video without separate encoders. 256K context window, 140+ languages, native function calling. First medium-sized model capable of natively ingesting audio. Optimized for local deployment on 16GB GPUs.
- **3 new mappings:**
  - Gemma 4 12B on Google AI Studio (free tier)
  - Gemma 4 12B on Hugging Face Inference ($0.10/$0.10 per 1M tokens)
  - Gemma 4 12B on NVIDIA NIM (free)

### Changed
- Total coverage: 104 models · 49 providers · 165 mappings

## [0.8.3] - 2026-06-03

### Added
- **MiniMax M3** (MiniMax, China) — frontier open-weight model with 1M-token context window, native multimodality (text, image, video), and strong coding capabilities. Built on MiniMax Sparse Attention (MSA) architecture, achieving 59% on SWE-Bench Pro with 1/20 the cost of the previous generation at 1M tokens. First open-weight model to combine frontier-level coding, ultra-long context, and multimodal input in a single system.
- **3 new mappings:**
  - MiniMax M3 on MiniMax ($0.60/$2.40 per 1M tokens, with cache read pricing)
  - MiniMax M3 on SiliconFlow (same pricing with cache support)
  - MiniMax M3 on OpenRouter ($0.30/$1.20 per 1M tokens — promotional pricing)

## [0.8.2] - 2026-05-30

### Added
- **3 new Turkish models** — first Turkey (TR) representation in the registry:
  - **Kumru 7B** (VNGRS, Turkey) — decoder-only LLM pre-trained from scratch on 500 GB of Turkish corpora (300B tokens), custom Turkish tokenizer, outperforms larger multilingual models on the Cetvel benchmark
  - **Trendyol LLM 8B T1** (Trendyol, Turkey) — fine-tuned from Qwen3-8B on large-scale Turkish e-commerce data, 32K context, chain-of-thought reasoning in Turkish, Apache-2.0
  - **WiroAI Turkish LLM 9B** (WiroAI, Turkey) — fine-tuned from Gemma 2 9B on 500K+ Turkish instructions, adapted to Turkish culture and local context
- **New provider: Featherless** — serverless inference platform hosting 20,000+ open-source HuggingFace models with flat-rate subscription pricing, OpenAI-compatible API, global availability
- **7 new mappings:**
  - Kumru 7B on Hugging Face Inference and Featherless
  - Trendyol LLM 8B T1 on Hugging Face Inference and Featherless
  - WiroAI Turkish LLM 9B on Hugging Face Inference, Featherless, and Azure AI

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

[Unreleased]: https://github.com/openmodels/openmodels/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/openmodels/openmodels/compare/v0.9.0...v1.0.0
[0.9.0]: https://github.com/openmodels/openmodels/compare/v0.8.8...v0.9.0
[0.8.8]: https://github.com/openmodels/openmodels/compare/v0.8.7...v0.8.8
[0.8.6]: https://github.com/openmodels/openmodels/compare/v0.8.5...v0.8.6
[0.8.5]: https://github.com/openmodels/openmodels/compare/v0.8.3...v0.8.5
[0.8.3]: https://github.com/openmodels/openmodels/compare/v0.8.2...v0.8.3
[0.8.2]: https://github.com/openmodels/openmodels/compare/v0.8.1...v0.8.2
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
