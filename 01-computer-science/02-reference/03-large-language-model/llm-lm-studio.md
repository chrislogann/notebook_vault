---
domain: 01-computer-science
class: 02-reference
subject: 03-large-language-model
type: note
status:
  - complete
created: 2026-07-27 17:50:00
updated: 2026-07-27 17:50:00
aliases:
  - LM Studio Client
author: ""
source: Gemma4
tags:
  - large-language-model
  - model-platform
  - local-ai
---

# Lm Studio

## Overview
> LM Studio is a graphical desktop application enabling local execution, management, and REST API serving of quantized open-source LLMs on consumer hardware.

## Core Concepts
- Leverages the GGUF file format to load quantized models efficiently onto local CPU and GPU RAM pools.
- Provides parameter control interfaces for real-time adjustments to temperature, top-p, and context length during testing.
- Hosts a local, OpenAI-compatible HTTP server endpoint to integrate offline LLMs into external applications.

## Connections & References
- [[03-large-language-model]]
- [[quantization]]
- [[model-platform]]
- [[ollama]]