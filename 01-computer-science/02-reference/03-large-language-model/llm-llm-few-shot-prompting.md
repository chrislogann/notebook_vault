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

# Llm Llm Few Shot Prompting

## Overview
> Few-shot prompting is a technique used to improve the performance of large language models (LLMs) by providing them with several examples of the desired input-output format directly within the prompt context. This acts as an in-context learning mechanism, guiding the model's understanding toward a specific task or style without requiring model fine-tuning.

## Core Concepts
- **In-Context Learning (ICL):** The ability of LLMs to learn from examples provided in the prompt without updating their underlying weights. Few-shot prompting is one primary method of leveraging ICL.
- **Prompt Engineering:** This refers to the art and science of structuring input prompts to elicit the desired behavior or output from a generative AI model. Providing examples (few shots) is a core technique within this discipline.
- **Zero-Shot vs. Few-Shot:** Zero-shot prompting relies solely on instructions ("Translate X to Y"). Few-shot prompting adds demonstrations ("X was translated to Y; therefore, Z should be translated to W"), significantly improving reliability for nuanced tasks like classification or formatting.

## Connections & References
- [[llm-prompt-engineering]]
- [[03-large-language-model]]
- [[in-context-learning]]
