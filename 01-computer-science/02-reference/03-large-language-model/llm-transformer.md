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

# Llm Transformer

## Overview
> The Transformer architecture revolutionized NLP by replacing recurrence (RNNs) entirely with self-attention mechanisms, allowing for massive parallelization during training while efficiently modeling long-range dependencies in sequence data.

## Core Concepts
- **Self-Attention Mechanism:** Allows the model to weigh the importance of different tokens relative to each other when processing a specific token, calculating contextually rich embeddings.
- **Positional Encoding:** Since self-attention processes all tokens simultaneously (losing sequential order), positional encodings are added to the input embeddings to inject critical information about the token's location within the sequence.
- **Encoder-Decoder Structure:** The full model typically uses an encoder stack to process the source sequence and a decoder stack, which is masked (preventing future lookahead) and attends both to the encoded output and its own previously generated tokens.

## Connections & References
- [[Self-Attention Mechanism]]
- [[Positional Encoding]]
- [[03-large-language-model]]
