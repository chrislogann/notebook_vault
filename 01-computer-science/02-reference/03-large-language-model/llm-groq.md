---
domain: 01-computer-science
class: 02-reference
subject: 03-large-language-model
type: note
status:
  - complete
created: 2026-07-30 22:02
updated: 2026-07-30 22:02
aliases: []
author:
source: gemma4
tags: []
---

# Groq

## Overview
> Groq is a hardware platform designed to accelerate large language model (LLM) inference by utilizing specialized, highly efficient processors that minimize latency and maximize throughput, often achieving record-setting response times for generative AI tasks.

## Core Concepts
- **LPU Architecture:** The core innovation lies in the Language Processing Unit (LPU), which is optimized specifically for LLM operations like matrix multiplications, leading to exceptional performance over general-purpose GPUs in inference scenarios.
- **High Memory Bandwidth:** Groq systems prioritize extremely high memory bandwidth and efficient data movement, eliminating common bottlenecks found when running large models that require constant reading/writing of weights and activations.
- **Context Streaming:** The platform excels at continuous token streaming, allowing users to receive model output tokens nearly instantly as they are generated, significantly improving the perceived speed and responsiveness of conversational AI applications.

## Connections & References
- [[03-large-language-model]]
- [[accelerated-inference]]
- [[low-latency-systems]]
- [[llm-hardware-architecture]]
