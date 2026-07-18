# Skill: SQL Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | SQL Software Engineer |
| Version | 1.0.0 |
| Language | SQL |
| Domain | Software Development |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, implement, and optimize relational database systems. This involves modeling data accurately, writing efficient and secure queries, ensuring data integrity via constraints and transactions, and understanding the physical storage and execution mechanics of database engines to achieve high performance and availability.

---

# Primary Responsibilities

* Design normalized or intentionally denormalized schemas.
* Write complex analytical and transactional queries.
* Optimize query performance using indexes and execution plans.
* Implement robust transactional logic.
* Ensure data security and privacy.

---

# Language Versions

* Target version: ANSI SQL:2016 (or latest).
* Be aware of dialect-specific extensions (PostgreSQL, SQL Server/T-SQL, MySQL, Oracle PL/SQL) but prioritize standard ANSI SQL where possible for portability.

---

# Coding Standards

* **Keywords:** UPPERCASE for keywords (`SELECT`, `FROM`, `WHERE`), lowercase for identifiers.
* **Indentation:** Indent joins, where clauses, and subqueries.
* **Aliases:** Always use table aliases in joins. Use meaningful aliases (e.g., `o` for orders, `c` for customers), not `a`, `b`, `c`.
* **Select ***: NEVER use `SELECT *` in application code. Explicitly list columns.

---

# Software Engineering Principles

* **ACID Properties:** Understand and ensure Atomicity, Consistency, Isolation, Durability.
* **Normalization:** Follow normal forms (1NF, 2NF, 3NF, BCNF) to eliminate redundancy, unless denormalization is required for read performance.
* **Immutability:** Use temporal tables or append-only patterns for auditability where applicable.

---

# Design Patterns

* **Soft Delete:** Use a `deleted_at` timestamp column instead of physically deleting rows (requires `WHERE deleted_at IS NULL` on all queries).
* **Adjacency List / Closure Table:** For hierarchical data (trees).
* **Entity-Attribute-Value (EAV):** Use sparingly only when schema is highly dynamic; prefer typed columns.
* **Upsert:** `MERGE` statement (or `ON CONFLICT` in Postgres, `ON DUPLICATE KEY` in MySQL) for idempotent inserts.

---

# Architecture Knowledge

* **OLTP vs OLAP:** Design schemas differently for transactional processing vs analytical reporting.
* **Data Warehouse:** Star Schema, Snowflake Schema, Fact tables, Dimension tables.
* **Partitioning:** Range, List, or Hash partitioning for large tables.

---

# Package Management

* N/A (Managed via database migration tools).

---

# Framework Knowledge

* **ORM Integration:** Understand how ORMs (Hibernate, Entity Framework, Prisma) generate SQL to anticipate performance issues.
* **Query Builders:** Knowledge of how tools like Knex.js or jOOQ construct queries.

---

# Database Skills

* **DDL:** `CREATE TABLE`, `ALTER TABLE`. Understand data types (use `VARCHAR(n)` appropriately, avoid `TEXT` for searchable columns).
* **Constraints:** `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK` constraints. Enforce integrity at the DB level, not just in the app.
* **Indexes:** B-Tree, Hash, GIN/GiST (Postgres), Full-Text. Understand clustered vs non-clustered.
* **Views:** Use for security (hiding columns) or complex query simplification. Avoid nesting views.

---

# API Development

* **Stored Procedures:** Use for complex, encapsulated business logic that requires high performance and minimal network roundtrips. Avoid for simple CRUD.
* **Functions:** Be cautious with scalar functions in `SELECT` lists (can kill performance). Prefer inline table-valued functions.

---

# Security

* **SQL Injection:** Prevented strictly by parameterized queries or ORMs. Never concatenate strings.
* **Principle of Least Privilege:** App code should only have SELECT/INSERT/UPDATE/DELETE on specific tables, never DDL rights.
* **Data Masking:** Use dynamic data masking for sensitive columns (SSNs, credit cards) for non-privileged users.
* **Encryption:** TDE (Transparent Data Encryption) for data at rest.

---

# Error Handling

* **Transactions:** Explicitly use `BEGIN TRAN`, `COMMIT`, `ROLLBACK`. Handle deadlocks (error 1205 in SQL Server) by retrying logic.
* **Exceptions:** Use `TRY...CATCH` blocks (T-SQL/PL/SQL) to handle errors gracefully and log them.

---

# Performance

* **Execution Plans:** The most critical skill. Read plans to find Table Scans vs Index Seeks, Sorts, Spools.
* **SARGability:** Ensure predicates are "Search ARGument ABLE" (avoid functions on left side of `WHERE` clause).
* **N+1 Problem:** Identify and fix via batching or joins.
* **Locking:** Understand shared/exclusive locks, row-level vs page-level locking. Use appropriate isolation levels (Read Committed Snapshot Isolation is often preferred).

---

# Testing

* **Unit Testing:** Test stored procedures/functions using frameworks like tSQLt (SQL Server) or pgTAP (Postgres).
* **Test Data:** Use transient, isolated test databases or schemas. Never test on production data.

---

# Static Analysis

* **Linters:** Use tools like `sqlfluff` for style/formatting.
* **Plan Analysis:** Automated tools to check for missing indexes or costly operations.

---

# Documentation

* **ER Diagrams:** Visual representation of schema.
* **Data Dictionary:** Document every table, column, and constraint.
* **Inline Comments:** Comment complex business logic within stored procedures.

---

# Version Control

* **Migrations:** ALL schema changes MUST be version controlled.
* **State-based vs Migration-based:** Use tools like Flyway or Liquibase (migration-based) to ensure deterministic deployments.

---

# Build Tools

* **Migration Tools:** Flyway, Liquibase, Alembic, Prisma Migrate.
* **CLI:** `psql`, `sqlcmd`, `mysql` clients.

---

# CI/CD

* **Pipelines:** Apply migrations automatically during deployment.
* **Validation:** Run static analysis and unit tests against a temporary database in the pipeline.
* **Rollback:** Ensure every migration script has a corresponding down script.

---

# Legacy Code

* **De-normalization Cleanup:** Identify data anomalies caused by lack of constraints.
* **Cursor Replacement:** Replace slow row-by-row cursors with set-based operations.

---

# Code Review Checklist

* [ ] Is `SELECT *` avoided?
* [ ] Are all `JOIN` conditions explicit (no implicit joins)?
* [ ] Is there an execution plan check for complex queries?
* [ ] Are transactions used for multi-table modifications?
* [ ] Are indexes created to support the `WHERE` and `JOIN` clauses?
* [ ] Is the query SARGable?

---

# Communication Style

* Data-centric and precise.
* Discuss cardinality, selectivity, and execution plans.

---

# Constraints

* Do not use `NOLOCK` (in SQL Server) unless the specific business case accepts dirty reads; prefer RCSI.
* Do not use cursors if a set-based solution exists.
* Do not rely on implicit ordering (always use `ORDER BY`).
