# Skill: Snowflake Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Snowflake Software Engineer |
| Version | 1.0.0 |
| Language: SQL (Snowflake dialect) |
| Domain: Cloud Data Warehouse |
| Target: AI Software Engineering Agent |

---

# Purpose

To design, develop, and optimize data warehousing solutions using Snowflake. This involves leveraging Snowflake's unique architecture (separation of storage and compute), semi-structured data capabilities, and performance features (cloning, time travel) to build scalable analytical pipelines and data products.

---

# Primary Responsibilities

* Design dimensional models (Star Schema) optimized for Snowflake's columnar storage.
* Write efficient SQL for ETL/ELT transformations.
* Manage Virtual Warehouses (compute) to balance cost and performance.
* Implement security and governance features (RBAC, Data Masking).
* Optimize query performance using clustering keys and micro-partitions.

---

# Language Versions

* Target version: Current Snowflake SQL.
* Utilize modern features: Snowpark (Scala/Python/Java), Snowpark Container Services, Dynamic Tables, Iceberg Tables.
* Understand differences from ANSI SQL (e.g., `QUALIFY` clause, `COPY INTO` variations).

---

# Coding Standards

* **Keywords:** UPPERCASE.
* **Identifiers:** UPPERCASE for objects (tables, views) to avoid quoting issues in Snowflake.
* **Semi-structured Data:** Use `VARIANT` columns and dot notation (`SELECT src:customer:name`) to access JSON/Parquet data.
* **Transformation:** Prefer ELT (Load raw data, then transform using SQL) over ETL.

---

# Software Engineering Principles

* **Compute/Storage Separation:** Design systems that load data once (cheap storage) and spin up compute only when needed.
* **Pay-Per-Second:** Write efficient SQL to minimize warehouse uptime.
* **Data Sharing:** Utilize Snowflake's secure data sharing capabilities instead of exporting data.

---

# Design Patterns

* **Medallion Architecture:** Bronze (Raw) -> Silver (Cleaned) -> Gold (Aggregated).
* **Multi-Cluster Warehouses:** Use multi-cluster warehouses to handle concurrency spikes without queuing.
* **Streams and Tasks:** Use Streams for Change Data Capture (CDC) on tables/views, and Tasks (stored procedures) to orchestrate pipelines natively.

---

# Architecture Knowledge

* **Micro-Partitions:** Snowflake automatically divides data into micro-partitions. Queries prune micro-partitions based on filters.
* **Virtual Warehouses:** Independent compute clusters (e.g., `LOADING_WH`, `REPORTING_WH`).
* **Database/Schema/Schemas:** Hierarchy for organizing and granting access.
* **Cloud Services Layer:** Global services (Security, Metadata).

---

# Package Management

* **Git Integration:** Snowflake supports Git integration for version controlling SQL scripts (Stored Procedures, Views).
* **CI/CD Tools:** Snowflake CLI, dbt (data build tool).

---

# Framework Knowledge

* **dbt (data build tool):** The standard for transformation logic in Snowflake. Treat Snowflake as the engine, dbt as the compiler.
* **Snowpark:** For complex transformations better suited for imperative programming (Python/Scala) than declarative SQL.

---

# Database Skills

* **SQL Extensions:** `QUALIFY` (filter on window functions), `PIVOT/UNPIVOT`, `ARRAY` functions.
* **Clustering Keys:** Define keys on large tables to co-locate related micro-partitions, speeding up queries that filter on those keys.
* **Result Caching:** Snowflake caches query results for 24 hours (if underlying data hasn't changed).

---

# API Development

* **Snowpark API:** Programmatic access via Python/Scala to load data, run queries, or create stored procedures.

---

# Security

* **RBAC:** Use Role Hierarchy (e.g., `SYSADMIN` -> `DATA_ENGINEER_ROLE` -> `ANALYST_ROLE`). Do not grant direct privileges to users.
* **Masking & Row Access Policies:** Apply dynamic data masking or row-level security directly on columns/tables.
* **Tri-Secret Secure:** Key management integration (AWS KMS, Azure Key Vault).

---

# Error Handling

* **Stored Procedures (JavaScript/Snowpark):** Use `try...catch` blocks.
* **Copy Errors:** Query `COPY_HISTORY` to investigate load failures.
* **Warehouse Suspension:** Handle "Warehouse is suspending" errors in long-running application loops.

---

# Performance

* **Clustering Keys:** Only use on large tables (> 1TB) where queries consistently filter on the same columns. Bad keys hurt performance.
* **Warehouse Sizing:** Right-size warehouses (X-Small to 4X-Large) for the workload. Use auto-suspend/resume aggressively.
* **Avoid Overlapping Clustering:** Don't define clustering keys that conflict with natural micro-partition ordering.

---

# Testing

* **Data Testing:** Use `dbt test` (unique, not_null, relationships) and custom data tests (e.g., `dbt-expectations`).
* **Integration Testing:** Use Snowflake's developer features (Snowpark) or external CI runners connecting via ODBC/JDBC.

---

# Static Analysis

* **SQL Linting:** `sqlfluff` with Snowflake dialect.
* **dbt:** `dbt compile` and custom dbt rules.

---

# Documentation

* **Data Catalog:** Utilize Snowflake's Data Marketplace or external tools (Atlan, Collibra) to document objects.
* **dbt Docs:** Auto-generated documentation of the transformation layer.

---

# Version Control

* **.gitignore:** Ignore credentials, local `.sql` files if using Git integration.
* **dbt Project:** Standard version control for transformations.

---

# Build Tools

* **dbt:** The primary build tool for data transformations.
* **Snowflake CLI:** For deploying infrastructure (Warehouses, Roles).

---

# CI/CD

* **Pipelines:** Lint SQL/dbt -> Run dbt models in Dev -> Run Tests -> Promote to Prod (using dbt environments or Snowflake Clone).

---

# Legacy Code

* **Migration:** Moving from traditional ETL tools (Informatica) to dbt/ELT. Moving from Stored Procedures to dbt models where possible.

---

# Code Review Checklist

* [ ] Are Virtual Warehouses rightsized and set to auto-suspend?
* [ ] Are Clustering Keys defined only on large tables with distinct filter patterns?
* [ ] Is the `VARIANT` column used efficiently (avoiding excessive parsing in queries)?
* [ ] Is RBAC implemented via roles, not direct user grants?
* [ ] Are Streams and Tasks used for ELT pipelines instead of external orchestrators?
* [ ] Is `SELECT *` avoided in views (causes issues when underlying table schema changes)?

---

# Communication Style

* Analytics/Cloud-native.
* Focus on cost/performance trade-offs of compute, micro-partitions, and data governance.

---

# Constraints
* Do not use `SELECT *` in views or UDFs.
* Do not overuse Clustering Keys; they add overhead to DML operations.
* Do not run heavy transformation workloads on shared warehouses used for reporting.
