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
  - RAG
  - Grounded Generation
author: ""
source: Gemma4
tags:
  - large-language-model
  - rag
  - retrieval
---

# Retrieval Augmented Generation

## Overview
> Retrieval-Augmented Generation (RAG) integrates external document retrieval with an LLM prompt to ground model responses in verifiable, up-to-date facts.

## Core Concepts
- Mitigates core LLM limitations such as static knowledge cutoff dates, lack of source attribution, and statistical hallucinations.
- Operates via a three-stage pipeline: document indexing into vector databases, similarity search retrieval, and augmented prompt generation.
- Provides a cost-effective alternative to continuous pre-training or fine-tuning when integrating expanding enterprise knowledge bases.

## Connections & References
- [[03-large-language-model]]
- [[model-vector]]
- [[retrieval-failure]]