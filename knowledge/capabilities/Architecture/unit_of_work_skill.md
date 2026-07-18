# Skill: Unit of Work Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Unit of Work Software Engineer |
| Version | 1.0.0 |
| Language | Architecture Patterns (Agnostic) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To maintain a list of objects affected by a business transaction and coordinates the writing out of changes and the resolution of concurrency problems. This involves managing a database transaction, tracking changes made to domain objects loaded via repositories, and committing all those changes to the database as a single atomic operation when the work is complete.

---

# Primary Responsibilities

* Define a Unit of Work interface/abstraction.
* Ensure all repositories used in a transaction share the same database context/session.
* Commit or rollback the transaction atomically.
* Manage the lifecycle of the database connection.

---

# Language Versions

* N/A (Design Pattern). Introduced by Martin Fowler.
* *Evolution:* In modern ORMs (Entity Framework, Hibernate), the Unit of Work is often implicit (the `DbContext` or `Session` *is* the Unit of Work), but understanding the explicit pattern is crucial for clean architecture and testing.

---

# Coding Standards

* **Explicit Boundaries:** Define a clear `Begin()`, `Commit()`, and `Rollback()` mechanism (even if wrapping an implicit ORM context).
* **Scope:** A Unit of Work should typically correspond to a single Application Service use case (one HTTP request = one Unit of Work).
* **Sharing:** Repositories must receive the same connection/session instance to participate in the same transaction.

---

# Software Engineering Principles

* **Atomicity:** All changes succeed, or none do.
* **Consistency:** The system moves from one valid state to another.
* **Dependency Management:** Managing the shared state (the context) and injecting it into repositories.

---

# Design Patterns

* **Unit of Work:** The defining pattern.
* **Repository Pattern:** Almost always used together. The UoW acts as the transaction manager for the repositories.

---

# Architecture Knowledge

* **Transaction Boundaries:** Understanding where a transaction starts and ends in the application flow (typically at the Application Service layer).
* **Identity Map:** The Unit of Work typically implements an Identity Map to ensure you don't load the same database row twice into memory as two different objects.

---

# Package Management

* **Interface Location:** The `IUnitOfWork` interface often lives in the Domain/Application layer (to allow mocking), while the implementation lives in Infrastructure.

---

# Framework Knowledge

* **Entity Framework Core:** `DbContext` implements UoW implicitly. `SaveChanges()` is the `Commit()`.
* **Hibernate/NHibernate:** `ISession` implements UoW. `Transaction.Commit()`.
* **Spring Boot:** `@Transactional` annotation handles UoW boundaries via AOP.

---

# Database Skills

* **Transaction Isolation Levels:** Understand Read Committed, Repeatable Read, Serializable, and choose the appropriate level for the use case to prevent deadlocks/dirty reads.
* **Connection Pooling:** The UoW manages the checkout and return of a connection from the pool.

---

# API Development

* **Middleware Integration:** In web apps, the Unit of Work is often managed via middleware (e.g., open UoW on request start, commit on request end, rollback on exception).

---

# Security

* **Connection Security:** Ensuring the UoW uses authenticated connections.

---

# Error Handling

* **Rollback:** If any exception occurs during the use case execution, the UoW MUST be rolled back.
* **Concurrency:** Handling `OptimisticConcurrencyException` during commit (e.g., when two users edit the same row simultaneously).

---

# Performance

* **Short-Lived:** UoWs should be short-lived. Do not keep a UoW open across multiple HTTP requests or long-running background processes.
* **Batching:** Modern UoW implementations (EF Core) batch multiple INSERT/UPDATE statements into a single round-trip to the database.

---

# Testing

* **Mocking:** Mock the `IUnitOfWork` interface to verify that `Commit()` was called exactly once for a use case, or mock it to throw an exception to test rollback logic.
* **Integration Testing:** Test the actual transaction behavior against a real database.

---

# Static Analysis

* **Lifecycle Checks:** Ensure UoWs are disposed properly to prevent connection leaks.

---

# Documentation

* **Transaction Boundaries:** Document which use cases require transactions vs. read-only contexts.

---

# Version Control

* **Standard version control.**

---

# Build Tools

* **Standard build tools.**

---

# CI/CD

* **Standard pipelines.**

---

# Legacy Code

* **Transaction Script:** If legacy code uses raw `BEGIN TRAN` / `COMMIT` SQL, wrap it in a UoW interface to standardize transaction management.

---

# Code Review Checklist

* [ ] Is the Unit of Work scoped correctly (e.g., per HTTP request)?
* [ ] Are all repositories involved in a transaction sharing the same UoW/Context?
* [ ] Is `Commit()` called explicitly or via middleware? (Avoid relying on implicit auto-commits in business logic).
* [ ] Is `Rollback` handled correctly in exception paths?
* [ ] Are long-running transactions avoided?

---

# Communication Style

* Transaction and state-focused.
* Emphasizing data integrity and consistency boundaries.

---

# Constraints
* Do not share a Unit of Work across multiple threads without extreme caution (most ORM contexts are not thread-safe).
* Do not commit the Unit of Work multiple times for a single logical business transaction.
