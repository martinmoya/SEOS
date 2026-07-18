# Skill: Docker Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Docker Software Engineer |
| Version | 1.0.0 |
| Language | Dockerfile / YAML (Compose) |
| Domain | Containerization |
| Target | AI Software Engineering Agent |

---

# Purpose

To build, ship, and run distributed applications reliably using containerization. This involves creating optimized, secure Docker images, orchestrating multi-container applications locally or in production via Docker Compose, and ensuring immutability and consistency across different environments.

---

# Primary Responsibilities

* Author efficient, multi-stage Dockerfiles to minimize image size and attack surface.
* Manage container lifecycles, networks, and persistent storage volumes.
* Implement caching strategies for Docker builds to reduce CI/CD pipeline execution time.
* Ensure container security through non-root users, minimal base images, and vulnerability scanning.
* Orchestrate local development environments using Docker Compose.

---

# Language Versions

* Dockerfile syntax (currently v1.7+).
* Docker Compose (currently V2 specification).
* *Evolution:* Transitioning from bash scripts in single-stage Dockerfiles to multi-stage builds and rootless containers.

---

# Coding Standards

* **Naming Conventions:** Use lowercase repository names, separated by hyphens (e.g., `my-app-api`). Tag images with semantic versions or Git commit SHAs, avoiding `latest` in production.
* **Linting:** Adhere to Hadolint rules for Dockerfile syntax and best practices.
* **Layer Caching:** Order Dockerfile instructions from least to most frequently changing to leverage build cache effectively.

---

# Software Engineering Principles

* **Immutability:** Containers should be treated as ephemeral and immutable; never modify a running container, rebuild the image instead.
* **Single Responsibility:** Run one primary process per container.
* **Configuration via Environment Variables:** Pass configuration and secrets via environment variables, not hardcoded in the Dockerfile.

---

# Design Patterns

* **Multi-stage Builds:** Use multiple `FROM` statements to compile build artifacts in one stage and copy only the final binaries to a minimal runtime stage.
* **Distroless Images:** Use Google's distroless or Alpine/Scratch as final base images to minimize OS-level vulnerabilities.
* **Healthchecks:** Implement `HEALTHCHECK` instructions to allow container orchestrators to manage container lifecycle accurately.

---

# Architecture Knowledge

* **Union File System:** Understand how Docker uses layered filesystems (OverlayFS) to store images and containers efficiently.
* **Network Models:** Understand bridge, host, overlay, and macvlan network drivers and their use cases.
* **Storage Drivers:** Differentiate between bind mounts, volumes, and `tmpfs` mounts for data persistence.

---

# Package Management

* **Registries:** Push images to Docker Hub, Amazon ECR, GitHub Container Registry, or private registries.
* **Artifact Management:** Use OCI (Open Container Initiative) standards for image formatting.

---

# Framework Knowledge

* **Docker Compose:** For defining and running multi-container Docker applications.
* **BuildKit:** Enable BuildKit (`DOCKER_BUILDKIT=1`) for advanced caching, multi-platform builds, and secret management.

---

# Database Skills

* **Data Persistence:** Use named volumes (`VOLUME` instruction or Compose volumes) to persist database data outside the container lifecycle.
* **Initialization:** Use entrypoint scripts (e.g., `/docker-entrypoint-initdb.d/`) to seed databases on first run.

---

# API Development

* **Port Exposure:** Use `EXPOSE` to document ports, but rely on `-p` (Compose) or orchestration to map ports to the host.
* **Internal Communication:** Use Docker DNS (service names as hostnames) for container-to-container API communication within custom networks.

---

# Security

* **Non-Root Execution:** Always create a dedicated user in the Dockerfile and switch to it (`USER appuser`).
* **Secrets:** Never bake secrets into images. Use Docker Secrets (Swarm), BuildKit secrets (`--secret`), or external secret managers.
* **Read-Only Filesystems:** Run containers with `--read-only` and mount `tmpfs` for writable directories (e.g., `/tmp`).

---

# Error Handling

* **Restart Policies:** Configure `restart: unless-stopped` or `restart: on-failure` in Compose to handle unexpected crashes.
* **Graceful Shutdown:** Ensure applications handle `SIGTERM` signals properly to allow Docker to stop containers gracefully without data loss.

---

# Performance

* **Image Size:** Keep images as small as possible to reduce pull times and attack surface.
* **Build Caching:** Use `.dockerignore` to exclude unnecessary files from the build context, speeding up builds.

---

# Testing

* **Integration Testing:** Use `testcontainers` or Docker Compose to spin up ephemeral dependencies (databases, message brokers) for testing.
* **Image Testing:** Use tools like `container-structure-test` to verify image contents and behavior.

---

# Static Analysis

* **Dockerfile Linting:** Use Hadolint to enforce best practices in Dockerfiles.
* **Vulnerability Scanning:** Use Trivy, Grype, or Snyk to scan images for known CVEs before pushing to a registry.

---

# Documentation

* **Dockerfile Comments:** Explain complex `RUN` commands or missing dependencies.
* **Compose Documentation:** Document environment variables in a `.env.example` file or Compose `environment` sections.

---

# Version Control

* **.dockerignore:** Ignore `node_modules`, `.git`, local secrets, and log files to keep the build context clean.

---

# Build Tools

* **Docker CLI:** `docker build`, `docker tag`, `docker push`.
* **Buildx:** For multi-architecture builds (e.g., AMD64 and ARM64).

---

# CI/CD

* **Pipelines:** Build, scan, and push images in CI pipelines. Use caching (e.g., GitHub Actions `docker/build-push-action` with cache-to/cache-from).
* **Tagging:** Automatically tag images with the Git commit SHA and branch name.

---

# Legacy Code

* **Containerization:** Incrementally containerize legacy monoliths. Start by externalizing configuration and state, then build a single Dockerfile.

---

# Code Review Checklist

* [ ] Is the Dockerfile using a multi-stage build?
* [ ] Is the application running as a non-root user?
* [ ] Are images tagged with specific versions rather than `latest`?
* [ ] Is there a `.dockerignore` file?
* [ ] Are secrets passed at runtime and not baked into the image?
* [ ] Is the base image updated to a recent, patched version?

---

# Communication Style

* Container-first mindset.
* Focus on immutability, layer efficiency, and minimal attack surface.

---

# Constraints
* Never run containers as `root` (UID 0).
* Never use the `latest` tag for production deployments.
* Do not store secrets, API keys, or passwords in Dockerfiles or environment files committed to version control.
