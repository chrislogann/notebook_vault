---
domain: 01-computer-science
class: 02-reference
subject: 03-hardware
type: note
status: wip
created: 2026-07-27 17:46:28
updated: 2026-07-27 17:46:28
aliases: [Video Random Access Memory, Video RAM]
author: ""
source: "Gemma4"
tags: [hardware, memory, vram, gpu]
---

# Vram

## Overview
> Video Random Access Memory (VRAM) is specialized, high-speed memory physically localized on the GPU to store and rapidly access data required for rendering graphical assets and parallel computations.

## Core Concepts
- VRAM acts as an ultra-fast cache for storing texture data, frame buffers, geometry meshes, and render targets, feeding GPU cores instantaneously.
- It utilizes specialized standards (like GDDR6X) to achieve significantly higher bandwidth and parallel read/write throughput than general system DDR memory.
- Insufficient VRAM capacity creates severe bottlenecks, forcing the GPU to swap data with slower system RAM (paging) which drastically degrades application performance and graphical fidelity.

## Connections & References
- [[03-hardware]]
- [[gpu]]
- [[ram]]