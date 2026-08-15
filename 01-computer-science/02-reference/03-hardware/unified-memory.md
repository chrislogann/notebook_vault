---
domain: 01-computer-science
class: 02-reference
subject: 03-hardware
type: note
status:
  - complete
created: 2026-07-30 22:03
updated: 2026-07-30 22:03
aliases: []
author:
source: gemma4
tags: []
---

# Unified Memory

## Overview
> Unified memory architecture integrates CPU, GPU, and specialized accelerators accessing a single pool of physical RAM, simplifying memory management and improving data coherence by eliminating redundant data transfers across discrete interconnects.

## Core Concepts
- **Coherent Access:** By sharing a single address space, all processing units (CPU cores and GPU shaders) operate on the most current version of the data without complex caching protocols or expensive cache-coherence messages typical in separate memory architectures.
- **Reduced Bottlenecks:** The elimination of high-latency copies required between distinct device memories (e.g., VRAM to system RAM) drastically reduces I/O bottlenecks, particularly crucial for workloads involving continuous data streams like AI training and simulations.
- **Programming Simplification:** Developers benefit from a simpler model where they do not need explicit memory management calls or complex kernel passes to migrate data between segregated device memories; the operating system and runtime environment handle resource allocation seamlessly across the unified pool.

## Connections & References
- [[03-operating-system]] (For discussion on virtual memory mapping)
- [[03-hardware]] (General hardware architectures comparison)
- [[03-large-language-model]] (How LLMs specifically benefit from increased bandwidth and coherence)
