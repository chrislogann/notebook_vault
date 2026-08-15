---
domain: 01-computer-science
class: 02-reference
subject: 03-ubuntu-server
type: note
status: active
created: 2026-07-27 18:05:00
updated: 2026-07-27 18:05:00
aliases: [Tailscale, Mesh VPN]
author: ""
source: "Gemini 3.1 Flash Lite"
tags: [tailscale, vpn, mesh-network, wireguard, ubuntu-server]
---

# Tailscale

## Overview
> Tailscale is a zero-configuration mesh VPN built on WireGuard that creates secure, peer-to-peer virtual private networks across remote devices.

## Core Concepts
- **Mesh Peer-to-Peer Architecture:** Interconnects nodes directly using NAT traversal techniques (STUN/ICE), reducing latency and bypassing port forwarding requirements.
- **Identity Provider Authentication:** Integrates authentication with existing Single Sign-On (SSO) and Multi-Factor Authentication (MFA) providers for access control.
- **Subnet and Exit Node Capabilities:** Allows Ubuntu Server to act as an exit gateway for public Wi-Fi security or a subnet router exposing private LAN endpoints.

## Connections & References
- [[03-ubuntu-server]]
- [[wireguard]]
- [[03-network]]