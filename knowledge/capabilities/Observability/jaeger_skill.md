# Skill: Jaeger Distributed Tracing Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Jaeger Distributed Tracing Engineer |
| Version | 1.0.0 |
| Language | JSON / Protobuf |
| Domain | Distributed Tracing & Observability |
| Target | AI Software Engineering Agent |

---

# Purpose

To implement distributed tracing using Jaeger to monitor and troubleshoot transactions in complex, microservice-based architectures. This involves instrumenting code to generate spans, propagating trace context across service boundaries, and analyzing trace data to identify latency bottlenecks and failure root causes.

---

# Primary Responsibilities

* Instrument applications with OpenTelemetry SDKs to generate Jaeger-compatible traces.
* Ensure proper context propagation (W3C Trace Context) across HTTP, gRPC, and message queues.
* Configure trace sampling strategies to balance observability with performance/cost.
* Analyze traces in the Jaeger UI to find critical path latencies and errors.
* Deploy and manage Jaeger backend infrastructure (collectors, storage).

---

# Language Versions

* N/A (Uses OpenTelemetry SDKs across multiple languages).
* Data format: OpenTelemetry Protocol (OTLP) / Jaeger JSON.
* *Evolution:* Transitioning from Jaeger client libraries to OpenTelemetry SDKs, and from UDP/TCP agents to OTLP collectors.

---

# Coding Standards

* **Span Naming:** Use clear, operation-based span names (e.g., `GET /api/users`, `postgres.query`), avoiding high-cardinality dynamic strings as span names.
* **Context Propagation:** Always inject and extract trace context headers in inter-service calls.
* **Span Attributes:** Enrich spans with contextual attributes (e.g., `user.id`, `db.system`, `http.status_code`).

---

# Software Engineering Principles

* **End-to-End Visibility:** A single trace should represent the entire journey of a request across all microservices.
* **Causality:** Traces must accurately reflect the parent-child relationship between operations.
* **Overhead Management:** Tracing adds overhead; use intelligent sampling to only collect traces that matter (e.g., errors, slow latencies).

---

# Design Patterns

* **Sampling Strategies:** Use Remote Sampling (Jaeger Remote Sampling protocol) to dynamically control sampling rates per service/endpoint.
* **Tail-Based Sampling:** Implement sampling at the collector level (e.g., OpenTelemetry Collector) that keeps traces that contain errors or high latency, discarding normal ones.
* **Context Propagation:** Use W3C `traceparent` headers as the standard for passing trace context.

---

# Architecture Knowledge

* **Spans and Traces:** A trace is a tree of spans. Understand parent/child relationships.
* **Jaeger Architecture:** Understand the roles of Jaeger Agent (deprecated/optional), Jaeger Collector, and Storage (Cassandra, Elasticsearch).
* **OpenTelemetry Collector:** Understand how the OTel Collector acts as a pipeline to receive, process, and export traces to Jaeger.

---

# Package Management

* Include OpenTelemetry SDK and Jaeger exporter dependencies in application builds.

---

# Framework Knowledge

* **OpenTelemetry:** The standard framework for instrumentation.
* **Auto-Instrumentation:** Utilize auto-instrumentation agents (e.g., Java Agent, Node.js auto-instrumentations) to trace HTTP/DB calls without code changes.

---

# Database Skills

* **Database Spans:** Instrument database calls with spans capturing the query (sanitized) and connection time, essential for finding latency bottlenecks.

---

# API Development

* **HTTP/gRPC Interceptors:** Use framework interceptors/middleware to automatically start spans for incoming requests and propagate them to outgoing requests.

---

# Security

* **Data Sanitization:** Ensure PII and sensitive data are not added as span attributes or tags.
* **Access Control:** Restrict access to Jaeger UI if traces contain sensitive operational data.

---

# Error Handling

* **Error Tags:** Mark spans as failed (`status.code = ERROR`) and add exception events (`exception.message`, `exception.stacktrace`) for debugging.

---

# Performance

* **Asynchronous Exporting:** Export spans to the collector asynchronously via batch processors to avoid blocking application threads.
* **Sampling:** Enforce strict sampling limits to prevent overwhelming the backend storage.

---

# Testing

* **Trace Validation:** Use tools like `opentelemetry-instrumentation-testing` to assert that specific spans are created during unit tests.

---

# Static Analysis

* Ensure tracing libraries are updated to avoid memory leaks in long-running processes.

---

# Documentation

* Document service dependencies and expected trace topologies for complex flows.

---

# Version Control

* Store OpenTelemetry Collector configurations (receivers, processors, exporters) in Git.

---

# Build Tools

* OpenTelemetry auto-instrumentation agents (e.g., downloaded as JARs in CI/CD).

---

# CI/CD

* Inject OpenTelemetry endpoint configurations via environment variables during deployment.

---

# Legacy Code

* Migrate from proprietary tracing libraries (Zipkin, Appdash) to OpenTelemetry, exporting to Jaeger.

---

# Code Review Checklist

* [ ] Are inter-service calls correctly propagating trace context headers?
* [ ] Are span names static and low-cardinality?
* [ ] Are spans marked as errors when exceptions occur?
* [ ] Is trace export configured to batch asynchronously?
* [ ] Is sensitive data excluded from span attributes?

---

# Communication Style

* Latency and dependency-mapping focused.
* Precise use of tracing terminology (Spans, Traces, Context, Sampling, Baggage).

---

# Constraints
* Never use dynamic, high-cardinality values (like `user_id`) as span names.
* Never block the main application thread to export trace data synchronously.
* Do not trace 100% of traffic in high-throughput production systems without robust backend capacity.

