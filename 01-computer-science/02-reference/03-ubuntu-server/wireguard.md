---
domain: 01-computer-science
class: 02-reference
subject: 03-ubuntu-server
type: note
status: active
created: 2026-07-27 18:05:00
updated: 2026-07-27 18:05:00
aliases: [WireGuard, WireGuard VPN]
author: ""
source: "Gemini 3.1 Flash Lite"
tags: [wireguard, vpn, security, network, ubuntu-server]
---

# Wireguard

## Overview
> WireGuard is a modern, high-performance VPN protocol integrated directly into the Linux kernel to provide fast, minimal, and secure encrypted network tunnels.

## Core Concepts
- **Kernel-Level Performance:** Operates inside the Linux kernel to deliver higher throughput and lower latency compared to user-space VPN implementations.
- **Public Key Cryptography:** Authenticates peers using public/private key pairs and state-of-the-art primitives (Curve25519, ChaCha20, Poly1305).
- **Stealth Architecture:** Drops unauthenticated UDP packets silently, leaving the server invisible to external network port scanners.

## Connections & References
- [[03-ubuntu-server]]
- [[tailscale]]
- [[03-network]]
- [[docker]]