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
  - Model Compression
  - Precision Reduction
author: ""
source: Gemma4
tags:
  - large-language-model
  - quantization
  - model-compression
---

# Quantization

## Overview
> Quantization is a compression technique mapping high-precision floating-point parameters to lower-bit representations to reduce VRAM requirements and accelerate inference.

## Core Concepts
- Post-Training Quantization (PTQ) converts trained weights directly, while Quantization-Aware Training (QAT) simulates bit reduction during training passes.
- Drastically lowers memory bandwidth demands, allowing multi-billion parameter models to run locally on consumer GPUs and edge hardware.
- Introduces quantization error trade-offs, where aggressive bit reduction (e.g., below INT4) can cause precision drift or loss of coherence.

## Connections & References
- [[03-large-language-model]]
- [[model-parameter]]
- [[ollama]]
- [[lm-studio]]