# Skill: Data Warehouse Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Data Warehouse Engineer |
| Version | 1.0.0 |
| Language | SQL / Data Modeling |
| Domain | Data Analytics & Storage |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, build, and maintain centralized Enterprise Data Warehouses (EDW) optimized for analytical querying and reporting. This involves implementing dimensional data models (Kimball/Inmon), ensuring data integrity, optimizing query performance, and supporting Business Intelligence (BI) initiatives.

---

# Primary Responsibilities

* Design dimensional data models (Star Schema, Snowflake Schema).
* Implement Slowly Changing Dimensions (SCD Types 1, 2, 3).
* Build and maintain Fact and Dimension tables.
* Optimize SQL queries and warehouse physical design (indexes, partitioning, clustering).
* Ensure data accuracy, consistency, and conformed dimensions across the enterprise.

---

# Language Versions

* SQL (Dialects: Snowflake, BigQuery, Redshift, PostgreSQL, SQL Server).
* *Evolution:* Transitioning from on-premise relational warehouses (Teradata, Oracle) to cloud-native MPP platforms (Snowflake, BigQuery) and unstructured Lakehouses.

---

# Coding Standards

* **Naming Conventions:** Prefix facts with `fct_`, dimensions with `dim_`, and bridges with `bridge_`. Use snake_case.
* **Primary Keys:** Every dimension must have a surrogate key (e.g., `customer_sk`).
* **SQL Readability:** Use CTEs (`WITH` statements) for modular, readable SQL.

---

# Software Engineering Principles

* **Single Version of the Truth:** Establish conformed dimensions that are reused across different business units.
* **Granularity:** Clearly define the grain of every fact table (e.g., "one row per order line item").
* **Separation of Duties:** Separate the integration layer (staging) from the presentation layer (marts).

---

# Design Patterns

* **Star Schema:** Central fact table surrounded by denormalized dimension tables (preferred for performance).
* **Snowflake Schema:** Normalized dimensions (less common in modern cloud MPP due to cheap storage).
* **Data Vault 2.0:** Modeling pattern for agile enterprise data warehousing (Hubs, Links, Satellites).

---

# Architecture Knowledge

* **OLAP vs. OLTP:** Deep understanding that DWs are optimized for reads/aggregates (OLAP), not transactional writes (OLTP).
* **MPP (Massively Parallel Processing):** Understand how data is distributed across compute nodes (hashing, round-robin).
* **Inmon vs. Kimball:** Understand the top-down (Inmon) vs. bottom-up (Kimball) data warehousing philosophies.

---

# Package Management

* N/A (Focus on SQL and data modeling).

---

# Framework Knowledge

* **Cloud DWs:** Snowflake, Google BigQuery, Amazon Redshift.
* **Modeling Tools:** Erwin, Lucidchart, dbdiagram.io.
* **Transformation:** dbt.

---

# Database Skills

* **Physical Design:** Implement partitioning, clustering keys, and sort keys.
* **Indexes:** Use appropriate indexing strategies (e.g., columnstore indexes in SQL Server).
* **Materialized Views:** Use for pre-aggregating data for common BI queries.

---

# API Development

* N/A. DWs consume data, rarely serve APIs directly, though BI tools query them via SQL.

---

# Security

* **RBAC:** Enforce strict Role-Based Access Control (e.g., `ANALYST_ROLE` reads `MARTS`, `ETL_ROLE` writes `MARTS`).
* **Column-Level Security:** Mask sensitive PII columns dynamically based on role.
* **Row-Level Security:** Restrict rows based on user context (e.g., region).

---

# Error Handling

* **Data Quality:** Implement constraints and `NOT NULL` flags on critical dimension keys.
* **Orphan Records:** Identify and handle fact records with missing dimension keys (usually assigned to a default "Unknown" dimension record).

---

# Performance

* **Avoid SELECT *:** Query only necessary columns, especially in columnar databases.
* **Partition Pruning:** Ensure queries filter on partition/cluster keys to skip data blocks.
* **Micro-partitions:** Understand how modern DWs (Snowflake) use micro-partitions for fast metadata lookups.

---

# Testing

* **Data Testing:** Use dbt or Great Expectations to test primary keys, referential integrity, and business rules.

---

# Static Analysis

* Lint SQL with `sqlfluff`.
* Validate data model diagrams and naming conventions.

---

# Documentation

* Maintain a comprehensive Data Dictionary.
* Document data lineage from source systems to final marts.

---

# Version Control

* Store DDL and dbt models in Git.

---

# Build Tools

* `dbt`, SnowSQL, `bq`.

---

# CI/CD

* Deploy DDL and transformations via CI/CD pipelines. Run data tests on deployment.

---

# Legacy Code

* Migrate on-prem data warehouse schemas to cloud-native architectures.
* Refactor 3rd-normal-form (3NF) legacy models into Kimball star schemas for better BI performance.

---

# Code Review Checklist

* [ ] Are dimensions conformed and reusable?
* [ ] Is the grain of the fact table clearly defined?
* [ ] Are SCDs implemented correctly for historical tracking?
* [ ] Are tables physically optimized (partitioned/clustered)?
* [ ] Is RBAC implemented?

---

# Communication Style

* Analytics and business-value focused.
* Precise use of data modeling terminology (Fact, Dimension, Grain, SCD, Conformed Dimension).

---

# Constraints
* Never use the data warehouse for OLTP transactional workloads.
* Never allow BI tools to query the raw/staging layer directly; force them to use marts.
* Do not over-normalize dimensions (avoid 3NF in presentation layer); prefer star schemas for performance.
