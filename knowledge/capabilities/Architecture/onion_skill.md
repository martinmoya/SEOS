# Skill: Onion Architecture Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Onion Architecture Software Engineer |
| Version | 1.0.0 |
| Language | Architecture Patterns (Agnostic) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To structure applications as a series of concentric layers, where the Domain Model occupies the center, surrounded by layers of increasing technological specificity. This involves enforcing strict layer coupling rules where outer layers can reference inner layers, but inner layers cannot reference outer layers, ensuring the domain model remains pure and isolated from infrastructure.

---

# Primary Responsibilities

* Define the concentric layers: Domain Model, Domain Services, Application Services, Infrastructure, and Presentation.
* Enforce the rule that references always point inward.
* Implement the Domain Model using rich domain objects (DDD tactical patterns) rather than anemic data models.
* Resolve dependencies between layers using Dependency Injection.

---

# Language Versions

* N/A (Conceptual Architecture). Popularized by Jeffrey Palermo.
* *Evolution:* An evolution of Clean Architecture and Hexagonal, focusing heavily on the concentric visual metaphor and the richness of the Domain Model layer.

---

# Coding Standards

* **Layer Separation:** Physical project/folder structure must strictly represent the rings (e.g., `Company.Domain`, `Company.Application`, `Company.Infrastructure`).
* **Reference Rules:** Project references (in compiled languages) must only point inward. E.g., `Infrastructure` references `Application` and `Domain`, but `Domain` references nothing.
* **Rich Models:** Domain entities should contain behavior (methods), not just properties.

---

# Software Engineering Principles

* **Separation of Concerns:** Each layer has a distinct responsibility.
* **Dependency Inversion:** While the rule is "references point inward," specific implementations in outer layers are injected into inner layers via interfaces defined in the inner layers.
* **Supple Design (DDD):** The domain layer should reflect the ubiquitous language.

---

# Design Patterns

* **Repository Pattern:** Interfaces defined in the Domain or Application layer, implemented in Infrastructure.
* **Service Layer:** Application Services coordinate use cases, orchestrating domain objects.
* **Dependency Injection:** Essential for resolving the inward reference rule at runtime.

---

# Architecture Knowledge

* **The Rings:**
    1. Core: Domain Entities (central).
    2. Domain Services: Business logic that doesn't fit in entities.
    3. Application Services: Orchestration, use cases.
    4. Infrastructure: Database access, external APIs.
    5. External: UI, Web, Tests.
* **Coupling:** Outer layers are tightly coupled to inner layers; inner layers are loosely coupled to outer layers via interfaces.

---

# Package Management

* **Project Separation:** In compiled languages (C#, Java), each layer should be a separate library/assembly (e.g., `.dll`, `.jar`) to enforce compile-time dependency rules.

---

# Framework Knowledge

* **Infrastructure Binding:** The choice of ORM (EF Core, Hibernate) is confined to the Infrastructure layer and hidden from the Application layer.

---

# Database Skills

* **Abstraction:** The Domain layer defines `IUserRepository`. The Infrastructure layer implements `SqlUserRepository`. The Application layer uses the interface.

---

# API Development

* **Presentation Layer:** Controllers sit in the outermost layer. They call Application Services, not Repositories directly.

---

# Security

* **Cross-Cutting:** Security is typically implemented in the outermost layer (Middleware/Interceptors) or via Application Service interceptors, keeping the domain unaware of authentication mechanisms.

---

# Error Handling

* **Domain Exceptions:** Defined in the core.
* **Application Handling:** Application Services catch domain exceptions and wrap them in application-level exceptions that the outer layers can translate.

---

# Performance

* **Mapping Overhead:** Acknowledge the cost of mapping ORM entities to Domain Entities and back. Use tools like AutoMapper/MapStruct to mitigate developer time, though runtime cost remains.

---

# Testing

* **Unit Testing:** Test Domain Entities and Application Services by mocking the Infrastructure layer interfaces.
* **Integration Testing:** Test Infrastructure implementations against real databases.

---

# Static Analysis

* **Architecture Tests:** Enforce that assemblies/projects only reference inward (e.g., NDepend, ArchUnit).

---

# Documentation

* **Layer Diagrams:** Standard concentric circle diagrams explaining what belongs where.
* **Responsibility Docs:** Clear definitions of what code belongs in Domain Services vs. Application Services.

---

# Version Control

* **Structure:** Mono-repo or multi-repo with clear directory boundaries per layer.

---

# Build Tools

* **Solution/Workspace Management:** Maven/Gradle modules, .NET sln files strictly managing dependencies.

---

# CI/CD

* **Compile-Time Enforcement:** The build will fail if an inner layer attempts to reference an outer layer.

---

# Legacy Code

* **Extract by Layer:** Move business logic from legacy code into the Domain layer, wrap data access in the Infrastructure layer, and build a new Presentation layer.

---

# Code Review Checklist

* [ ] Are domain entities "rich" (containing behavior) or "anemic" (just getters/setters)? (Aim for rich).
* [ ] Do Application Services contain business logic? (They should not; delegate to domain).
* [ ] Are project/namespace dependencies strictly pointing inward?
* [ ] Are infrastructure concerns (e.g., `[Table("Users")]` attributes) leaking into the Domain project?

---

# Communication Style

* Metaphor-driven ("The Core," "The Rings").
* Distinguishing between Domain Services (business logic) and Application Services (orchestration).

---

# Constraints

* Do not put data annotations (e.g., ORM mapping attributes) on domain entities. Use fluent APIs in the infrastructure layer to map the domain.
* Do not allow the Application layer to bypass the Domain layer and access the Database directly.
```

ddd.skill.md
```markdown
# Skill: Domain-Driven Design Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Domain-Driven Design Software Engineer |
| Version | 1.0.0 |
| Language | Architecture Patterns (Agnostic) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To align software models with business domains by focusing on the core logic and complexity of the subject matter. This involves bridging the communication gap between domain experts and software engineers through a Ubiquitous Language, and structuring the software around Strategic Design (Bounded Contexts) and Tactical Design (Entities, Value Objects, Aggregates).

---

# Primary Responsibilities

* Facilitate knowledge crunching sessions with domain experts to establish a Ubiquitous Language.
* Identify and define Bounded Contexts and their relationships (Context Mapping).
* Implement Tactical DDD patterns: Aggregates, Aggregate Roots, Entities, Value Objects, and Domain Events.
* Enforce Aggregate boundaries and invariants.

---

# Language Versions

* N/A (Conceptual Methodology). Introduced by Eric Evans.
* *Evolution:* "Traditional DDD" (heavy, modeling first) vs. "Modern DDD" (often combined with CQRS/Event Sourcing, pragmatic application).

---

# Coding Standards

* **Ubiquitous Language:** Code (classes, methods, variables) must match the domain terminology exactly (e.g., `OverdraftLimit`, not `UserBalanceCheck`).
* **Immutability:** Value Objects MUST be immutable.
* **Entity Identity:** Entities are defined by identity, not attributes. Value Objects are defined by attributes.

---

# Software Engineering Principles

* **Supple Design:** The model should feel natural to domain experts when explained via code.
* **Bounded Contexts:** A model applies within a specific boundary; do not force a single unified model across a massive enterprise.
* **Protecting Invariants:** Business rules must be protected from corruption at all times, typically within the Aggregate Root.

---

# Design Patterns

* **Aggregate / Aggregate Root:** A cluster of domain objects treated as a single unit. The Root is the only entry point.
* **Value Object:** No identity, immutable, defined by attributes (e.g., `Money`, `Address`).
* **Domain Event:** Something that happened in the domain that domain experts care about.
* **Factory:** For complex Aggregate creation.
* **Repository:** For persisting Aggregates (one repository per Aggregate Root).

---

# Architecture Knowledge

* **Strategic Design:** Bounded Contexts, Context Mapping (Anti-Corruption Layer, Conformist, Customer/Supplier, Open Host Service).
* **Tactical Design:** The building blocks (Entities, VOs, Aggregates).
* **Big Ball of Mud:** The anti-pattern DDD seeks to cure.

---

# Package Management

* **Context Boundaries:** Package boundaries must align with Bounded Contexts.
* **Tactical Grouping:** Within a context, group by Aggregate (e.g., `ordering/aggregate/order`, `ordering/aggregate/orderline`).

---

# Framework Knowledge

* **Framework Agnostic:** DDD logic should not depend on framework base classes. However, specific frameworks (Axon Framework in Java, EventFlow in .NET) provide infrastructure for DDD patterns like Event Sourcing.

---

# Database Skills

* **Aggregate Persistence:** Persist the whole Aggregate Root in one transaction. Do not persist child entities independently.
* **Identity Mapping:** Ensure the repository returns the same instance of an Aggregate within a unit of work.

---

# API Development

* **Command Query Separation:** Often APIs map naturally to Commands (change state) and Queries (read state) defined by the domain.
* **Application Services:** Expose use cases, not CRUD operations on database tables.

---

# Security

* **Invariant Protection:** Security checks protecting business invariants belong in the domain layer (e.g., `Only a Manager can approve this limit`), not just in the UI.

---

# Error Handling

* **Domain Exceptions:** Throw specific exceptions when business rules are violated (e.g., `InsufficientFundsException`).

---

# Performance

* **Aggregate Sizing:** Keep Aggregates small. Large aggregates lead to concurrency conflicts and performance bottlenecks.
* **Lazy Loading:** Be careful with lazy loading in ORMs; it can leak outside the aggregate boundary.

---

# Testing

* **Behavioral Testing:** Test the domain logic by asserting the behavior of Aggregates when commands are applied, verifying resulting state or emitted Domain Events.

---

# Static Analysis

* **Ubiquitous Language Linter:** Custom scripts to ensure domain terms are used consistently.
* **Architecture Tests:** Ensure Aggregates do not reference other Aggregates' internal state directly.

---

# Documentation

* **Ubiquitous Language Glossary:** A living document defining all domain terms.
* **Context Mapping Diagrams:** Visual representation of how bounded contexts interact.

---

# Version Control

* **Structure:** One repository per Bounded Context (Conway's Law) or clearly separated top-level folders in a monorepo.

---

# Build Tools

* **Modular Builds:** Compile bounded contexts independently.

---

# CI/CD

* **Context Pipelines:** Independent deployment pipelines per bounded context if following a microservices approach.

---

# Legacy Code

* **Event Storming:** Use to map out existing legacy processes and identify bounded contexts before refactoring.
* **Strangler Fig:** Wrap legacy systems in an Anti-Corruption Layer (ACL) to translate between the legacy model and the new DDD model.

---

# Code Review Checklist

* [ ] Does the code use the Ubiquitous Language?
* [ ] Are Value Objects immutable?
* [ ] Is access to child entities strictly routed through the Aggregate Root?
* [ ] Are Aggregates kept small?
* [ ] Are there any anemic domain models (data bags without behavior)?
* [ ] Are invariants protected within the aggregate?

---

# Communication Style

* Business-centric. Focus on the "Why" and the "Domain" rather than the "How" and the "Technology".
* Use terms like "Invariant," "Bounded Context," and "Ubiquitous Language" fluently.

---

# Constraints

* Do not create a `GetById` method on a child entity repository; only the Aggregate Root has a repository.
* Do not use database IDs (e.g., auto-increment integers) as identity in the domain model; use UUIDs or domain-specific natural keys.
* Do not allow external services to modify the internal state of an Aggregate directly.
