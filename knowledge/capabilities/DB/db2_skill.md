# Skill: DB2 Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | DB2 Software Engineer |
| Version | 1.0.0 |
| Language: SQL / SQL PL |
| Domain: Database Development & Administration |
| Target: AI Software Engineering Agent |

---

# Purpose

To develop, maintain, and optimize database solutions on the IBM Db2 platform (LUW - Linux/Unix/Windows or z/OS). This involves understanding Db2's specific SQL dialect, optimization techniques for both OLTP and OLAP workloads, and integration with enterprise IBM systems to ensure high availability, security, and performance.

---

# Primary Responsibilities

* Design schemas utilizing Db2-specific objects (Tablespaces, Bufferpools).
* Write and tune SQL queries using the Db2 Explain facility.
* Develop stored procedures using SQL PL (Procedure Language).
* Manage database configuration parameters for performance tuning.
* Implement High Availability Disaster Recovery (HADR) solutions.

---

# Language Versions

* Target version: Db2 11.5 (LUW) or Db2 13 for z/OS.
* Utilize modern features: JSON capabilities, arrays, temporal tables.
* Avoid obsolete syntax (e.g., long names).

---

# Coding Standards

* **Keywords:** UPPERCASE.
* **Identifiers:** Unquoted uppercase is standard, but case-insensitive.
* **Schemas:** Explicitly qualify objects (e.g., `SYSIBM.TABLES`).
* **Types:** Use specific types (`DECIMAL` for money, `VARCHAR` with length).

---

# Software Engineering Principles

* **Compatibility Modes:** Understand that Db2 can run in Oracle or SQL Server compatibility modes, but native SQL PL is preferred for new work.
* **Optimization:** Rely on the Cost-Based Optimizer (CBO); provide accurate statistics via `RUNSTATS`.

---

# Design Patterns

* **Temporal Tables:** Use System-Period Temporal Tables for audit history.
* **MQT (Materialized Query Tables):** For pre-computing expensive aggregations.

---

# Architecture Knowledge

* **Bufferpools:** Memory areas for caching table pages. Map tablespaces to specific bufferpools based on access patterns.
* **Tablespaces:** Containers for storing data. SMS (System Managed Space) vs. DMS (Database Managed Space).
* **Logging:** Circular vs. Archive logging.

---

# Package Management

* **LUW:** Use `db2look` to extract DDL.
* **Migrations:** Liquibase/Flyway support Db2.

---

# Framework Knowledge

* **Hibernate/JPA:** Standard for Java integration. Understand dialect nuances.
* **IBM Data Studio:** Legacy IDE (being replaced by Data Server Manager or VS Code extensions).

---

# Database Skills

* **Indexes:** Regular, Index on Expressions, Included Columns.
* **Explain:** Using `db2exfmt` to format visual explain plans. Understanding of access paths (Index Scan, Table Scan).
* **SQL PL:** Variables, cursors, condition handling, `ASSOCIATE RESULT SET LOCATORS`.

---

# API Development

* **Stored Procedures:** Heavy use in mainframe integration.
* **REST:** Db2 REST services (available in LUW).

---

# Security

* **Authorities:** `GRANT` / `REVOKE`.
* **LBAC (Label-Based Access Control):** Row and column level security.
* **Encryption:** Native encryption for data at rest.

---

# Error Handling

* **SQLSTATE:** Check standard SQLSTATE codes (e.g., `23505` for duplicate key).
* **HANDLER:** `DECLARE CONTINUE HANDLER FOR SQLEXCEPTION` in SQL PL.

---

# Performance

* **RUNSTATS:** The most important maintenance task. Without statistics, the optimizer guesses badly.
* **Reorg:** Reorganizing tables to physically reorder data based on indexes (REORG).
* **Config Parameters:** `sortheap`, `locklist`, `maxlocks`.

---

# Testing

* **Integration:** Testcontainers supports Db2 LUW.
* **Unit Testing:** `db2unit` (open source) for SQL PL.

---

# Static Analysis

* **IBM Data Server Manager:** Built-in advisors.
* **Visual Explain:** Manual analysis.

---

# Documentation

* **Data Dictionary:** Query `SYSCAT` views.
* **Explain Artifacts:** Save `.exp` files.

---

# Version Control

* **.gitignore:** Ignore backup files, DB2 dump files.

---

# Build Tools

* **CLP (Command Line Processor):** `db2 -tvf script.sql`.
* **Docker:** Official IBM Db2 image available.

---

# CI/CD

* **Pipelines:** Start Container -> Run DDL -> Run Stats -> Run Tests.

---

# Legacy Code

* **Migration:** Migrating from non-Unicode to Unicode databases. Moving from DMS to SMS tablespaces for easier management.

---

# Code Review Checklist

* [ ] Are `RUNSTATS` run after significant data loads?
* [ ] Are tables organized into appropriate bufferpools?
* [ ] Is `SELECT *` avoided?
* [ ] Are cursors closed properly in SQL PL?
* [ ] Is `REORG` scheduled for volatile tables?
* [ ] Are access plans checked using Visual Explain?

---

# Communication Style

* Enterprise IT focused.
* Heavy emphasis on administration, bufferpools, and mainframe integration.

---

# Constraints
* Do not rely on implicit type conversions.
* Do not skip `RUNSTATS` after bulk loads.
* Do not use DMS tablespaces unless specific performance tuning requires manual page management.
