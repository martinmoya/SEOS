# Skill: Modular Monolith Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Modular Monolith Software Engineer |
| Version | 1.0.0 |
| Language | Architecture Patterns (Agnostic) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To develop a single deployable application that is strictly structured into loosely coupled, highly cohesive modules. This involves reaping the benefits of clean architecture and domain-driven design (clear boundaries, independent teams) without incurring the distributed system complexity (network latency, consensus, deployment overhead) of microservices, while preserving the option to extract modules into microservices later if required.

---

# Primary Responsibilities

* Define clear module boundaries based on business capabilities.
* Enforce strict rules preventing modules from accessing other modules' internal data directly.
* Implement a public API (set of interfaces/classes) for each module.
* Manage shared kernels (common logic) carefully to prevent tight coupling.

---

# Language Versions

* N/A (Architectural Style).
* *Evolution:* A pragmatic reaction against premature microservice adoption. Understanding that most "microservices" start as distributed monoliths anyway.

---

# Coding Standards

* **Module Structure:** Each module should mirror a clean architecture (e.g., `modules/billing/src/domain`, `modules/billing/src/api`).
* **Public Surface:** Only specific classes/interfaces should be exported/public. Everything else should be `internal` or `private` to the module.
* **No Cross-Module DB Queries:** Module A must never execute a SQL `JOIN` with Module B's tables.

---

# Software Engineering Principles

* **High Cohesion:** Group related business logic and data together.
* **Loose Coupling:** Modules communicate via well-defined interfaces, not via direct database access or shared data structures (except primitives/dtos).
* **Encapsulation:** The internal implementation of a module is hidden from other modules.

---

# Design Patterns

* **Public API / Facade:** Exposing a specific set of Use Cases or Application Services as the module's entry point.
* **In-Process Adapter:** When Module A calls Module B, it calls an interface defined in B. B implements it.
* **Shared Kernel:** A carefully managed, small set of shared code (e.g., authentication primitives) that all modules depend on, treated as a stable external dependency.

---

# Architecture Knowledge

* **Monolithic Deployment:** Single unit of deployment (one JAR, one Docker image, one process).
* **Modular Boundaries:** Logical separation enforced at compile time (Java modules, .NET InternalsVisibleTo, Go internal packages).
* **Extraction Path:** The architecture must allow a module to be extracted into a microservice by changing the in-process adapter to an HTTP/gRPC adapter.

---

# Package Management

* **Module Independence:** Each module should ideally manage its own internal dependencies, or rely on a central dependency management file that treats modules as first-class citizens.

---

# Framework Knowledge

* **Modularity Support:** Utilize language/framework features that enforce module boundaries (e.g., Java 9+ Module System `module-info.java`, .NET `InternalsVisibleTo`, NestJS Modules).

---

# Database Skills

* **Schema Separation:** Each module should own its database schema (e.g., `billing.orders`, `inventory.products`). Avoid a single monolithic schema.
* **Cross-Module Queries:** Prohibit `JOIN`s across schemas. If Module A needs data from Module B, it must call Module B's public API (in-process) and assemble the data in memory.

---

# API Development

* **Internal APIs:** Modules expose application services (in-process function calls) rather than REST APIs.
* **External APIs:** A single API Gateway/Facade sits at the edge of the monolith to handle HTTP requests and route them to the appropriate module.

---

# Security

* **Module-Level Authorization:** Ensure internal APIs respect authorization rules (e.g., Module A shouldn't be able to invoke a "DeleteUser" use case in Module B just because they are in the same process).

---

# Error Handling

* **Simplified:** No need for distributed tracing (Correlation IDs) or Sagas. Standard in-process exception handling and local database transactions (ACID) are sufficient.

---

# Performance

* **In-Process Speed:** Communication between modules is extremely fast (function calls) compared to network calls.
* **Transaction Management:** Can use standard ACID transactions across a module's data, but avoid distributed transactions across modules.

---

# Testing

* **Module Isolation:** Test modules in isolation by mocking the public APIs of other modules.
* **Integration Testing:** Easy to spin up the whole monolith and run integration tests against a single database instance.

---

# Static Analysis

* **Dependency Graphs:** Automated checks to ensure Module A does not depend on Module B's internal packages.
* **ArchUnit / NDepend:** Essential tools for enforcing architectural rules.

---

# Documentation

* **Module Dependency Diagram:** Clear mapping of which modules depend on which.
* **Public API Docs:** Each module must document its public interfaces.

---

# Version Control

* **Mono-repo:** Standard approach. Allows refactoring tools to update multiple modules simultaneously.

---

# Build Tools

* **Monorepo Tools:** Nx, Lerna (JS/TS), Gradle (Java/Kotlin), .NET Solution.

---

# CI/CD

* **Simplified Pipeline:** One pipeline to build, test, and deploy the whole application.
* **Incremental Builds:** Build only the modules that changed (crucial for large modular monoliths).

---

# Legacy Code

* **Strangler Fig within Monolith:** Introduce a new module next to the legacy code, route traffic to the new module, and delete the legacy code.

---

# Code Review Checklist

* [ ] Are there any cross-module database queries (e.g., joining tables from different modules)?
* [ ] Is the module's internal implementation properly hidden (e.g., using `internal` access modifiers)?
* [ ] Is the Shared Kernel kept to an absolute minimum?
* [ ] Does the module have a clear, documented public API?
* [ ] Could this module be extracted into a microservice without rewriting its core logic?

---

# Communication Style

* Pragmatic and anti-hype.
* Focusing on team autonomy and code structure rather than deployment topology.

---

# Constraints
* Do not use distributed communication patterns (message brokers, REST) for inter-module communication within the monolith.
* Do not create a "Shared Library" module that becomes a dumping ground for random utilities (this creates tight coupling).
* Do not allow circular dependencies between modules.
