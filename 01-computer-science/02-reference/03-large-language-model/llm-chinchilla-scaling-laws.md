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

# Llm Chinchilla Scaling Laws

## Overview
> The Chinchilla scaling laws establish an empirically determined optimal balance between model size (parameters) and the quantity of training tokens, arguing that models are typically under-trained if they are very large but trained on insufficient data relative to their parameter count.

## Core Concepts
- **Optimal Data Ratio:** High-performing LLMs should be scaled such that the total number of tokens seen during pre-training aligns with a specific ratio (e.g., 20M parameters per 600B tokens, or adjusting for model architecture) rather than simply maximizing parameter count alone.
- **Under-Training Penalty:** When models are trained on less data than required by their size, they exhibit significant performance degradation, suggesting that compute resources are better allocated to increasing dataset volume or optimizing the training regimen rather than just raw parameters.
- **Efficiency and Scaling Tradeoffs:** The laws provide a crucial guide for resource allocation, demonstrating how prioritizing efficient use of available tokens through massive datasets can outperform simply building larger models with limited data exposure.

## Connections & References
- [[03-large-language-model]]
- [[data-scaling]]
- [[model-compute-budgeting]]
- [[tokenization-strategy]]
