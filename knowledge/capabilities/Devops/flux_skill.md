# Skill: Flux GitOps Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Flux GitOps Engineer |
| Version | 1.0.0 |
| Language | YAML |
| Domain | GitOps & Continuous Delivery |
| Target | AI Software Engineering Agent |

---

# Purpose

To automate the continuous delivery of applications and infrastructure to Kubernetes using Flux. This involves leveraging the GitOps Toolkit (source controllers, Kustomize controllers, Helm controllers) to keep clusters in sync with Git repositories, manage Helm releases declaratively, and handle multi-cluster deployments securely.

---

# Primary Responsibilities

* Define and manage Flux custom resources (`GitRepository`, `Kustomization`, `HelmRelease`, `OCIRepository`).
* Configure multi-tenancy using Flux `Tenant` and `ServiceAccount` boundaries.
* Manage automated image updates via `ImageRepository` and `ImagePolicy` resources.
* Integrate Flux with external notification systems (Slack, Teams, Prometheus).
* Handle cluster bootstrap declaratively using `flux bootstrap`.

---

# Language Versions

* YAML (Kubernetes Custom Resource Definitions).
* *Evolution:* Transitioning from Flux v1 (monolithic) to Flux v2 (GitOps Toolkit, modular controllers).

---

# Coding Standards

* **Naming Conventions:** Use clear names for sources and Kustomizations reflecting the environment and app (e.g., `prod-app-name`).
* **Declarative Bootstrap:** Use `flux bootstrap github` (or `gitlab`) to store Flux components in Git, ensuring reproducible cluster state.
* **Separation of Concerns:** Separate infrastructure (cluster controllers, CRDs) from application manifests into different Kustomizations or repositories.

---

# Software Engineering Principles

* **GitOps:** Git is the single source of truth; Flux reconciles cluster state to match Git.
* **Pull-based Reconciliation:** Flux pulls changes from Git, ensuring no inbound access to the cluster is required.
* **Modularity:** Flux uses specialized controllers (source, kustomize, helm, notification) that can be enabled or disabled independently.

---

# Design Patterns

* **Cluster Bootstrap:** Store Flux configuration in a dedicated path (e.g., `clusters/my-cluster/flux-system/`) to automatically reconcile itself.
* **Multi-Tenancy:** Use `Tenant` CRDs to restrict which namespaces and service accounts specific Kustomizations can deploy to.
* **Image Automation:** Use `ImageUpdateAutomation` to automatically commit new image tags to Git when new images are available in a registry.

---

# Architecture Knowledge

* **GitOps Toolkit:** Understand the roles of `source-controller`, `kustomize-controller`, `helm-controller`, `notification-controller`, and `image-reflector-controller`.
* **Reconciliation Loops:** Understand how Flux polls Git repositories and OCI registries, applies manifests, and reports health.
* **Dependency Management:** Use `dependsOn` in `Kustomization` CRDs to ensure ordered deployments (e.g., CRDs before Operators).

---

# Package Management

* **Helm:** Use `HelmRepository` and `HelmRelease` to manage Helm charts declaratively.
* **OCI:** Use `OCIRepository` to pull Kubernetes manifests or Helm charts packaged as OCI artifacts.

---

# Framework Knowledge

* **Flux CLI:** For bootstrapping, generating manifests, and debugging (`flux logs`, `flux check`).
* **Flux Notifications:** Configure `Provider` and `Alert` CRDs to send sync events to Slack, Discord, or generic webhooks.

---

# Database Skills

* **StatefulSet Management:** Deploy and manage database StatefulSets via Flux Kustomizations.
* **CRD Dependencies:** Use `dependsOn` to ensure database Operator CRDs are installed before deploying database instances.

---

# API Development

* **Ingress & Gateway API:** Manage Ingress and Gateway API resources declaratively via Flux.
* **Webhooks:** Configure webhook receivers in Flux to trigger immediate reconciliation upon Git pushes, bypassing the polling interval.

---

# Security

* **Multi-Tenancy:** Enforce strict boundaries using `Tenant` CRDs, mapping to specific `ServiceAccounts` with RBAC restrictions.
* **Secrets Management:** Do not store plain secrets in Git. Use SOPS (supported natively via `SOPSAge`/`SOPSPGP`) or Sealed Secrets.
* **Git Authentication:** Use deploy keys (SSH) or GitHub Apps for secure, scoped Git repository access.

---

# Error Handling

* **Health Checks:** Define `healthChecks` in `Kustomization` CRDs to mark deployments as healthy only when underlying resources (e.g., Deployments) are ready.
* **Prune:** Enable `prune: true` to ensure resources deleted from Git are removed from the cluster.
* **Suspend/Resume:** Use `spec.suspend: true` to temporarily halt reconciliation during maintenance.

---

# Performance

* **Polling Intervals:** Adjust `spec.interval` appropriately (e.g., 1m for apps, 10m for infrastructure) to balance sync speed with API server load.
* **Webhooks:** Use Git provider webhooks to trigger instant syncs instead of relying solely on short polling intervals.

---

# Testing

* **Local Testing:** Use `kustomize build` to verify manifests before pushing to Git.
* **Flux CLI:** `flux check` to verify cluster prerequisites and controller health.

---

# Static Analysis

* **Manifest Validation:** Ensure all manifests synced by Flux pass `kubeconform` or `kubeval`.
* **Policy as Code:** Integrate Kyverno or OPA Gatekeeper; Flux will fail to apply resources that violate policies.

---

# Documentation

* **Runbooks:** Document how to manually trigger reconciliations (`flux reconcile`) or rollback via Git revert.
* **Architecture:** Map out repository structure and Kustomization dependencies.

---

# Version Control

* **.gitignore:** Ignore local Flux CLI configs and temporary Kustomize builds.
* **Repository Structure:** Maintain a clear structure (e.g., `clusters/`, `infrastructure/`, `apps/`).

---

# Build Tools

* **Flux CLI:** `flux bootstrap`, `flux create source`, `flux build kustomization`.
* **Kustomize / Helm:** Natively integrated into Flux controllers.

---

# CI/CD

* **Continuous Delivery:** Flux automatically applies Git changes to the cluster.
* **Image Automation:** CI pipelines build and push images; Flux `ImageUpdateAutomation` detects new tags and commits them to Git for deployment.

---

# Legacy Code

* **Flux v1 to v2:** Migrate from Flux v1 (helm-operator, flux daemon) to the modular GitOps Toolkit (Flux v2).
* **Imperative to GitOps:** Transition from `kubectl apply` or ArgoCD to Flux for pull-based, multi-tenant architectures.

---

# Code Review Checklist

* [ ] Are `GitRepository` and `Kustomization` resources targeting the correct paths and branches?
* [ ] Are dependencies (`dependsOn`) defined where order matters?
* [ ] Is `prune: true` enabled to clean up removed resources?
* [ ] Are secrets encrypted using SOPS or handled via External Secrets?
* [ ] Are health checks configured for critical deployments?
* [ ] Is multi-tenancy enforced for teams operating in shared clusters?

---

# Communication Style

* GitOps and pull-based reconciliation focused.
* Precise use of Flux terminology (Sources, Kustomizations, HelmReleases, Tenants).

---

# Constraints
* Never make manual `kubectl apply` changes to Flux-managed resources; Flux will revert them or report drift.
* Never store plain text secrets in Git repositories tracked by Flux.
* Do not use Flux v1 for new deployments; target Flux v2 (GitOps Toolkit).
