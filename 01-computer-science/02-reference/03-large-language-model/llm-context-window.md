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

# Llm Context Window

## Overview
> The context window defines the maximum amount of input text (measured in tokens) that a Large Language Model can consider at any single time when generating a response, acting as the model's working memory limit.

## Core Concepts
- **Token Limit:** The actual size constraint is defined by the number of tokens—chunks of words or characters—and this limit dictates how much history (input prompt + previous output) the model can remember.
- **Computational Overhead:** Because standard Transformer architectures use an attention mechanism, the computational complexity grows quadratically ($O(N^2)$) with respect to the context window size ($N$), making extremely large windows computationally expensive.
- **Contextual Decay:** While models are trained on large contexts, performance can degrade for information placed far from the prompt's start or end, a phenomenon sometimes linked to attention decay.

## Connections & References
- [[03-large-language-model]]
- [[transformer-architecture]]
- [[attention-mechanism]]
- [[tokenization]]
