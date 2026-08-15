---
domain: 01-computer-science
class: 02-reference
subject: 03-encoding
type: note
status: wip
created: 2026-07-27 17:42:47
updated: 2026-07-27 17:42:47
aliases: [Floating-Point Precision, FP16, FP32]
author: ""
source: "Gemma4"
tags: [encoding, floating-point, precision]
---

# Float 16 And 32

## Overview
> Floating-point precision standards, dictated by IEEE 754, govern how real numbers are divided into a sign, exponent, and mantissa, requiring a careful balance between numerical accuracy and computational speed.

## Core Concepts
- Float 32 (Single Precision) offers a robust balance of range and precision, historically serving as the standard for general scientific computation and simulations.
- Float 16 (Half Precision) significantly reduces memory bandwidth and accelerates computation on specialized hardware like GPUs, making it ideal for deep learning and graphics shading.
- Quantization error happens when moving from higher to lower precision, losing decimal accuracy and requiring mitigation techniques like Mixed Precision Training to maintain algorithmic stability.

## Connections & References
- [[03-encoding]]
- [[binary-scheme]]