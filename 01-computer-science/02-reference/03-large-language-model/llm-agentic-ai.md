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

# Llm Agentic Ai

## Overview
> An LLM agent is an autonomous system built around a Large Language Model (LLM) that enables it to perform complex, multi-step tasks by internalizing planning capabilities and interacting with external tools or environments. Unlike simple API calls, an agent can reason about the required steps, execute them sequentially, and adapt its plan based on the results received.

## Core Concepts
- **Planning & Reasoning:** Agents employ techniques like Chain-of-Thought (CoT) or ReAct (Reasoning and Acting) to break down high-level goals into a sequence of actionable sub-tasks, simulating human project management capabilities.
- **Tool Utilization:** They do not operate in a vacuum; agents are defined by their ability to select and use external tools (e.g., databases, code interpreters, APIs) as extensions of the LLM's knowledge base. This drastically expands their operational scope beyond simple text generation.
- **Feedback Loop & Self-Correction:** A core mechanism is the iterative feedback loop: the agent executes a step, receives an observation/result, and feeds that result back into the prompt for reflection, allowing it to correct errors or pivot its strategy dynamically until the goal state is reached.

## Connections & References
- [[03-large-language-model]]
- [[autonomous-agent]]
- [[tool-use-pattern]]
- [[complex-task-decomposition]]
