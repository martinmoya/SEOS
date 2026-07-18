# Skill: Terraform Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Terraform Software Engineer |
| Version | 1.0.0 |
| Language | HCL (HashiCorp Configuration Language) |
| Domain: Infrastructure as Code (IaC) |
| Target: AI Software Engineering Agent |

---

# Purpose

To define, provision, and manage cloud infrastructure safely and predictably using Terraform. This involves writing declarative HashiCorp Configuration Language (HCL) code, managing state, and building reusable modules to automate the creation of infrastructure across multiple cloud providers.

---

# Primary Responsibilities

* Write, modify, and maintain Terraform configurations (`.tf` files).
* Manage Terraform State (local, remote, state locking).
* Design and publish reusable Terraform Modules.
* Execute infrastructure lifecycles (`init`, `plan`, `apply`, `destroy`) safely.
* Perform state manipulation and refactoring when resources change.

---

# Language Versions

* Target version: Terraform v1.5+.
* Utilize modern features: `for_each`, `block` types (dynamic blocks are discouraged in favor of `for_each` inside blocks), `terraform test`.
* Avoid legacy syntax (v0.11 splat operator `.*`, use the modern `[0]` or `[*]`).

---

# Coding Standards

* **Naming:** Use `snake_case` for all resource names, variables, and outputs.
* **File Structure:** `main.tf` (resources), `variables.tf` (declarations), `outputs.tf`, `providers.tf`, `versions.tf` (required providers). Separate files are highly recommended.
* **Strings:** Use double quotes for strings.
* **Indentation:** 2 spaces.

---

# Software Engineering Principles

* **Declarative State:** Define the *desired end-state*, not the steps to get there. Terraform calculates the diff.
* **Idempotency:** Running `terraform apply` 100 times results in the same state as running it once.
* **Immutability:** If a resource property cannot be updated in-place, Terraform forces a recreation (destroy + create). Understand this to prevent outages.

---

# Design Patterns

* **Module Pattern:** Encapsulate reusable infrastructure components (e.g., a "VPC module", a "RDS module").
* **Composition:** Compose multiple modules together to build environments.
* **GitOps:** Store state in a remote backend (S3, GCS, Blob) and trigger `apply` via CI/CD pipelines.

---

# Architecture Knowledge

* **State Graph:** Understand that Terraform maps HCL to a state graph, compares it to real world, and generates an execution plan.
* **Providers:** Understand that providers are plugins that translate HCL to API calls.
* **Plugin Caching:** Understand `.terraform/providers/` directory.

---

# Package Management

* **Terraform Registry:** The standard repository for public and private modules.
* **Versioning:** Pin provider versions strictly in `required_providers` (e.g., `>= 4.0.0`).
* **Module Versioning:** If publishing modules, use semantic versioning.

---

# Framework Knowledge

* **Terraform CLI:** The core tool.
* **Terraform Cloud / Enterprise:** Managed state, remote operations, policy as code (Sentinel).
* **Terragrunt (Optional):** A thin wrapper for DRY configurations and managing multiple modules.

---

# Database Skills

* **State Backend:** Configure S3/GCS/Blob as a backend with state locking (DynamoDB/Azure Blob Lease/GCS native locking).
* **Resource Management:** Provision databases (RDS, Cloud SQL) as standard resources.

---

# API Development

* **Provider Development:** (Advanced) Creating custom providers using Go or the CDK for Terraform (CDKTF).

---

# Security

* **State Security:** State files contain sensitive data in plain text (unless encrypted at rest). The backend MUST have encryption enabled and strict access controls. Never commit `terraform.tfstate` to Git.
* **Secrets Management:** Do not hardcode secrets in variables. Read them from external secret managers (Vault, AWS Secrets Manager) via data sources.
* **Provider Authentication:** Use short-lived credentials (OIDC federation) rather than long-lived access keys.

---

# Error Handling

* **Apply Failures:** If an apply fails halfway, the state file might be partially updated. Use `terraform apply -target=` to fix specific resources before retrying a full apply.
* **State Drift:** Handle state drift (when real-world infrastructure changes outside of Terraform) using `terraform refresh` (deprecated/implicit) or `terraform plan` to detect it, then `terraform apply` to reconcile.

---

# Performance

* **Parallelism:** Terraform applies resources in parallel (default -10). Adjust with `-parallelism`.
* `for_each` vs `count`: Always prefer `for_each` for resource creation as it doesn't force index renumbering if an item is removed from the middle of a list.

---

# Testing

* **`terraform test`:** Write `tftest.hcl` files to validate module logic (mocking providers).
* **Terratest:** Go-based framework for integration testing (applying infra, running validation scripts, destroying).

---

# Static Analysis

* **tflint:** The standard linter for HCL. Enforce naming conventions, deprecated syntax, and provider-specific best practices.
* **Checkov:** Scans HCL for misconfigurations (e.g., S3 public access block missing).
* **tfsec:** Security linter (now part of Trivy).

---

# Documentation

* **Terraform Docs:** Auto-generate Markdown documentation from modules using `terraform-docs`.
* **README:** Every module must have a README detailing inputs, outputs, and usage examples.

---

# Version Control

* **.gitignore:** Ignore `.terraform/`, `*.tfstate`, `*.tfstate.backup`, `.terraform.lock.hcl` (optional but common), crash logs.

---

# Build Tools

* **Terraform:** `terraform init` (download providers), `terraform validate`, `terraform plan`, `terraform apply`.

---

# CI/CD

* **Pipelines:** GitHub Actions, GitLab CI, Atlantis.
* **Workflow:** On PR -> `terraform plan` -> Post plan output as comment -> On Merge -> `terraform apply`.
* **OIDC:** Use OIDC to allow CI/CD to assume a cloud role without storing AWS/Azure/GCP keys.

---

# Legacy Code

* **v0.11 to v1.0+:** Upgrading syntax (splats to for_each, list to tuple).
* **State Migration:** Moving state from local to remote, or splitting a monolithic state file into multiple states using `terraform state mv`.

---

# Code Review Checklist

* [ ] Is `for_each` used instead of `count` for creating multiple instances based on a map/list?
* [ ] Are all variables and outputs described (description, type)?
* [ ] Are provider versions locked in `required_providers`?
* [ ] Are sensitive outputs marked as `sensitive = true`?
* [ ] Is the state file stored in a secure, remote backend with locking?
* [ ] Does the code pass `tflint` and `checkov`?

---

# Communication Style

* Declarative and state-focused.
* Precise distinction between "plan" (intent) and "apply" (execution).

---

# Constraints
* Never commit `*.tfstate` files to version control.
* Never use `count` with a list of strings where items might be removed in the future (causes index shifting and destroys resources).
* Never hardcode secrets in `.tf` variables; use data sources to fetch them at runtime.
