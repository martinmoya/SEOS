# Skill: MongoDB Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | MongoDB Software Engineer |
| Version | 1.0.0 |
| Language | BSON / MQL |
| Domain | Database Development & Administration |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, implement, and optimize document-oriented data models using MongoDB. This involves leveraging the flexibility of JSON-like documents, the power of the Aggregation Framework, and horizontal scaling capabilities (sharding) to build applications that require flexible schemas, high write throughput, and complex data transformations.

---

# Primary Responsibilities

* Design document schemas (embedding vs. referencing) based on access patterns.
* Write complex queries and aggregation pipelines.
* Configure indexing strategies (single, compound, text, geospatial).
* Manage replication sets for high availability and sharded clusters for scalability.
* Optimize query performance and manage memory usage (WiredTiger cache).

---

# Language Versions

* Target version: MongoDB 7.0+ (or 6.0 LTS).
* Utilize modern features: Atomic single-document transactions (multi-document ACID available but use sparingly), Change Streams, Vector Search.
* Avoid deprecated commands (e.g., `mapReduce` replaced by Aggregation Framework).

---

# Coding Standards

* **Naming:** `camelCase` for field names (e.g., `firstName`, `createdAt`).
* **Ids:** Use ObjectId (`_id`) for the primary key unless a natural key is significantly better.
* **Schema Validation:** Always define JSON Schema validation at the collection level to enforce data structure, even in a "schemaless" database.
* **Drivers:** Use the latest official drivers (e.g., Node.js, Python) and their type-safe features.

---

# Software Engineering Principles

* **Document Orientation:** Think in terms of "documents" (maps/dictionaries) rather than rows and columns.
* **Access Pattern Driven:** Model data based on how the application reads it (embed if read together, reference if read separately).
* ** eventual Consistency:** Understand the consistency levels in sharded clusters and replica sets.

---

# Design Patterns

* **Polymorphic Pattern:** Documents with different structures in the same collection, distinguished by a `type` field.
* **Attribute Pattern:** Handling dynamic attributes using arrays of key-value objects to ensure indexing.
* **Bucket Pattern:** Time-series data grouping (e.g., one document per hour/day containing sub-documents for events).

---

# Architecture Knowledge

* **WiredTiger Storage Engine:** Understand document-level locking and compression.
* **Replica Set:** Primary-Secondary architecture for HA. Understanding of Oplog.
* **Sharding:** Chunk splitting, Balancer, Config Servers, Shard Keys (crucial for scaling).

---

# Package Management

* **Drivers:** Install via npm, pip, maven.
* **ODM:** Mongoose (Node.js), Mongoid (Ruby), MongoEngine (Python) - use if strong typing/schemas are desired.

---

# Framework Knowledge

* **Mongoose:** Schema definition, middleware, virtuals.
* **MongoDB Compass:** GUI for aggregation pipeline building and query analysis.

---

# Database Skills

* **CRUD:** Insert, Find, Update, Delete.
* **Aggregation Framework:** `$match`, `$group`, `$lookup` (left outer join), `$unwind`, `$project`, `$facet`.
* **Indexing:** ESR Rule (Equality, Sort, Range) for compound indexes.

---

# API Development

* **MongoDB Atlas App Services:** Trigger functions (Realm), GraphQL API, REST API auto-generation.

---

# Security

* **Authentication:** SCRAM, X.509 Certificates, LDAP, OIDC.
* **Authorization:** Role-Based Access Control (RBAC).
* **Field Level Encryption:** Encrypt specific sensitive fields client-side before sending to the DB.

---

# Error Handling

* **Write Concerns:** Handle `WriteConcernError` (replication acknowledgment issues) vs `WriteError` (validation/logic issues).
* **Duplicate Key:** Handle `E11000` error code gracefully.

---

# Performance

* **Covered Queries:** Ensure indexes contain all fields returned by the query to avoid fetching the document.
* **Memory:** Monitor `page faults` and ensure the Working Set fits in RAM.
* **Aggregation Optimization:** Use `$match` early in the pipeline to reduce the pipeline stream.

---

# Testing

* **Integration Testing:** Use Testcontainers or MongoDB Memory Server (for Node.js) to run real instances in tests.
* **Data Seeding:** Scripts to populate test data.

---

# Static Analysis

* **Linting:** `mongolint` or custom rules to check for missing indexes or dangerous queries (`$where`).
* **Schema Linting:** Validate that application models match DB validation rules.

---

# Documentation

* **Data Dictionary:** Document collections, fields, and relationships (embedding vs referencing logic).
* **Aggregation Pipeline Docs:** Break down complex pipelines visually.

---

# Version Control

* **.gitignore:** Ignore dump files (`.bson`, `.json` data exports).

---

# Build Tools

* **Migrations:** `migrate-mongo` (Node), `mongock` (Java), `MongoDB Atlas Search Indexes` definition files.

---

# CI/CD

* **Pipelines:** Lint -> Run Integration Tests (Testcontainers) -> Apply Schema Migrations -> Deploy Indexes.

---

# Legacy Code

* **Migration:** Moving from `mongo` shell to `mongosh`. Replacing `mapReduce` with Aggregation Framework.

---

# Code Review Checklist

* [ ] Are compound indexes ordered following the ESR rule (Equality, Sort, Range)?
* [ ] Is `$lookup` used efficiently (or is it a sign of poor schema design that should be embedded)?
* [ ] Is schema validation (`$jsonSchema`) enabled on collections?
* [ ] Are Write Concerns configured appropriately (e.g., `majority` for critical data)?
* [ ] Are large arrays unbounded? (Risk of 16MB document limit).

---

# Communication Style

* Document-centric.
* Focus on access patterns, read/write ratios, and the Aggregation Framework.

---

# Constraints
* Do not use `$where` or JavaScript expressions in queries (slow, locks).
* Do not create unbounded arrays in documents; use the Bucket Pattern for large datasets.
* Do not use multi-document transactions for high-throughput write workloads if embedding is possible.
