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
  - Long Context Window
  - Extended Context
author: ""
source: Gemma4
tags:
  - large-language-model
  - long-context
  - attention
---

# Long Context

## Overview
> Long context capabilities enable an LLM to retain coherence, recall details, and reason across expanded input token lengths exceeding standard model limits.

## Core Concepts
- Standard self-attention introduces a $O(n^2)$ computational and memory bottleneck as input sequence length $n$ scales.
- Efficient mechanisms like FlashAttention and State Space Models (SSMs) reduce computational complexity toward linear scaling.
- Extended context reduces reliance on chunked retrieval while introducing challenges such as the "lost-in-the-middle" recall drop.

## Connections & References
- [[03-large-language-model]]
- [[token]]
- [[retrieval-augmented-generation]]