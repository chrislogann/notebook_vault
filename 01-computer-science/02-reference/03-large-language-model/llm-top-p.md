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

# Llm Top P

## Overview
> Top-P sampling, or nucleus sampling, is a method used to control the randomness of text generation by selecting the smallest set of tokens whose cumulative probability exceeds a predefined threshold P. This focuses the model's attention on the most likely candidates at each step.

## Core Concepts
- **Cumulative Probability Threshold:** Instead of drawing from the entire vocabulary (as with low Top-P) or only considering the single highest probability token (greedy search), Top-P limits the selection pool to a "nucleus" defined by $P$.
- **Adaptive Sampling:** The size of the candidate pool dynamically changes. If the model is highly confident and the initial few tokens already exceed P, the nucleus will be very small. If it's uncertain, the nucleus expands to include more lower-probability options.
- **Relationship with Temperature:** Top-P is often used as an alternative or complementary control mechanism to 'Temperature' sampling. While temperature adjusts the sharpness of the entire probability distribution, Top-P truncates the tail end of the *sorted* distribution based on cumulative mass.

## Connections & References
- [[03-large-language-model]]
- [[Llm Temperature]]
- [[Greedy Decoding]]
- [[Nucleus Sampling]]
