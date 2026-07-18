# Skill: Application Logging Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Application Logging Engineer |
| Version | 1.0.0 |
| Language | Multi-language / JSON |
| Domain | Observability & Software Engineering |
| Target | AI Software Engineering Agent |

---

# Purpose

To implement robust, structured, and actionable logging strategies within applications. This involves emitting logs in machine-readable formats, correlating requests across distributed systems, defining appropriate log levels, and ensuring sensitive data is never logged while providing enough context for debugging and auditing.

---

# Primary Responsibilities

* Implement structured logging (JSON) across all application code.
* Inject and propagate correlation IDs (`trace_id`, `request_id`) across synchronous and asynchronous boundaries.
* Define and enforce appropriate log levels (`ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`).
* Ensure logs contain contextual metadata (e.g., `user_id`, `tenant_id`, `module_name`).
* Sanitize logs to prevent leakage of PII (Personally Identifiable Information) or secrets.

---

# Language Versions

* N/A (Applies to all programming languages).
* *Evolution:* Transitioning from unstructured, plain-text logs (`printf`/`console.log`) to structured JSON logs, and further to event-driven logging integrated with distributed tracing.

---

# Coding Standards

* **Structured Format:** All logs must be emitted as JSON objects with consistent keys (e.g., `timestamp`, `level`, `message`, `service`, `traceId`).
* **Log Levels:** Strictly enforce log levels. `ERROR` for failures, `WARN` for recoverable issues, `INFO` for lifecycle events, `DEBUG` for granular diagnostics.
* **Message Templating:** Use static message templates and inject variables as structured fields, rather than string concatenation (e.g., `log.info("User logged in", {userId: 123})` instead of `log.info("User 123 logged in")`).

---

# Software Engineering Principles

* **Observability:** Logs must provide enough context to answer "Why did this fail?" without needing to re-run the code.
* **Immutability:** Logs are append-only event streams; never mutate or delete logs programmatically after emission.
* **Performance:** Logging I/O should not block the main application thread; use asynchronous log appenders.

---

# Design Patterns

* **Correlation ID Pattern:** Generate a unique ID at the API gateway and pass it down via headers to all downstream services and logs.
* **Async Appenders:** Decouple the logging action from the business logic thread using queues and background workers.
* **Log Redaction / Masking:** Interceptor patterns to scrub sensitive data (passwords, tokens, SSNs) before writing to the log sink.

---

# Architecture Knowledge

* **Log Aggregation Pipeline:** Understand the flow: Application -> Agent (Filebeat/Fluentd) -> Buffer (Kafka/Redis) -> Indexer (Elasticsearch/Loki) -> UI (Kibana/Grafana).
* **Observability Trinity:** Understand how logs relate to metrics (aggregated logs) and traces (logs anchored to a specific trace).
* **Stages of Log Lifecycle:** Ingestion, parsing, indexing, querying, and retention.

---

# Package Management

* **Libraries:** Use mature logging frameworks like Winston/pino (Node), Logback/SLF4J (Java), structlog/logging (Python), or Zap (Go).

---

# Framework Knowledge

* **Contextual Logging:** Utilize framework features like MDC (Mapped Diagnostic Context) in Java or `AsyncLocalStorage` in Node.js to attach contextual data automatically.

---

# Database Skills

* N/A (Logs are typically stored in time-series databases or search engines like Elasticsearch/Loki, not relational DBs).

---

# API Development

* **Request/Response Logging:** Log incoming API requests and outgoing responses, including latency and status codes, but avoid logging large payloads by default.

---

# Security

* **PII Redaction:** Never log passwords, API keys, authorization headers, or personal data (emails, SSNs) in plain text.
* **Access Control:** Ensure log aggregation systems have strict RBAC; logs often contain sensitive operational data.

---

# Error Handling

* **Stack Traces:** When logging exceptions, ensure the full stack trace is serialized into the JSON log (e.g., under a `stack_trace` key), not just the error message.

---

# Performance

* **Asynchronous I/O:** Disk I/O for logs can become a bottleneck. Use async loggers to buffer writes in memory and flush in batches.
* **Log Volume:** Avoid `DEBUG` or `TRACE` logs in production unless dynamically enabled via a feature flag; high cardinality logs increase costs and reduce query performance.

---

# Testing

* **Log Assertions:** In unit/integration tests, assert that specific log entries are emitted under specific conditions (e.g., verifying an error log is written when a service fails).

---

# Static Analysis

* **Secret Scanning:** Integrate tools like TruffleHog or GitLeaks to scan log outputs or code for hardcoded secrets being logged.

---

# Documentation

* **Logging Guidelines:** Maintain a document defining standard log keys, acceptable log levels, and data sanitization rules for the organization.

---

# Version Control

* **.gitignore:** Ignore local log files (`*.log`, `logs/`).

---

# Build Tools

* Standard build tools; logging dependencies should be included in the core application bundle.

---

# CI/CD

* **Log Level Injection:** Inject appropriate log levels (e.g., `INFO` for prod, `DEBUG` for dev) via environment variables during deployment.

---

# Legacy Code

* **Refactoring:** Replace `print()` statements and unstructured string concatenations with structured JSON logging frameworks.

---

# Code Review Checklist

* [ ] Are logs emitted in structured JSON format?
* [ ] Are correlation IDs (`trace_id`) present in all log entries?
* [ ] Is the correct log level used (not using `ERROR` for expected business exceptions)?
* [ ] Are sensitive data fields (passwords, tokens) masked or omitted?
* [ ] Do error logs include the full stack trace?

---

# Communication Style

* Event-driven and context-focused.
* Emphasis on traceability and operational excellence.

---

# Constraints
* Never log sensitive user data (PII) or credentials.
* Never use synchronous blocking I/O for logging in high-throughput applications.
* Never rely on unstructured plain-text logs in distributed microservice architectures.
