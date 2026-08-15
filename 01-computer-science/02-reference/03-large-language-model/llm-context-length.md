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

# Llm Context Length

## Overview
> Context length defines the maximum number of tokens an LLM can consider when generating a response, establishing the model's "working memory." Exceeding this limit causes the model to forget information provided early in the prompt or conversation history.

## Core Concepts
- **Token Limits:** The context window is measured in tokens (not words), and limits restrict both the input prompt size and the output generation size combined.
- **Lost-in-the-Middle:** Models tend to pay disproportionately more attention to information presented at the beginning or end of a long context, often degrading recall of key facts buried deep within the middle sections.
- **Attention Mechanism Constraint:** The underlying transformer architecture limits performance because computational complexity scales quadratically with the sequence length ($O(n^2)$), making very long contexts computationally expensive and challenging to manage.

## Connections & References
- [[llm-prompt-engineering]]
- [[attention-mechanism]]
- [[03-large-language-model]]
