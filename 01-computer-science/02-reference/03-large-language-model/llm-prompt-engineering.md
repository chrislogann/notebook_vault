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

# Llm Prompt Engineer

## Overview
> Prompt Engineering is the discipline of structuring input prompts and contexts provided to a large language model (LLM) to elicit specific, reliable, and high-quality outputs that align with desired operational goals or analytical structures. It treats the prompt itself as a specialized form of code or instruction set.

## Core Concepts
- **Zero-shot Prompting:** Providing only the task description without any examples, relying solely on the LLM's pre-trained knowledge base to complete the request. This is suitable for simple classification or general retrieval tasks.
- **Few-Shot Learning (FSL):** Including a small set of example input/output pairs within the prompt itself. These concrete examples demonstrate the desired format, tone, and reasoning pattern, significantly improving task specificity and consistency.
- **Chain-of-Thought (CoT) Prompting:** Directing the LLM to reason step-by-step before providing a final answer ("Let's think step by step"). This technique activates deep reasoning pathways within the model, dramatically improving performance on complex arithmetic, logical deduction, and multi-stage planning problems.
- **Role Definition & Constraint Setting:** Explicitly assigning the AI a persona or role (e.g., "You are a seasoned quantum physicist...") and imposing strict output constraints (e.g., "Respond only in JSON format with keys 'title' and 'summary'") to maximize reliability and minimize hallucination.

## Connections & References
- [[03-large-language-model]]
- [[structured-data]]
- [[03-computational-thinking]]
- [[prompt-chaining]]
