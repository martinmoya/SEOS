# Skill: GitLab CI/CD Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | GitLab CI/CD Engineer |
| Version | 1.0.0 |
| Language | YAML |
| Domain | CI/CD & DevOps Automation |
| Target | AI Software Engineering Agent |

---

# Purpose

To automate the software development lifecycle using GitLab CI/CD. This involves defining robust `.gitlab-ci.yml` pipelines, managing GitLab Runners, utilizing Auto DevOps features, and ensuring secure, scalable, and efficient build, test, and deployment processes integrated natively with GitLab repositories.

---

# Primary Responsibilities

* Author efficient `.gitlab-ci.yml` files defining build, test, and deploy stages.
* Configure and manage GitLab Runners (shared, specific, or ephemeral via Docker/Kubernetes executors).
* Implement GitLab CI/CD components and hidden jobs/templates for reusability.
* Secure pipelines using GitLab Secrets, protected environments, and scoped variables.
* Integrate deeply with GitLab features like Merge Requests, Container Registry, and Package Registry.

---

# Language Versions

* YAML (GitLab CI/CD pipeline configuration).
* Shell (Bash/PowerShell) for script execution.
* *Evolution:* Transitioning from monolithic `.gitlab-ci.yml` files to modular `include` templates and CI/CD Components.

---

# Coding Standards

* **Naming Conventions:** Use clear job names prefixed by stage (e.g., `build:app`, `test:unit`, `deploy:prod`).
* **Keywords:** Adhere to GitLab CI/CD keyword schema (`stages`, `script`, `rules`, `needs`).
* **Template Reusability:** Use `include`, `extends`, and hidden jobs (`.` prefix) to avoid YAML duplication.

---

# Software Engineering Principles

* **DRY:** Use `include` to fetch external YAML templates and `extends` to inherit configurations.
* **Pipeline Efficiency:** Utilize DAG (Directed Acyclic Graph) via `needs` to run jobs out of stage order.
* **Infrastructure as Code:** Store `.gitlab-ci.yml` in the root of the repository.

---

# Design Patterns

* **Child/Parent Pipelines:** Use `trigger` to run complex, multi-step pipelines as child pipelines, keeping the main `.gitlab-ci.yml` clean.
* **Dynamic Pipelines:** Generate `.gitlab-ci.yml` dynamically in a script and trigger it, allowing for matrix-based or auto-generated jobs.
* **Environment & Deployments:** Use `environment` keyword to track deployments and implement protected environments.

---

# Architecture Knowledge

* **GitLab Runner Architecture:** Understand SaaS runners vs. self-managed runners, and executors (Docker, Shell, Kubernetes, Instance).
* **Executor Isolation:** Understand how the Docker executor isolates jobs and uses cache/volumes.
* **Pipeline Graphs:** Understand stage sequencing vs. DAG (`needs`) for optimized execution.

---

# Package Management

* **GitLab Container Registry:** Build, push, and pull Docker images using the integrated registry.
* **GitLab Package Registry:** Publish npm, Maven, PyPI, or NuGet packages directly from pipelines.

---

# Framework Knowledge

* **GitLab CLI (`glab`):** For interacting with GitLab APIs.
* **Auto DevOps:** Pre-built CI/CD configurations for rapid onboarding.

---

# Database Skills

* **Services:** Define database containers (e.g., PostgreSQL) under `services:` for integration testing.
* **Migrations:** Run schema migrations as dedicated jobs in the `deploy` stage.

---

# API Development

* **API Testing:** Run Postman collections or curl commands within `script` blocks.
* **Webhooks:** Trigger pipelines via GitLab API (`/trigger` endpoint) using pipeline trigger tokens.

---

# Security

* **Protected Variables:** Store secrets in CI/CD variables marked as "Protected" (only available on protected branches/tags) and "Masked" (hidden in logs).
* **Protected Environments:** Restrict deployment jobs to specific users or require manual approval.
* **Scanners:** Leverage built-in GitLab security scanners (SAST, DAST, Dependency Scanning, Container Scanning).

---

# Error Handling

* **Retry:** Use `retry` keyword to automatically retry jobs on transient failures.
* **Rules:** Use `rules:if` to skip jobs gracefully or run them only under specific conditions.
* **Allow Failure:** Use `allow_failure: true` for non-blocking jobs (e.g., linting) while still reporting status.

---

# Performance

* **Caching:** Use `cache` keyword with `key` to cache dependencies (e.g., `node_modules`, `.m2`) across jobs.
* **Artifacts:** Use `artifacts` to pass compiled binaries between jobs; keep `expire_in` short to save storage.
* **DAG (`needs`):** Bypass stage ordering to run independent jobs concurrently.

---

# Testing

* **Local Testing:** Use `gitlab-ci-local` to run and test `.gitlab-ci.yml` locally without pushing to GitLab.
* **CI Lint:** Use GitLab's built-in CI Lint API to validate YAML syntax.

---

# Static Analysis

* **Linting:** Validate `.gitlab-ci.yml` using GitLab UI or API.
* **Security Scanning:** Integrate `gitlab-sast` and `gitlab-dependency-scanning` templates.

---

# Documentation

* **README:** Document required CI/CD variables and environment setups.
* **Job Descriptions:** Use `description` keyword (or comments) to explain complex job logic.

---

# Version Control

* **.gitignore:** Ignore local CI test artifacts and `.env` files.
* **Branch Rules:** Ensure `.gitlab-ci.yml` is reviewed via Merge Requests.

---

# Build Tools

* **Predefined Variables:** Utilize `$CI_REGISTRY_IMAGE`, `$CI_COMMIT_SHA`, `$CI_ENVIRONMENT_NAME`.
* **Docker-in-Docker:** Use `dind` service for building Docker images within pipelines.

---

# CI/CD

* **Continuous Integration:** Trigger on `push` and `merge_request_event`.
* **Continuous Deployment:** Trigger on `push` to `main` with `environment: production` and manual `when: manual` gates.

---

# Legacy Code

* **Migration:** Transition from Jenkins to GitLab CI by mapping Jenkins stages to GitLab jobs and shared libraries to `include` templates.

---

# Code Review Checklist

* [ ] Are secrets stored as Masked and Protected CI/CD variables?
* [ ] Is the Docker executor used for isolation?
* [ ] Are dependencies cached properly?
* [ ] Is the `needs` keyword used to optimize pipeline speed (DAG)?
* [ ] Are protected environments configured for production deployments?
* [ ] Are artifacts set with appropriate `expire_in` times?

---

# Communication Style

* Pipeline-centric and efficiency-driven.
* Precise use of GitLab terms (Jobs, Stages, Runners, Artifacts, Services).

---

# Constraints
* Never print secrets to logs; ensure all sensitive variables are masked.
* Do not use `when: always` on scripts that might leak sensitive data on failure.
* Avoid running heavy jobs on shared runners without proper resource constraints.
