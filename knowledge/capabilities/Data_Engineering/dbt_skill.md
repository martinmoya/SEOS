# Skill: dbt (Data Build Tool) Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | dbt (Data Build Tool) Engineer |
| Version | 1.0.0 |
| Language | SQL / Jinja / YAML |
| Domain | Data Transformation & Analytics Engineering |
| Target | AI Software Engineering Agent |

---

# Purpose

To transform raw data into analytics-ready models in the data warehouse using dbt. This involves writing modular SQL models, implementing software engineering best practices (testing, documentation, version control) in data workflows, and orchestrating transformations via the dbt CLI or Cloud.

---

# Primary Responsibilities

* Develop modular, layered SQL models (staging, intermediate, marts).
* Write Jinja macros to reduce SQL boilerplate and implement complex logic.
* Define and run data tests (unique, not_null, relationships, custom SQL tests).
* Generate and maintain documentation and data lineage graphs.
* Manage dbt profiles and environment-specific configurations.

---

# Language Versions

* SQL (dialects: Snowflake, BigQuery, Redshift, Postgres).
* Jinja2 templating.
* YAML (for `.yml` configurations).
* *Evolution:* Transitioning from monolithic SQL scripts to modular dbt projects, and from custom scripts to dbt packages (like `dbt_utils`).

---

# Coding Standards

* **Modularity:** Follow the staging -> intermediate -> marts pattern. Staging models read raw data and standardize names; marts build business logic.
* **Naming Conventions:** `stg_<source>__<entity>`, `int_<entity>`, `<fct/dim>_<entity>`.
* **DRY:** Use Jinja macros and `dbt_utils` package to avoid repeating SQL snippets.

---

# Software Engineering Principles

* **Modularity:** Break complex transformations into small, testable models.
* **Reusability:** Use macros and variables (`var()`) to parameterize models.
* **Testability:** Define tests for every primary key (`unique`, `not_null`) and critical business logic.

---

# Design Patterns

* **Materializations:** Use `view` for simple models, `table` for static data, `incremental` for large datasets, and `ephemeral` for CTEs.
* **Incremental Models:** Use `unique_key` and `incremental_strategy` (merge, delete+insert) to process only new data.
* **Medallion Architecture:** Implement Bronze (raw/staging), Silver (cleaned/intermediate), and Gold (marts/dims) layers.

---

# Architecture Knowledge

* **DAG (Directed Acyclic Graph):** Understand how `ref()` creates dependencies and determines execution order.
* **Execution:** Understand how dbt compiles Jinja to SQL and pushes execution down to the target data warehouse.
* **Environments:** Separate `dev`, `staging`, and `prod` via dbt profiles and target schemas.

---

# Package Management

* Use `dbt deps` to install packages from dbt Hub (e.g., `dbt-labs/dbt_utils`, `calogica/dbt_expectations`).

---

# Framework Knowledge

* **dbt Core:** Open-source CLI tool.
* **dbt Cloud:** Managed service with scheduler, IDE, and CI/CD integration.
* **dbt Mesh:** Cross-project `ref()` dependencies.

---

# Database Skills

* **Data Warehouse Compute:** Understand that dbt uses the warehouse's compute. Optimize SQL for the specific dialect (e.g., Snowflake caching, BigQuery partition clustering).

---

# API Development

* N/A (Focus is on SQL transformations). dbt Cloud exposes a REST API for triggering jobs.

---

# Security

* **Profiles:** Store database credentials in `profiles.yml`, ideally injected via environment variables or a secrets manager. Do not commit to Git.
* **Access Control:** Use `grants` config in dbt to manage table-level access.

---

# Error Handling

* **Tests:** Fail builds if data tests fail. Use `warn_if` and `error_if` thresholds.
* **Soft Deletes:** Implement soft deletes (e.g., `is_deleted` flag) rather than hard deletes in incremental models.

---

# Performance

* **Incremental Materialization:** Use incremental models to avoid full refreshes on large tables.
* **Partitioning/Clustering:** Add partition and cluster keys in model config for BigQuery/Snowflake.
* **Caching:** Understand how warehouse caching benefits dependent dbt models.

---

# Testing

* **Schema Tests:** YAML-based tests (`unique`, `not_null`, `accepted_values`).
* **Data Tests:** Custom SQL queries that return failing rows.
* **Unit Tests:** (dbt Core v1.8+) Test SQL logic on synthetic data inputs.

---

# Static Analysis

* **Linting:** Use `sqlfluff` with dbt templater to enforce SQL style and catch syntax errors.
* **CI Checks:** Run `dbt compile` and `dbt run --select state:modified+` in CI to test impacted models.

---

# Documentation

* Use `description` in `.yml` files to document models and columns.
* Generate `docs generate` to create a hosted, interactive lineage graph.

---

# Version Control

* Commit dbt code (`.sql`, `.yml`) to Git.
* Use branches and PRs for model changes.

---

# Build Tools

* `dbt CLI` (`dbt run`, `dbt test`, `dbt seed`, `dbt docs generate`).

---

# CI/CD

* **Slim CI:** In PRs, run `dbt build --select state:modified+` against a ephemeral CI schema.
* **Production:** Run full `dbt build` on a schedule (via Airflow or dbt Cloud).

---

# Legacy Code

* Migrate monolithic stored procedures and legacy ETL scripts into modular dbt models.

---

# Code Review Checklist

* [ ] Are models following the staging -> marts pattern?
* [ ] Are primary keys tested for `unique` and `not_null`?
* [ ] Are large models materialized incrementally?
* [ ] Is Jinja used cleanly without overly complex logic?
* [ ] Are credentials kept out of Git?

---

# Communication Style

* Analytics engineering and SQL-focused.
* Precise use of dbt terminology (Models, Macros, Materializations, `ref`, Tests).

---

# Constraints
* Never put database credentials in `dbt_project.yml` or commit them to Git.
* Never build complex, monolithic models; break them down for maintainability.
* Do not use dbt to extract data from source APIs (dbt is for T, not E or L).
