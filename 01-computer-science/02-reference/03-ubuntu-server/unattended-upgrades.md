---
domain: 01-computer-science
class: 02-reference
subject: 03-ubuntu-server
type: note
status: active
created: 2026-07-27 18:05:00
updated: 2026-07-27 18:05:00
aliases: [Unattended Upgrades, Automated Patching]
author: ""
source: "Gemini 3.1 Flash Lite"
tags: [unattended-upgrades, automation, maintenance, security, ubuntu-server]
---

# Unattended Upgrades

## Overview
> Unattended-upgrades is an automated system utility for Ubuntu Server that periodically fetches and installs security patches to maintain system security without manual intervention.

## Core Concepts
- **Automated Security Patching:** Minimizes system exposure windows by applying security hotfixes automatically in the background.
- **Configurable Control:** Managed via `/etc/apt/apt.conf.d/50unattended-upgrades` to restrict update origins, blacklist unstable packages, or set automated reboot windows.
- **Low-Maintenance Operating Model:** Essential for headless server administration, guaranteeing critical software bugs are patched while keeping overall OS stability intact.

## Connections & References
- [[03-ubuntu-server]]