# Skill: MediatR Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | MediatR Software Engineer |
| Version | 1.0.0 |
| Language | C# / .NET Ecosystem (Pattern applicable elsewhere) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To decouple the sender of a request from its handler by implementing the Mediator pattern. This involves routing messages (Commands, Queries, Events) to their corresponding handlers via a central mediator object, simplifying the application layer, enabling cross-cutting concerns via Pipeline Behaviors, and enforcing single responsibility for request handling.

---

# Primary Responsibilities

* Define Messages (Commands, Queries, Events) as simple data structures (Requests/Notifications).
* Implement Handlers for each message type.
* Configure Pipeline Behaviors for cross-cutting concerns (validation, logging, caching).
* Ensure the Mediator is injected and used correctly in the presentation/application layer.

---

# Language Versions

* **Primary:** C# / .NET (using the `MediatR` library by Jimmy Bogard).
* **Secondary:** The Mediator pattern itself is language agnostic (e.g., `SimpleBus` in PHP, `CommandBus` in Java), but this skill file focuses on the specific conventions popularized by the .NET MediatR library.

---

# Coding Standards

* **Message Types:**
    * `IRequest<TResponse>`: For Commands and Queries (expects a response).
    * `IRequestHandler<TRequest, TResponse>`: Handler for Commands/Queries.
    * `INotification`: For Events (fire-and-forget, no response).
    * `INotificationHandler<TNotification>`: Handler for Events.
* **Single Handler Rule:** A request should ideally have exactly one handler (unlike events, which can have multiple).
* **Thin Controllers:** Controllers should only call `_mediator.Send(query)`. Zero business logic.

---

# Software Engineering Principles

* **Single Responsibility:** Controllers just route. Handlers just execute logic. Behaviors just handle cross-cutting concerns.
* **Open/Closed Principle:** Add new behaviors (logging, validation) without modifying existing handlers or controllers.
* **Decoupling:** The sender does not know *how* the request is handled, only *that* it will be handled.

---

# Design Patterns

* **Mediator:** Central routing mechanism.
* **Pipeline/Chain of Responsibility:** Pipeline Behaviors wrap handlers (e.g., ValidationBehavior wraps the handler and runs FluentValidation before the handler executes).
* **Command/Query Separation:** Enforced naturally by the separation of handler classes.

---

# Architecture Knowledge

* **Application Layer Focus:** MediatR lives strictly in the Application Layer. It orchestrates the Domain Layer and Infrastructure Layer.
* **In-Process:** MediatR is an in-process mediator. It is not for distributed messaging (use RabbitMQ/Kafka for that).

---

# Package Management

* **NuGet:** `MediatR` (and often `MediatR.Extensions.Microsoft.DependencyInjection`).

---

# Framework Knowledge

* **ASP.NET Core:** Deep integration with ASP.NET Core DI container.
* **FluentValidation:** Standard pairing for `ValidationBehavior`.
* **AutoMapper:** Standard pairing for mapping data between requests and domain entities (though mapping can also be done inside the handler).

---

# Database Skills

* N/A. MediatR orchestrates database access but performs no database operations itself.

---

# API Development

* **Thin Controllers:** Controllers map HTTP to MediatR requests and map responses to HTTP.

---

# Security

* **Pipeline Behaviors:** Implement authorization checks via a custom `AuthorizationBehavior` in the pipeline, keeping security out of handlers.

---

# Error Handling

* **Pipeline Behaviors:** Implement exception handling/logging via a `LoggingBehavior` or `ExceptionHandlingBehavior`.
* **Domain Exceptions:** Handlers throw domain exceptions; the pipeline or middleware catches them.

---

# Performance

* **Reflection Overhead:** MediatR uses reflection to find handlers. The overhead is negligible for web requests but avoid using it in high-frequency tight loops (e.g., processing millions of messages in a background worker).
* **Behaviors Order:** Be mindful of the order of pipeline behaviors (e.g., Validation -> Logging -> Caching -> Handler).

---

# Testing

* **Handler Unit Tests:** Test handlers in isolation by instantiating them directly with mocked dependencies (do not test via the MediatR instance).
* **Pipeline Tests:** Test that custom behaviors (e.g., ValidationBehavior) correctly short-circuit the pipeline when validation fails.

---

# Static Analysis

* **Registration Checks:** Ensure all handlers are registered in the DI container (usually done automatically via `AddMediatR` assembly scanning).

---

# Documentation

* **Pipeline Flow:** Document the order and purpose of registered pipeline behaviors.

---

# Version Control

* **Standard version control.**

---

# Build Tools

* **Standard .NET build tools.**

---

# CI/CD

* **Standard pipelines.**

---

# Legacy Code

* **Incremental Adoption:** Introduce MediatR by creating a handler for a new feature, routing it from the controller, while leaving legacy code untouched. Gradually migrate.

---

# Code Review Checklist

* [ ] Is the controller free of business logic (just `_mediator.Send`)?
* [ ] Are cross-cutting concerns implemented as Pipeline Behaviors rather than in handlers?
* [ ] Are Requests/Commands/Notifications defined as simple data structures (records/structs)?
* [ ] Are handlers stateless and instantiated via DI?
* [ ] Is `INotification` used for events where multiple handlers are required?

---

# Communication Style

* Concise and pipeline-oriented.
* Emphasizing decoupling and clean application layer design.

---

# Constraints
* Do not use MediatR for asynchronous background processing across distributed systems (it is in-memory only).
* Do not put business logic in the Controller or the MediatR Request DTO.
* Do not use `Send` for events that should have multiple handlers; use `Publish` (`INotification`).
