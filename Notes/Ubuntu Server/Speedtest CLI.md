---
tags:
  - Note
  - AI
Topic:
  - "[[Network]]"
  - "[[CLI]]"
Genre:
  - "[[Ubuntu Server]]"
Source Name:
  - "[[notebook_vault/Library/AI/Gemini 3.1 Flash Lite|Gemini 3.1 Flash Lite]]"
---
The **Speedtest CLI** is a command-line interface tool developed by Ookla that allows you to measure your internet connection's performance (latency, download speed, and upload speed) directly from your terminal. On Ubuntu Server, it is an essential utility for monitoring network health and verifying that your ISP is delivering the bandwidth you are paying for.

### Core Functionality
- **Performance Metrics:** Provides accurate measurements of ping (latency), jitter, download speed, and upload speed.
- **Server Selection:** Automatically selects the best server based on proximity, or allows you to manually specify a server ID to test against specific geographic locations.
- **Data Export:** Supports output in formats like JSON, CSV, or TSV, which makes it perfect for logging and automation.

### Key Advantages
- **Headless Operation:** Unlike browser-based speed tests, the CLI version is lightweight and does not require a graphical interface, making it perfect for remote SSH sessions on your Ubuntu Server.
- **Automation-Ready:** Because it is a CLI tool, you can easily integrate it into cron jobs or shell scripts to log your internet speeds over time, helping you identify patterns of throttling or instability.
- **Accuracy:** By running the test directly on the server, you eliminate the overhead of your local network's Wi-Fi or internal hardware, providing a "cleaner" measurement of your ISP's performance.

### Deployment on Ubuntu Server
1. **Installation:** The official way to install it on Ubuntu is by adding the Ookla repository:
   - Import the GPG key.
   - Add the repository to your sources list.
   - Run `sudo apt update && sudo apt install speedtest`.
2. **Usage:** Simply type `speedtest` in your terminal to run a standard test.
3. **Advanced Usage:** Use `speedtest -L` to list available servers and `speedtest -s <server-id>` to target a specific test server.

### Implementation Considerations
- **Resource Usage:** While the tool is lightweight, running high-speed tests on a low-power server (like a Raspberry Pi) can occasionally be CPU-bound, which might slightly skew the results.
- **Data Usage:** Be aware that frequent automated speed tests can consume a significant amount of data, especially on high-speed fiber connections.
- **Network Context:** Since you have a [[Network]] note, this tool is a perfect companion for troubleshooting connectivity issues or verifying the impact of your [[pi-hole]] or firewall configurations.