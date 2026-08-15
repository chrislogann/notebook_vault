---
domain: 01-computer-science
class: 02-reference
subject: 03-ubuntu-server
type: note
status: active
created: 2026-07-27 18:05:00
updated: 2026-07-27 18:05:00
aliases: [Pi-hole, DNS Sinkhole]
author: ""
source: "Gemini 3.1 Flash Lite"
tags: [pi-hole, dns, ad-blocking, network, ubuntu-server]
---

# Pi Hole

## Overview
> Pi-hole is a network-wide DNS sinkhole and ad blocker that filters advertising and tracking domains before they reach local network endpoints.

## Core Concepts
- **DNS Sinkholing:** Serves as the network's primary DNS resolver, intercepting known ad-serving domains and returning null IP responses.
- **Network-Level Protection:** Blocks ads and telemetry across all connected hardware—including smart TVs, smartphones, and IoT devices—without client software installation.
- **Deployment:** Deployed efficiently via Docker containers or automated scripts, often paired with recursive resolvers like Unbound for enhanced privacy.

## Connections & References
- [[03-ubuntu-server]]
- [[03-network]]
- [[docker]]