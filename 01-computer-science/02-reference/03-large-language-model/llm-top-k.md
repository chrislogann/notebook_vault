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

# Llm Top K

## Overview
> Top-K sampling is a decoding strategy that constrains the vocabulary choices at each token generation step to the $K$ most probable tokens predicted by the model distribution, mitigating the risks associated with generating extremely low-probability but unique tokens.

## Core Concepts
- **Temperature Sampling:** Often used in conjunction with Top-K; adjusting the temperature ($\tau$) parameter modifies the sharpness of the probability distribution before selection.
- **Mechanism:** The system calculates the probabilities for all possible next tokens, identifies the $K$ highest-probability tokens based on their likelihoods, and then resamples the token only from that reduced set, ensuring coherence while maintaining variety.
- **Hyperparameter Tuning:** The value of $K$ (the number of tokens to keep) is a critical hyperparameter requiring careful tuning; too small makes text repetitive, while too large approaches greedy sampling variance.

## Connections & References
- [[03-large-language-model]]
- [[temperature-sampling]]
- [[beam-search]]
- [[nucleus-top-p-sampling]]
