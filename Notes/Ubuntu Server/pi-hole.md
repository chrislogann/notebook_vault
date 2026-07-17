---
tags:
  - Note
  - AI
Topic:
  - "[[DNS]]"
Genre:
  - "[[Ubuntu Server]]"
Source Name:
  - "[[notebook_vault/Library/AI/Gemini 3.1 Flash Lite]]"
---
Pi-hole is a network-wide ad-blocking and DNS sinkhole application. When installed on an Ubuntu Server, it acts as a DNS server for your entire network, intercepting requests for known ad-serving and tracking domains and returning a "null" response, effectively preventing those requests from ever reaching your devices.

### Core Functionality
- **DNS Sinkholing:** By acting as the primary DNS server for your router or individual devices, Pi-hole filters traffic at the network level.
- **Ad Blocking:** It blocks advertisements, trackers, and malicious domains across all devices on your network—including smart TVs, mobile phones, and IoT devices—without requiring individual software installations.
- **Network Statistics:** It provides a web-based dashboard that visualizes your network traffic, showing you which devices are making the most requests and which domains are being blocked.

### Key Advantages
- **Performance:** By blocking ads and trackers before they are downloaded, web pages often load faster and consume less bandwidth.
- **Privacy:** It prevents many telemetry and tracking services from "phoning home," enhancing the overall privacy of your home network.
- **Centralized Control:** You manage your blocklists in one place, and changes apply instantly to every device connected to your network.

### Deployment on Ubuntu Server
1. **Installation:** The standard method is the automated script provided by the Pi-hole team (`curl -sSL https://install.pi-hole.net | bash`), which handles the installation of the web server (Lighttpd), PHP, and the DNS resolver (FTL).
2. **Docker/Docker Compose:** Highly recommended for Ubuntu Server users. Running Pi-hole in a container keeps it isolated and makes updates and backups significantly easier.
3. **Configuration:** Once installed, you point your router's DHCP settings to the IP address of your Ubuntu Server. All devices on your network will then automatically use Pi-hole for DNS resolution.

### Implementation Considerations
- **Upstream DNS:** You must configure which "upstream" DNS servers Pi-hole should use for legitimate requests (e.g., Cloudflare, Google, or Quad9).
- **Redundancy:** If your Ubuntu Server goes down, your entire network will lose internet connectivity because DNS resolution will fail. It is often wise to have a secondary DNS server configured or a backup plan.
- **Unbound Integration:** Many users pair Pi-hole with **Unbound** (a recursive DNS resolver) to create a fully private, self-hosted DNS chain that does not rely on third-party providers like Google or Cloudflare.

### Relationship to your other notes
- **[[Network]]**: Pi-hole is a critical component of your network infrastructure, acting as the "gatekeeper" for all outbound traffic.
- **[[Ubuntu Server]]**: Serving as the host, your Ubuntu Server provides the stability required for a 24/7 DNS service.