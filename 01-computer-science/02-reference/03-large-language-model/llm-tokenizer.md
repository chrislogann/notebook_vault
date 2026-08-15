---
domain: 01-computer-science
class: 02-reference
subject: 03-large-language-model
type: note
status:
  - complete
created: 2026-07-27 17:50:00
updated: 2026-07-27 17:50:00
aliases:
  - Tokenization
  - Subword Tokenizer
author: ""
source: Gemma4
tags:
  - large-language-model
  - tokenizer
  - nlp
---

# Tokenizer

## Overview
> A tokenizer is the pre-processing algorithm that segments raw text into subword units and maps them to fixed vocabulary IDs for model ingestion.

## Core Concepts
- Employs sub-word algorithms like Byte Pair Encoding (BPE), WordPiece, or SentencePiece to balance vocabulary size with out-of-vocabulary flexibility.
- Decomposes unknown or complex jargon into recognizable sub-units, preventing out-of-vocabulary execution failures.
- Efficiency directly governs context window density, memory utilization, and cross-lingual translation efficiency.

## Connections & References
- [[03-large-language-model]]
- [[token]]