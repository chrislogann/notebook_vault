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

# Llm Base

## Overview
> A large language model base refers to a foundational LLM that has undergone extensive unsupervised pre-training on massive, diverse datasets (like the entire internet corpus). These models learn general linguistic patterns and world knowledge without being explicitly trained for a single task.

## Core Concepts
- **Pre-training:** The initial phase where the model learns to predict masked tokens or the next token in a sequence (causal modeling). This process establishes a vast, generalized internal representation of syntax, semantics, and world facts.
- **Emergent Abilities:** Due to sheer scale and data diversity, base models sometimes exhibit abilities (such as complex reasoning or code generation) that were not explicitly taught during training and appear suddenly as parameters increase.
- **Zero/Few-Shot Learning:** A key property of the base model is its ability to perform tasks it has never been specifically fine-tuned for, relying solely on natural language instructions provided in the prompt.

## Connections & References
- [[03-computational-thinking]]
- [[03-large-language-model]]
- [[llm-transformer]]
