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
  - Model Parameters
  - Weights and Biases
author: ""
source: Gemma4
tags:
  - large-language-model
  - parameters
  - deep-learning
---

# Model Parameter

## Overview
> Model parameters are the internal learnable weights and biases within a neural network that encode statistical relationships learned during training.

## Core Concepts
- Total parameter count ($N$) quantifies model capacity, where larger counts generally enable higher emergent reasoning abilities.
- Parameters (learned weights) differ fundamentally from hyperparameters (external pre-training configurations like learning rate).
- Parameter-efficient techniques (e.g., LoRA) adapt base model behavior by updating low-rank matrices rather than all full weights.

## Connections & References
- [[03-large-language-model]]
- [[model]]
- [[quantization]]