---
tags:
  - Note
  - AI
Topic:
  - "[[VPN]]"
Genre:
  - "[[Ubuntu Server]]"
Source Name:
  - "[[notebook_vault/Library/AI/Gemini 3.1 Flash Lite|Gemini 3.1 Flash Lite]]"
---
**WireGuard** is a modern, high-performance VPN (Virtual Private Network) protocol designed to be faster, simpler, and more secure than older standards like IPsec or OpenVPN. It is widely considered the "gold standard" for self-hosted remote access on Ubuntu Server.

### Core Characteristics
- **Performance:** WireGuard is built directly into the Linux kernel, which allows it to achieve significantly higher throughput and lower latency compared to user-space VPN solutions.
- **Simplicity:** The codebase is extremely small (around 4,000 lines of code), making it easy to audit for security vulnerabilities.
- **Modern Cryptography:** It uses state-of-the-art cryptographic primitives (like Curve25519, ChaCha20, and Poly1305) by default, ensuring robust security without complex configuration.
- **Stealth:** By default, WireGuard does not respond to unauthenticated packets, making the server "invisible" to port scanners.

### How it Works
- **Public/Private Keys:** Similar to SSH, WireGuard uses public/private key pairs for authentication. You exchange public keys between the server (the "peer") and your client devices (phone, laptop, etc.).
- **Interface-based:** It creates a virtual network interface (e.g., `wg0`) on your Ubuntu Server, which acts as a tunnel for your traffic.
- **Roaming:** WireGuard handles IP address changes seamlessly. If you switch from Wi-Fi to cellular data on your phone, the VPN connection stays active without needing to reconnect.

### Deployment on Ubuntu Server
1. **Installation:** Easily installed via `sudo apt install wireguard`.
2. **Configuration:** Managed via the `/etc/wireguard/wg0.conf` file. You define the server's private key, the listening port, and the public keys of the allowed clients.
3. **Tools:** Many users utilize tools like **WireGuard-UI** or **wg-easy** (which run in Docker) to provide a web-based dashboard for managing client keys and QR codes, making setup much more user-friendly.

### Implementation Considerations
- **Port Forwarding:** To access your home network from the internet, you must forward the chosen UDP port on your router to your Ubuntu Server.
- **Split Tunneling:** You can configure WireGuard to route *only* traffic destined for your home network through the VPN, while letting general internet traffic go through your local ISP, which saves bandwidth and improves speed.
- **Security:** Because it is a VPN, it is the primary way to securely access your [[nextcloud]], [[gitea]], or other internal services without exposing them directly to the public internet.

### Relationship to your other notes
- **[[Network]]**: WireGuard is the secure "pipe" that connects your remote devices to your local network.
- **[[docker]]**: Running WireGuard in a Docker container (like `wg-easy`) is a popular way to keep your VPN configuration isolated and easy to manage.
- **[[Ubuntu Server]]**: Your server acts as the "VPN Gateway," allowing you to securely reach your home lab from anywhere in the world.

Since you have a [[wireguard]] note open, you might use it to store your server's public key, the configuration templates for your client devices, or the specific IP range (e.g., `10.13.13.0/24`) you assign to your VPN tunnel.