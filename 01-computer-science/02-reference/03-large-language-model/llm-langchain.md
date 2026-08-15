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

# Langchain

## Overview
> LangChain is a powerful framework designed to simplify the development of complex applications powered by Large Language Models (LLMs). It provides standardized interfaces and components for chaining together multiple steps, tools, and data sources into cohesive application logic.

## Core Concepts
- **Chains:** The fundamental mechanism in LangChain, allowing developers to sequence calls—for example, passing the output of a summarization step as the input prompt for a classification model.
- **Agents:** Advanced execution loops that enable LLMs to act like sophisticated decision-makers. An Agent uses an underlying reasoning framework (often based on specific prompts) to determine which tools it needs and in what order to use them to achieve a final goal.
- **Retrieval Augmented Generation (RAG):** A critical pattern implemented via LangChain, where the LLM does not rely solely on its internal training knowledge, but instead retrieves relevant external context (e.g., from a vector database) before generating an informed response.

## Connections & References
- [[03-large-language-model]]
- [[llm-prompt-engineering]]
- [[model-vector]]
- [[managing-dependencies]]
