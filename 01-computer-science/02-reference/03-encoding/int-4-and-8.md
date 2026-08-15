---
domain: 01-computer-science
class: 02-reference
subject: 03-encoding
type: note
status: wip
created: 2026-07-27 17:42:47
updated: 2026-07-27 17:42:47
aliases: [Integer Bit Widths]
author: ""
source: "Gemma4"
tags: [encoding, integers, data-capacity]
---

# Int 4 And 8

## Overview
> Integer encoding defines the rules for converting base-10 values into fixed binary sequences, where the bit width heavily constrains data capacity and introduces computational limits.

## Core Concepts
- Bit capacity is strictly limited by the width $N$, yielding $2^N$ unique states (e.g., 4-bit yields 16 states, 8-bit yields 256 states).
- 4-bit integers (nibbles) are restricted to very small ranges (0 to 15 unsigned) and are primarily optimal for flags or low-level hardware registers.
- 8-bit integers (bytes) serve as the standard minimum unit across modern architectures for general storage and character encoding.
- Overflow occurs when an arithmetic operation exceeds the allocated bits' maximum capacity, forcing the data into a wrap-around behavior that can cause system failure.

## Connections & References
- [[03-encoding]]
- [[binary-scheme]]