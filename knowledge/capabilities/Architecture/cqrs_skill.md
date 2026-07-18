# Skill: CQRS Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | CQRS Software Engineer |
| Version | 1.0.0 |
| Language | Architecture Patterns (Agnostic) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To separate the read side of a system from the write side by having separate models for each. This involves optimizing the command (write) model for validation and business rules, and the query (read) model for speed and shaping data specifically for UI requirements, eliminating the need for a single complex domain model that tries to serve both purposes.

---

# Primary Responsibilities

* Segregate command handlers (state mutation) from query handlers (data retrieval).
* Design optimized read models (often denormalized) tailored to specific UI views.
* Ensure synchronization between the write model and read models (often via events or async processes).
* Prevent "anemic" domain models on the write side.

---

# Language Versions

* N/A (Architectural Pattern). Introduced by Greg Young.
* *Evolution:* Often confused with Event Sourcing. Understand that CQRS does *not* require Event Sourcing, though they pair well together.

---

# Coding Standards

* **Separation:** Commands return nothing (void) or a simple success/failure. Queries return data (DTOs) and must not mutate state.
* **Naming Conventions:** `CreateOrderCommand`, `GetOrderByIdQuery`.
* **Handler Pattern:** One handler per Command/Query (e.g., `ICommandHandler<TCommand>`).

---

# Software Engineering Principles

* **Single Responsibility Principle:** A class/method should either change state or return state, not both.
* **Optimization:** Optimize reads and writes independently.

---

# Design Patterns

* **Command Handler:** Processes a command, executes business logic against the write model, and returns nothing.
* **Query Handler:** Executes a read against the read model/DB and returns a DTO.
* **Mediator Pattern:** A central mediator (e.g., MediatR) routes commands/queries to their respective handlers.
* **Materialized View:** The read model is essentially a materialized view of the write model's state.

---

# Architecture Knowledge

* **Write Side:** Relational database, highly normalized, enforces invariants, uses the Domain Model.
* **Read Side:** NoSQL (Document DB) or highly denormalized SQL tables, optimized for specific screen queries.
* **Synchronization:** Async sync (via events/queues) is standard; sync sync (updating both DBs in one transaction) is fragile and only for simple cases.

---

# Package Management

* **Separation:** Physical separation of `Commands`, `Queries`, `ReadModels`, and `Domain`.

---

# Framework Knowledge

* **MediatR (.NET):** The most famous implementation of the mediator pattern for CQRS.
* **Axon Framework (Java):** Supports CQRS natively.
* **Simpler implementations:** Custom routing using decorators or simple factory patterns.

---

# Database Skills

* **Write DB:** Strong consistency (ACID), optimized for transactions.
* **Read DB:** Eventual consistency, optimized for reads (e.g., MongoDB documents matching exactly what the frontend needs).

---

# API Development

* **Endpoints:** Map cleanly to Commands (POST/PUT/DELETE) and Queries (GET).

---

# Security

* **Command Authorization:** Validate permissions on the Command side before mutating state.
* **Query Filtering:** Ensure users can only query data they are authorized to see (often done in the Query Handler or Read DB).

---

# Error Handling

* **Command Failures:** Throw specific domain exceptions (e.g., `InsufficientStockException`).
* **Query Failures:** Throw "not found" exceptions if the read model doesn't have the data yet (due to eventual consistency).

---

# Performance

* **Read Scaling:** Read side can be scaled independently of the write side (e.g., multiple read replicas).
* **Complex Joins:** Move complex SQL joins from the write side to the read side (pre-calculated denormalized data).

---

# Testing

* **Write Side:** Unit test Commands against the domain model.
* **Read Side:** Unit test Queries against the read model structure.
* **Sync Mechanism:** Integration test the process that updates the read model when a command executes.

---

# Static Analysis

* **Boundary Enforcement:** Ensure queries do not accidentally access the write database or domain model directly.

---

# Documentation

* **Command/Query Catalog:** List all commands and queries, their payloads, and expected outcomes.
* **Read Model Mapping:** Document how write model events map to read model structures.

---

# Version Control

* **Structure:** `src/Commands/`, `src/Queries/`, `src/ReadModels/`.

---

# Build Tools

* **Standard build tools.** No specific requirements.

---

# CI/CD

* **Standard pipelines.**

---

# Legacy Code

* **Read Model Extraction:** Introduce CQRS by first creating a read database alongside the legacy monolith DB. Route all `SELECT` queries to the new read DB, sync data asynchronously. Leave writes in the legacy system initially.

---

# Code Review Checklist

* [ ] Do any queries modify state? (Strict violation).
* [ ] Do any commands return business data? (They should only return an ID or success status).
* [ ] Is the read model denormalized and optimized for the specific UI use case?
* [ ] Is eventual consistency handled gracefully in the UI (e.g., loading spinners, optimistic updates)?
* [ ] Are commands validated strictly before reaching the domain?

---

# Communication Style

* Precise distinction between "Intent" (Command) and "Information request" (Query).
* Focus on data flow divergence and eventual consistency.

---

# Constraints
* Do not implement CQRS for simple CRUD applications where the read and write models are identical (it adds unnecessary complexity).
* Do not query the write database directly from the UI/API layer.
