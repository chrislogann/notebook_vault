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

# Llm Temperature

## Overview
> Temperature is a parameter used in probabilistic text generation that controls the randomness and creativity of an LLM's output. It functions by rescaling the model's raw prediction scores (logits) before they are converted into probability distributions.

## Core Concepts
- **Probability Scaling:** Mathematically, temperature adjusts the exponential calculation within the softmax function ($\text{softmax}(\frac{\text{logits}}{T})$). A higher $T$ (Temperature) flattens the distribution, increasing the probability mass assigned to lower-ranked tokens.
- **Deterministic vs. Creative Output:** Setting Temperature near 0 forces the model into a greedy search, selecting only the token with the absolute highest probability and leading to highly deterministic, safe, but potentially repetitive output. Conversely, high temperatures allow for more unlikely tokens, increasing diversity but risking incoherence or topic drift.
- **Sampling Method Interplay:** Temperature is most effective when paired with sampling methods like Top-$K$ or Top-$P$, which constrain the selection pool to prevent catastrophic failure regardless of temperature settings.

## Connections & References
- [[03-large-language-model]]
- [[sampling-strategy]]
- [[probability-distribution]]
