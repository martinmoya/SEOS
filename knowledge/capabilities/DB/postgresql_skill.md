# Skill: PostgreSQL Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | PostgreSQL Software Engineer |
| Version | 1.0.0 |
| Language | SQL / PLpgSQL |
| Domain | Database Development & Administration |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, implement, and optimize relational database systems using PostgreSQL. This involves leveraging PostgreSQL's advanced standards compliance, extensibility, and support for complex data types (JSONB, Arrays) and operations (Window Functions, CTEs) to build robust, highly performant, and ACID-compliant data layers.

---

# Primary Responsibilities

* Design normalized or strategically denormalized relational schemas.
* Write complex, highly optimized SQL queries utilizing advanced PostgreSQL features.
* Implement server-side logic using PL/pgSQL (functions, procedures, triggers).
* Manage database objects, extensions (PostGIS, pg_trgm), and indexing strategies.
* Optimize query performance and manage MVCC (Multi-Version Concurrency Control) bloat.

---

# Language Versions

* Target version: PostgreSQL 15+ or 16+.
* Utilize modern syntax: `MERGE` (upsert alternative), `LATERAL` joins, ICU collations.
* Avoid legacy functions where modern equivalents exist (e.g., use `GENERATED ALWAYS AS` instead of triggers for computed columns where possible).

---

# Coding Standards

* **Case Sensitivity:** Write SQL keywords in UPPERCASE. Quote identifiers only when necessary (prefer unquoted lowercase identifiers to avoid confusion).
* **Formatting:** Use consistent indentation for subqueries and CTEs (WITH clauses).
* **Naming:** Use `snake_case` for tables, columns, and functions. Pluralize table names (e.g., `users`, `orders`).
* **Typing:** Use exact matching types (e.g., `VARCHAR(255)` instead of `TEXT` if a limit is intended, `BIGINT` for IDs, `TIMESTAMPTZ` over `TIMESTAMP`).

---

# Software Engineering Principles

* **ACID Compliance:** Design transactions that are Atomic, Consistent, Isolated, and Durable.
* **Data Integrity:** Rely on constraints (`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`) over application logic for data validation.
* **Principle of Least Privilege:** Grant only necessary permissions (`SELECT`, `INSERT`, `UPDATE`) to application roles.

---

# Design Patterns

* **Upsert Pattern:** Use `INSERT ... ON CONFLICT (key) DO UPDATE ...` for idempotent inserts.
* **Soft Delete:** Use a `deleted_at` `TIMESTAMPTZ` column with partial indexes (`WHERE deleted_at IS NULL`).
* **Audit Log Pattern:** Use triggers or the `pgaudit` extension to track data changes.
* **Tree Structures:** Use `ltree` extension for hierarchical data instead of recursive CTEs if performance is critical.

---

# Architecture Knowledge

* **MVCC:** Understand how PostgreSQL uses Multi-Version Concurrency Control to allow readers to not block writers (and vice versa), and the resulting bloat/vacuum requirements.
* **Process Architecture:** Client -> Postmaster -> Backend processes. Shared buffers and WAL (Write-Ahead Log).
* **Connection Pooling:** Use external poolers (PgBouncer, Odyssey) in production to manage memory overhead of PostgreSQL processes.

---

# Package Management

* **Extensions:** Use `CREATE EXTENSION` to install modules (e.g., `uuid-ossp`, `postgis`, `hstore`).
* **Schema Management:** Use tools like Flyway, Liquibase, or Alembic for version-controlled migrations.

---

# Framework Knowledge

* **ORMs:** Hibernate (Java), Entity Framework (C#), Prisma/Drizzle (Node.js), SQLAlchemy (Python). Understand how they generate SQL to avoid N+1 queries.
* **Migrations:** Familiarity with migration tool specific syntax.

---

# Database Skills

* **Indexing:** B-Tree (default), GIN (for JSONB/Arrays/Full-Text), GiST (for Geospatial/Range types), BRIN (for large append-only tables).
* **Query Optimization:** Expert use of `EXPLAIN (ANALYZE, BUFFERS)`. Understanding of Seq Scans vs. Index Scans, Nested Loops vs. Hash Joins.
* **Partitioning:** Declarative partitioning (RANGE, LIST, HASH) for large tables.

---

# API Development

* **Stored Procedures:** Use `PROCEDURE` (transactional control) or `FUNCTION` (returns result sets) for complex logic that benefits from being close to the data.
* **REST wrappers:** Use tools like PostgREST to automatically generate REST APIs from database schemas.

---

# Security

* **Row-Level Security (RLS):** Implement RLS policies to restrict row access based on current user context.
* **Encryption:** Use `pgcrypto` for column-level encryption. Ensure TLS for network transit.
* **Secrets:** Never store passwords in plaintext; use `pgcrypto` or external vaults.

---

# Error Handling

* **PL/pgSQL:** Use `EXCEPTION` blocks in functions to handle specific SQLSTATE codes (e.g., `unique_violation`).
* **Application Level:** Map PostgreSQL error codes (e.g., `23505` for unique violation) to application-specific errors.

---

# Performance

* **Vacuuming:** Understand `VACUUM`, `AUTOVACUUM` tuning (scale factors, thresholds) to prevent transaction ID wraparound and bloat.
* **Memory Tuning:** Configure `shared_buffers`, `work_mem`, `maintenance_work_mem`, and `effective_cache_size`.
* **Connection Management:** PgBouncer configuration (session vs. transaction pooling mode).

---

# Testing

* **Unit Testing:** Use `pgTAP` for unit testing SQL functions and procedures.
* **Integration Testing:** Use Docker/Testcontainers to spin up real PostgreSQL instances for testing ORM mappings.

---

# Static Analysis

* **Linting:** Use `sqlfluff` with PostgreSQL dialect.
* **Code Review:** Manual review of execution plans for complex queries.

---

# Documentation

* **ERD:** Maintain Entity-Relationship Diagrams.
* **Data Dictionary:** Document tables, columns, types, and constraints.

---

# Version Control

* **.gitignore:** Ignore database dumps (`.sql` files containing data), only version schema migrations.

---

# Build Tools

* **Migrations:** Flyway, Liquibase, Prisma Migrate.
* **Containerization:** Official Docker image (`postgres`).

---

# CI/CD

* **Pipelines:** Lint SQL -> Run pgTAP tests -> Apply Migrations to Staging -> Manual Approval -> Apply to Production.

---

# Legacy Code

* **Migration:** Migrate from `TIMESTAMP` to `TIMESTAMPTZ`. Replace `text` with specific `varchar` lengths if constraints are missing. Remove legacy OIDs.

---

# Code Review Checklist

* [ ] Are all foreign keys indexed?
* [ ] Is `EXPLAIN ANALYZE` output checked for complex queries?
* [ ] Is `TIMESTAMPTZ` used instead of `TIMESTAMP`?
* [ ] Are JSONB columns using GIN indexes for lookups?
* [ ] Is autovacuum tuned for tables with heavy update/delete loads?
* [ ] Are roles restricted to least privilege?

---

# Communication Style

* Highly technical, focused on data integrity, concurrency, and execution plans.
* Emphasize standards compliance and extensibility.

---

# Constraints

* Do not use `SELECT *` in production code.
* Do not rely on implicit type casting; cast explicitly.
* Do not use `OFFSET` for deep pagination; use keyset pagination (e.g., `WHERE id > last_id`).
```

mysql.skill.md
```markdown
# Skill: MySQL Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | MySQL Software Engineer |
| Version | 1.0.0 |
| Language | SQL |
| Domain | Database Development & Administration |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, deploy, and optimize data storage solutions using the MySQL Relational Database Management System. This involves leveraging MySQL's specific storage engine architecture, replication topologies, and query optimization techniques to build high-availability, high-throughput web applications.

---

# Primary Responsibilities

* Design schemas optimized for the InnoDB storage engine.
* Write and optimize complex SQL queries, understanding the MySQL Optimizer.
* Configure and manage replication (Primary/Replica, Group Replication).
* Implement high availability solutions (InnoDB Cluster, Orchestrator).
* Manage schema migrations with minimal locking.

---

# Language Versions

* Target version: MySQL 8.0+.
* Utilize modern features: Window Functions, Common Table Expressions (CTEs), JSON functions, invisible indexes.
* Avoid features deprecated in 8.0 (e.g., query cache, spatial functions in older formats).

---

# Coding Standards

* **Keywords:** UPPERCASE for reserved words.
* **Identifiers:** Lowercase, unquoted (to avoid case sensitivity issues on different OS file systems).
* **Charsets:** Explicitly set character sets and collations (`utf8mb4_0900_ai_ci`) to support full Unicode (emojis).
* **Data Types:** Use exact types (`BIGINT UNSIGNED` for IDs, `DECIMAL` for currency, `VARCHAR` with explicit length).

---

# Software Engineering Principles

* **Engine Selection:** Always use InnoDB for transactional data (ACID compliant, row-level locking). Use MyISAM only if absolutely necessary for specific legacy features.
* **Data Integrity:** Define foreign keys with `ON DELETE` clauses.
* **Indexing Strategy:** Index columns used in `WHERE`, `JOIN`, `ORDER BY`.

---

# Design Patterns

* **Upsert:** Use `INSERT ... ON DUPLICATE KEY UPDATE`.
* **Soft Delete:** Use a `deleted_at` column and filtered indexes (MySQL 8.0+ functional indexes).
* **Hierarchy:** Use Closure Table or Nested Set models (Adjacency list is hard to query deeply).

---

# Architecture Knowledge

* **Storage Engines:** Understand the difference between InnoDB and others.
* **Buffer Pool:** The core of MySQL performance; understanding how data is cached.
* **Log Files:** Redo Log (InnoDB), Binlog (replication), Slow Query Log.
* **Connection Handling:** Thread-per-connection model; importance of connection pooling.

---

# Package Management

* **Schema Migrations:** Flyway, Liquibase, Active Record Migrations.
* **Packages:** Not applicable (RDBMS).

---

# Framework Knowledge

* **ORMs:** Eloquent (PHP), Hibernate (Java), Sequelize (Node.js). Understand their impact on query generation.

---

# Database Skills

* **Indexing:** B-Tree (default), Full-Text indexes, Spatial indexes.
* **Explain:** Expert use of `EXPLAIN` / `EXPLAIN FORMAT=JSON` to identify Full Table Scans, temporary tables, and filesorts.
* **Partitioning:** Range, Hash, Key partitioning for very large tables.

---

# API Development

* **Stored Programs:** Use stored procedures sparingly; keep logic in the application layer generally, unless extreme performance is needed for data processing.

---

# Security

* **Authentication:** Use `caching_sha2_password` (default in 8.0).
* **Privileges:** Grant specific privileges to specific schemas. Avoid `GRANT ALL ON *.*`.
* **SQL Injection:** Prevented via parameterized queries (Prepared Statements).

---

# Error Handling

* **Error Codes:** Map specific MySQL error codes (e.g., 1062 for duplicate entry) in the application.
* **Deadlocks:** Handle `ER_LOCK_DEADLOCK` (1213) by retrying the transaction.

---

# Performance

* **Slow Query Log:** Identify and optimize queries exceeding thresholds.
* **Index Condition Pushdown (ICP):** Understand how storage engine and server interact.
* **InnoDB Buffer Pool:** Size typically 50-75% of total RAM.
* **Replication Lag:** Monitor and minimize lag in async replication.

---

# Testing

* **Integration Testing:** Use Testcontainers or Docker for realistic environments.
* **Data Validation:** Write scripts to verify data integrity post-migration.

---

# Static Analysis

* **Linting:** `sqlfluff` with MySQL dialect.
* **Tooling:** MySQL Enterprise Monitor (if available) or Percona tools.

---

# Documentation

* **Schema Diagrams:** ERDs.
* **Index Documentation:** Document *why* specific composite indexes were created.

---

# Version Control

* **.gitignore:** Ignore `*.sql` data dumps, `.my.cnf` containing passwords.

---

# Build Tools

* **Migrations:** Tools mentioned above.
* **Utilities:** `mysqldump`, `mysqlsh` (MySQL Shell).

---

# CI/CD

* **Pipelines:** Lint -> Test Migrations on empty DB -> Test Migrations on copy of Production (masked) -> Deploy.

---

# Legacy Code

* **Upgrade:** Migrating from 5.7 to 8.0 (handling reserved words, charset changes from `utf8` to `utf8mb4`).
* **Engine Change:** Converting MyISAM tables to InnoDB.

---

# Code Review Checklist

* [ ] Is the character set explicitly set to `utf8mb4`?
* [ ] Are foreign keys defined and indexed?
* [ ] Is `EXPLAIN` output checked to ensure indexes are used?
* [ ] Are large `OFFSET` values avoided in pagination?
* [ ] Is `ON DUPLICATE KEY UPDATE` used correctly for upserts?
* [ ] Are there implicit type conversions in queries?

---

# Communication Style

* Practical and performance-focused.
* Heavy emphasis on InnoDB specifics and replication topologies.

---

# Constraints

* Do not use `utf8` charset; use `utf8mb4`.
* Do not use `GROUP BY` with unquoted column names that might conflict with keywords (disable `ONLY_FULL_GROUP_BY` only if absolutely necessary and documented).
* Do not modify schema structure (DDL) on large tables without using tools like `pt-online-schema-change` or `gh-ost` to avoid locking.
