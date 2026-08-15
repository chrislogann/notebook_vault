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

# Llm Lmm Flash Attention

## Overview
> Flash Attention is an optimized memory and compute algorithm designed for Transformer models that dramatically speeds up the attention mechanism by minimizing the number of expensive High Bandwidth Memory (HBM) reads/writes, thus significantly improving efficiency on modern hardware accelerators.

## Core Concepts
- **Memory Optimization:** Instead of computing the full $Q \times K^T$ matrix and storing it in HBM, Flash Attention computes key components directly within fast on-chip SRAM memory, eliminating redundant I/O operations.
- **Gradient Recomputation (Logit Recompute):** It cleverly handles the calculation of gradients by recomputing them efficiently during the backward pass without requiring excessive temporary storage, allowing for larger batch sizes and longer contexts.
- **Mathematical Stability:** The algorithm maintains numerical stability while transforming the sequence length dependence from quadratic ($O(N^2)$) to nearly linear complexity relative to the sequence length ($O(N)$), where $N$ is the context window size.

## Connections & References
- [[03-large-language-model]]
- [[transformer-architecture]]
- [[attention-mechanism]]
- [[memory-hierarchy]]
