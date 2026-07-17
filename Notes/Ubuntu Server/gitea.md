---
tags:
  - Note
  - AI
Topic:
  - "[[Network]]"
  - "[[versioning]]"
Genre:
  - "[[Ubuntu Server]]"
  - "[[Git]]"
Source Name:
  - Gemini 3.1 Flash Lite
---
Gitea is a lightweight, self-hosted Git service that is highly popular for deployment on Ubuntu Server due to its minimal resource footprint and ease of use. It is often described as a "lightweight GitHub" alternative.

### Core Characteristics
- **Resource Efficiency:** Written in Go, Gitea is extremely fast and consumes very little RAM, making it an excellent choice for low-power hardware like Raspberry Pis or small VPS instances.
- **Self-Hosted:** Like Nextcloud, Gitea gives you full control over your source code, issue tracking, and pull requests, ensuring your development data remains on your own infrastructure.
- **Feature Set:** Despite its small size, it includes robust features:
    - Repository management (Git LFS support).
    - Issue tracking, Kanban boards, and wikis.
    - Built-in CI/CD (via Gitea Actions).
    - User management with organization and team support.

### Deployment on Ubuntu Server
1. **Binary Installation:** You can run Gitea as a standalone binary, which is the simplest way to get started.
2. **Docker/Docker Compose:** This is the recommended approach for most Ubuntu Server users. It simplifies updates and keeps the application isolated from the host system.
3. **Package Managers:** While available in some repositories, using the official Docker image or the binary is generally preferred to ensure you are running the latest version.

### Integration with your Infrastructure
- **Database:** Gitea supports SQLite (default, great for small instances), PostgreSQL, and MySQL/MariaDB.
- **Reverse Proxy:** Similar to Nextcloud, you will typically place Gitea behind a reverse proxy (like Nginx, Caddy, or Traefik) to handle SSL/TLS termination and provide a clean URL.
- **Authentication:** Gitea supports LDAP, OAuth2, and PAM, allowing you to integrate it with your existing user management systems.

### Comparison to Nextcloud
While Nextcloud is focused on **file and document collaboration**, Gitea is focused on **code and project management**. Both are excellent additions to a home lab or private server environment.

Since you have a [[gitea]] note open, you might consider using it to document your repository structure, your chosen authentication method (e.g., LDAP or local), or your backup strategy for your Git repositories.