---
domain: 01-computer-science
class: 02-reference
subject: 03-ubuntu-server
type: note
status: active
created: 2026-07-27 18:05:00
updated: 2026-07-27 18:05:00
aliases: [Samba, SMB File Sharing, NAS]
author: ""
source: "Gemini 3.1 Flash Lite"
tags: [samba, smb, storage, lan, ubuntu-server]
---

# Samba

## Overview
> Samba is an open-source software suite implementing the SMB/CIFS protocol to provide seamless local network file and print sharing across cross-platform clients.

## Core Concepts
- **Cross-Platform Interoperability:** Bridges Linux server file systems with Windows, macOS, and Linux network clients.
- **High-Speed LAN Performance:** Optimized for high-bandwidth local area network operations such as raw file transfers, system backups, and media streaming.
- **Granular Access Control:** Configured via `/etc/samba/smb.conf` with dedicated SMB user authentication and per-share permission rules.

## Connections & References
- [[03-ubuntu-server]]
- [[03-network]]
- [[nextcloud]]