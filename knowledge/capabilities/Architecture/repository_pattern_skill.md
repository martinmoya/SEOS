# Skill: Repository Pattern Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Repository Pattern Software Engineer |
| Version | 1.0.0 |
| Language | Architecture Patterns (Agnostic) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To mediate between the domain and data mapping layers, acting like an in-memory domain object collection. This involves encapsulating the logic required to access data sources, providing a domain-oriented view of the data, and completely hiding the details of database queries, ORM specifics, and data mapping from the business logic.

---

# Primary Responsibilities

* Define repository interfaces (contracts) within the domain or application layer.
* Implement concrete repositories in the infrastructure layer using ORMs or raw SQL.
* Ensure the domain layer remains completely ignorant of the database technology (SQL, NoSQL, In-Memory).
* Expose collection-like semantics (e.g., `Add()`, `Remove()`, `FindById()`) rather than database semantics (e.g., `ExecuteSql()`).

---

# Language Versions

* N/A (Design Pattern). Introduced by Martin Fowler / Eric Evans (DDD).
* *Evolution:* Moving from generic repositories (`Repository<T>`) to specific repositories (`IOrderRepository`) to better enforce aggregate boundaries and query specifics.

---

# Coding Standards

* **Interface Location:** The interface MUST be defined in the domain/application layer.
* **Implementation Location:** The implementation MUST be in the infrastructure layer.
* **Collection Semantics:** Methods should reflect domain language (`GetActiveUsers()`) rather than SQL concepts (`SelectWhereActive=1()`).
* **No ORM Leakage:** Return domain entities, not ORM framework-specific base classes or lazy-loading proxies.

---

# Software Engineering Principles

* **Dependency Inversion:** High-level domain modules depend on repository interfaces, not low-level database implementations.
* **Separation of Concerns:** Business logic does not know how data is persisted.
* **Testability:** Business logic can be tested by mocking the repository interface.

---

# Design Patterns

* **Repository:** The defining pattern.
* **Factory:** Sometimes used with repositories to create complex domain objects upon retrieval.
* **Specification Pattern:** Often combined with repositories to encapsulate complex query logic in a reusable composable way (e.g., `ActiveUserSpecification`).

---

# Architecture Knowledge

* **Aggregate Boundary:** In DDD, you typically have one Repository per Aggregate Root. You do not create repositories for child entities.

---

# Package Management

* **Interface Segregation:** Keep repository interfaces in the `Domain` or `Application` package. Keep implementations in `Infrastructure.Persistence`.

---

# Framework Knowledge

* **ORM Abstraction:** Must be familiar with Entity Framework, Hibernate, SQLAlchemy, etc., strictly as implementation details hidden behind the repository interface.

---

# Database Skills

* **Query Optimization:** The repository implementation is where query optimization (indexing, joins) happens, but this logic is hidden from the caller.
* **Connection Management:** Repositories handle opening/closing connections (often delegated to a Unit of Work).

---

# API Development

* **Indirection:** The API layer calls Application Services, which call Repositories. The API layer never touches repositories directly.

---

# Security

* **Row-Level Security:** If required, the repository implementation is the correct place to apply row-level filtering (e.g., "only return orders belonging to this tenant ID"), though passing a `TenantContext` to the repository method is preferred over hardcoding.

---

# Error Handling

* **Exception Translation:** The repository implementation catches database-specific exceptions (e.g., `SqlException` for unique constraint violations) and translates them into domain exceptions (e.g., `DuplicateUserException`).

---

# Performance

* **Eager vs. Lazy Loading:** The repository must handle loading strategies (e.g., eagerly loading child collections if the domain requires them to enforce invariants) without leaking ORM lazy-loading proxies to the domain layer.

---

# Testing

* **Mocking:** In unit tests, mock the repository interface to return fake domain entities.
* **Integration Testing:** Test the concrete repository implementation against a real database (e.g., using Testcontainers) to verify SQL/ORM mapping.

---

# Static Analysis

* **Dependency Checks:** Ensure the Infrastructure layer references the Domain layer, never the reverse.

---

# Documentation

* **Interface Docs:** Document the domain intent of the repository methods.
* **Implementation Notes:** Document specific ORM configurations or SQL quirks used in the implementation.

---

# Version Control

* **Structure:** Clear separation of interface and implementation files.

---

# Build Tools

* **Standard build tools.**

---

# CI/CD

* **Standard pipelines.**

---

# Legacy Code

* **Anti-Corruption Layer:** If legacy code uses raw SQL everywhere, introduce repository interfaces and implement them using the existing SQL, then gradually refactor the SQL.

---

# Code Review Checklist

* [ ] Is the repository interface defined in the domain/application layer?
* [ ] Does the repository return domain entities, not ORM entities?
* [ ] Is there a repository for a child entity? (Violation of Aggregate Root pattern).
* [ ] Are database-specific exceptions being caught and translated to domain exceptions?
* [ ] Is the repository hiding ORM-specific details (like `Include()` or `Join` syntax) from the caller?

---

# Communication Style

* Collection-oriented.
* Focused on data access encapsulation and domain purity.

---

# Constraints
* Do not return `IQueryable` (in C#) or query builders from repository methods. This leaks data access logic to the business layer. Return `IEnumerable` or `List` instead.
* Do not expose CRUD methods (Get/Update/Delete) if they violate business invariants; use specific domain methods (e.g., `CancelOrder()` instead of `UpdateOrderStatus()`).
