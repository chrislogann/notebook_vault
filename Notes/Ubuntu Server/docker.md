---
tags:
  - Note
  - AI
Topic:
  - "[[containerization]]"
Genre:
  - "[[Ubuntu Server]]"
Source Name:
  - "[[notebook_vault/Library/AI/Gemini 3.1 Flash Lite|Gemini 3.1 Flash Lite]]"
---
At its simplest, **Docker is a tool that allows you to package an application and everything it needs to run—code, libraries, settings, and dependencies—into a single, lightweight, portable unit called a "container."**

Think of it like a **shipping container** for software. Just as a physical shipping container can be moved from a truck to a train to a ship without anyone needing to know what is inside, a Docker container can be moved from your laptop to your Ubuntu Server without you needing to worry about whether the server has the right version of Python, PHP, or database software installed.

### The Core Problem Docker Solves
Before Docker, developers often faced the "it works on my machine" problem. You might spend hours configuring your Ubuntu Server to run a specific version of a database, only to find that the application requires a different version, or that a system update broke your configuration.

Docker eliminates this by providing **isolation**. Each container runs in its own environment, completely separate from the host operating system and other containers.

### Key Terminology
*   **Image:** Think of this as a "blueprint" or a "recipe." It is a read-only file that contains the instructions for how to build your container. You download these from registries like Docker Hub.
*   **Container:** This is the "running instance" of an image. It is the actual, active process running on your server. You can start, stop, and delete containers without affecting the host system.
*   **Docker Engine:** The background service (daemon) that actually runs and manages your containers.
*   **Docker Compose:** A tool that lets you define a multi-container application (like running Nextcloud, a database, and a reverse proxy all at once) in a single text file called `docker-compose.yml`.

### Why use it on Ubuntu Server?
1.  **Cleanliness:** You don't clutter your server's main system files with dozens of different software packages. If you want to uninstall an app, you just delete the container and its data folder—no "leftover" files remain.
2.  **Version Control:** If you want to test a new version of Gitea, you can spin up a new container in seconds. If it breaks, you just delete it and go back to your old one.
3.  **Portability:** If you ever decide to move your services to a different server or a cloud provider, you simply copy your data folders and your `docker-compose.yml` file. Everything will work exactly the same way on the new machine.

### A Simple Analogy
If your **Ubuntu Server** is a house:
*   **Traditional installation** is like building a custom room for every hobby (a darkroom for photography, a workshop for woodworking). If you move, you can't take those rooms with you.
*   **Docker** is like having **modular, self-contained pods** that you can plug into the house. If you move to a new house, you just unplug your pods and plug them into the new one. Everything inside the pod stays exactly as you left it.

Since you have a [[docker]] note open, you might want to copy this summary into it as a high-level definition!

### Suggested Structure for your [[docker]] note:

- **Global Configuration:**
    - Path to your main `docker-compose` directory (e.g., `/opt/docker/`).
    - Global environment variables or network settings (e.g., a shared `proxy` network for your reverse proxy).
- **Service Inventory (The "Stack"):**
    - A table or list of your active containers:
        | Service | Port | Volume Path | Purpose |
        | :--- | :--- | :--- | :--- |
        | Nextcloud | 8080 | `/mnt/data/nextcloud` | File Storage |
        | Gitea | 3000 | `/mnt/data/gitea` | Code Hosting |
        | Pi-hole | 53 | `/mnt/data/pihole` | DNS/Ad-blocking |
- **Essential Commands (Cheat Sheet):**
    - `docker compose up -d` (Start services)
    - `docker compose pull && docker compose up -d` (Update services)
    - `docker compose logs -f <service>` (Troubleshooting)
    - `docker system prune` (Cleanup unused images/containers)
- **Backup Strategy:**
    - Document the specific command or script you use to back up your Docker volumes (e.g., `rsync` or `tar` commands).
- **Troubleshooting Log:**
    - A space to note common errors you encounter (e.g., port conflicts, permission issues with volumes).

### Why this approach works:
By treating your [[docker]] note as a **central registry**, you bridge the gap between your individual service notes ([[nextcloud]], [[gitea]], etc.) and the actual infrastructure running them. When you need to perform maintenance, you won't have to hunt for the configuration paths—they will all be indexed in one place.