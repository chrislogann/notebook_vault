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

# Llm Tiktoken

## Overview
> Tokenization is the process of converting raw text into numerical units (tokens) that a Language Model can process. Modern tokenizers, like those derived from Byte Pair Encoding (BPE), break down complex words into common sub-word units, managing vocabulary size efficiently and enabling robust handling of Out-Of-Vocabulary (OOV) words.

## Core Concepts
- **Sub-Word Tokenization:** Instead of treating every word as a single unit, tokenizers break them into smaller components (e.g., 'tokenization' $\rightarrow$ 'token', 'iz', 'ation'). This approach vastly reduces the necessary vocabulary size while maintaining semantic integrity.
- **Byte Pair Encoding (BPE):** BPE is a statistical method that iteratively merges the most frequently occurring character pairs in a corpus to build an optimal vocabulary. It balances compression and representation accuracy, making it foundational for modern transformer architectures.
- **Vocabulary Size & Efficiency:** The tokenizer's vocabulary defines the maximum unique tokens the model can recognize. A well-designed tokenizer must maintain a balance between minimizing code length (efficiency) and retaining semantic detail (accuracy).

## Connections & References
- [[03-large-language-model]]
- [[03-encoding]]
- [[03-computational-thinking]]
