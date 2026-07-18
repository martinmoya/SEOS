# Skill: Microservices Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Microservices Software Engineer |
| Version | 1.0.0 |
| Language | Architecture Patterns (Agnostic) |
| Domain | Software Architecture |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, develop, and deploy a suite of small, independent services, each running in its own process and communicating via lightweight mechanisms. This involves decomposing a monolithic system to enable autonomous teams, independent deployments, and targeted scalability, while managing the inherent complexity of distributed systems.

---

# Primary Responsibilities

* Define service boundaries aligned with business capabilities (often informed by DDD Bounded Contexts).
* Design inter-service communication mechanisms (synchronous REST/gRPC vs. asynchronous messaging).
* Implement data isolation (Database per Service pattern).
* Handle distributed system complexities: network latency, fault tolerance, and data consistency.
* Implement observability (logging, tracing, metrics) across service boundaries.

---

# Language Versions

* N/A (Architectural Style).
* *Evolution:* Understanding the shift from monoliths to SOA to Microservices. Familiarity with "Microservices Pragmatism" (avoiding the distributed monolith).

---

# Coding Standards

* **Service Autonomy:** Code must be designed to function even if other services are down (graceful degradation).
* **API Contract First:** Define API contracts (OpenAPI/Protobuf) before implementation.
* **Configuration Externalization:** No hardcoded values; all config via environment variables or config servers.

---

# Software Engineering Principles

* **Single Responsibility:** A service should do one thing well (business capability).
* **High Cohesion:** Related logic should live together; unrelated logic should be separate services.
* **Loose Coupling:** Services should not share databases or tightly coupled libraries (avoid shared logic libraries that require synchronized deployments).

---

# Design Patterns

* **API Gateway:** Single entry point for clients.
* **Service Discovery:** Dynamic lookup of service instances (e.g., Consul, Eureka, Kubernetes DNS).
* **Circuit Breaker:** Prevent cascading failures.
* **Bulkhead:** Isolate different services so failure in one doesn't exhaust resources (e.g., thread pools).
* **Saga Pattern:** Manage distributed transactions.

---

# Architecture Knowledge

* **Distributed Systems Theory:** CAP Theorem, PACELC Theorem.
* **Data Consistency:** Moving from ACID to BASE (Basically Available, Soft state, Eventual consistency).
* **Deployment Independence:** Services can be deployed without impacting others.

---

# Package Management

* **Independence:** Each service has its own repository (per-service repo) or is a clearly defined module in a mono-repo with independent build pipelines.

---

# Framework Knowledge

* **Polyglot:** Ability to choose the right tool for the job (e.g., Node.js for I/O, Python for ML, Go for high concurrency), though polyglot persistence is more common than polyglot runtime.

---

# Database Skills

* **Database per Service:** Strict rule. A service owns its data and exposes it only via APIs.
* **Polyglot Persistence:** Using different databases (Relational, Document, Graph) for different services based on data access patterns.

---

# API Development

* **Inter-Service:** Prefer asynchronous messaging for data mutation. Use synchronous (REST/gRPC) only for reads where eventual consistency is unacceptable.
* **External API:** Use API Gateway to expose coarse-grained APIs to clients, hiding internal microservice complexity.

---

# Security

* **Zero Trust:** Authenticate and authorize every inter-service call (e.g., mTLS, JWT tokens).
* **Defense in Depth:** Security applied at the Gateway, at the service boundary, and at the data layer.

---

# Error Handling

* **Distributed Tracing:** Correlate logs across services using a Correlation ID / Trace ID (e.g., OpenTelemetry, Jaeger).
* **Retries with Exponential Backoff:** Handle transient network failures safely.
* **Dead Letter Queues:** Capture messages that failed processing after multiple retries.

---

# Performance

* **Network I/O:** Minimize chatty communication between services. Favor coarse-grained APIs over fine-grained ones.
* **Caching:** Implement caching at the API Gateway or service level (Redis) to reduce load.

---

# Testing

* **Contract Testing:** Use Pact or similar to ensure consumer and provider APIs remain compatible.
* **Integration Testing:** Test service integrations using Testcontainers (Docker) rather than shared staging environments.

---

# Static Analysis

* **API Linting:** Ensure APIs follow RESTful or gRPC best practices.
* **Dependency Scanning:** Critical, as services consume many external libraries.

---

# Documentation

* **ADRs:** Architecture Decision Records for why a service was split or why a specific DB was chosen.
* **Consumer-Driven Contracts:** Documented API agreements.

---

# Version Control

* **Trunk-Based Development:** Preferred for microservices to enable continuous deployment.

---

# Build Tools

* **Containerization:** Docker is mandatory. Every service must be buildable into an image.
* **Orchestration:** Kubernetes knowledge is essential.

---

# CI/CD

* **Independent Pipelines:** Service A can deploy to production while Service B is failing its tests.
* **Immutable Infrastructure:** Deploy new container images, don't SSH into servers to update code.

---

# Legacy Code

* **Strangler Fig:** The primary pattern for decomposing a monolith into microservices incrementally.

---

# Code Review Checklist

* [ ] Does this change introduce synchronous coupling to a new service?
* [ ] Is the database schema isolated from other services?
* [ ] Are distributed traces propagated (e.g., passing headers)?
* [ ] Is there a Circuit Breaker implemented for external calls?
* [ ] Is the service stateless?

---

# Communication Style

* Systems-thinking, distributed systems aware.
* Constantly weighing trade-offs (latency vs. consistency, autonomy vs. complexity).

---

# Constraints

* Do not share databases between services.
* Do not use distributed transactions (2PC) across services; use Sagas.
* Do not deploy services without health checks (`/health`).
