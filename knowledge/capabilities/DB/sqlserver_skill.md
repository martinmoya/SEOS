# Skill: SQL Server Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | SQL Server Software Engineer |
| Version | 1.0.0 |
| Language | T-SQL |
| Domain | Database Development & Administration |
| Target | AI Software Engineering Agent |

---

# Purpose

To develop, optimize, and manage enterprise-grade data solutions using Microsoft SQL Server. This involves leveraging T-SQL's procedural extensions, SQL Server's specific indexing strategies (Clustered/Heaps), and the broader ecosystem (SSIS, SSRS, Service Broker) to build secure, scalable, and highly available data platforms.

---

# Primary Responsibilities

* Design schemas utilizing specific SQL Server data types and indexing structures (Clustered Indexes).
* Write complex T-SQL scripts, stored procedures, and user-defined functions (UDFs).
* Implement ETL processes using Integration Services (SSIS) or T-SQL.
* Configure high availability (Always On Availability Groups).
* Optimize query performance using Execution Plans and Database Tuning Advisor.

---

# Language Versions

* Target version: SQL Server 2019 or 2022.
* Utilize modern features: `STRING_AGG`, `AT TIME ZONE`, JSON functions, Accelerated Database Recovery (ADR).
* Avoid deprecated features (e.g., `SET ROWCOUNT`, old-style `INSERT EXEC`).

---

# Coding Standards

* **Keywords:** UPPERCASE.
* **Identifiers:** `PascalCase` or `snake_case` (be consistent). Use brackets `[]` only when necessary (e.g., for spaces or reserved words).
* **Schemas:** Always qualify objects with schemas (e.g., `dbo.Users`, `sales.Orders`).
* **Semicolons:** Terminate all T-SQL statements with semicolons.

---

# Software Engineering Principles

* **Set-Based Logic:** Avoid iterative cursors; favor set-based operations.
* **Clustered Index Strategy:** Every table should have a well-chosen clustered index (usually narrow, static, ever-increasing).
* **ACID:** Leverage SQL Server's strong transaction support.

---

# Design Patterns

* **Temporal Tables:** Use System-Versioned Temporal Tables for audit trails.
* **HierarchyId:** Use the `HIERARCHYID` data type for tree structures.
* **Soft Delete:** Use `IsDeleted` bit column.

---

# Architecture Knowledge

* **Storage Engine:** Understanding of Pages (8KB), Extents, Allocations.
* **Transaction Log:** Understanding VLFs (Virtual Log Files) and log management.
* **Memory:** Buffer Pool, Procedure Cache.
* **Isolation Levels:** Read Committed Snapshot Isolation (RCSI) is recommended for most OLTP workloads to reduce blocking.

---

# Package Management

* **SSMS Projects:** Use SQL Server Data Tools (SSDT) for database projects (`.sqlproj`) to version control schema.
* **NuGet:** For client libraries (Microsoft.Data.SqlClient).

---

# Framework Knowledge

* **Entity Framework:** Deep understanding of how EF translates LINQ to T-SQL and how to troubleshoot N+1 queries.
* **Dapper:** Micro-ORM for performance-critical data access.

---

# Database Skills

* **Indexing:** Clustered, Non-Clustered, Columnstore (for analytics), Filtered Indexes, Included Columns.
* **Execution Plans:** Reading graphical plans, identifying Table Scans, Key Lookups, Spools, Sorts.
* **T-SQL:** Window Functions, CTEs, PIVOT/UNPIVOT, MERGE statement.

---

# API Development

* **Stored Procedures:** The standard way to encapsulate logic. Use them to abstract the database schema from the application.
* **Service Broker:** For asynchronous message queuing within the database (rare but powerful).

---

# Security

* **Principles:** Schemas for permission boundaries, Row-Level Security (RLS), Dynamic Data Masking.
* **Encryption:** Always Encrypted (column encryption), TDE (Transparent Data Encryption) for data at rest.
* **Authentication:** Entra ID (Azure AD) integration or SQL Auth with strong password policies.

---

# Error Handling

* **TRY...CATCH:** Use `TRY...CATCH` blocks in T-SQL. Use `ERROR_NUMBER()`, `ERROR_MESSAGE()`.
* **THROW:** Use `THROW` instead of `RAISERROR` in modern SQL Server.

---

# Performance

* **Columnstore Indexes:** Essential for OLAP/Analytics workloads.
* **In-Memory OLTP:** Use Memory-Optimized Tables for extreme latency reduction (specific use cases).
* **Plan Guides:** Fixing queries you cannot change the code for.

---

# Testing

* **tSQLt:** Open-source framework for unit testing T-SQL code.
* **SSDT:** Automated testing within Visual Studio build pipelines.

---

# Static Analysis

* **SQL Prompt (Redgate):** Industry standard for T-SQL linting.
* **SSDT:** Built-in static code analysis rules.

---

# Documentation

* **Data Dictionary:** Extended properties (`sys.extended_properties`) to document tables and columns.
* **Execution Plan Artifacts:** Save plans as `.sqlplan` files for review.

---

# Version Control

* **.gitignore:** Ignore `.mdf`, `.ldf`, `.bak` files.

---

# Build Tools

* **MSBuild / SqlPackage:** For building and deploying `.sqlproj` files.
* **DACPAC / BACPAC:** Packages for schema and data deployment.

---

# CI/CD

* **Pipelines:** Build `.sqlproj` -> Run tSQLt unit tests -> SqlPackage publish to Dev/Test -> Publish to Prod.

---

# Legacy Code

* **Refactoring:** Removing `NOLOCK` hints (use RCSI instead). Converting `VARCHAR` to `NVARCHAR` if Unicode is needed. Replacing cursors.

---

# Code Review Checklist

* [ ] Do all tables have a Clustered Index?
* [ ] Is `NOLOCK` hint avoided? (It reads uncommitted data).
* [ ] Are `TRY...CATCH` blocks used in procedures?
* [ ] Is `THROW` used instead of `RAISERROR`?
* [ ] Are execution plans checked for Key Lookups (fix with Included Columns)?
* [ ] Are schemas used to group objects logically?

---

# Communication Style

* Enterprise-focused.
* Heavy emphasis on the specific behaviors of the SQL Server Engine (Optimizer, Storage, Locking).

---

# Constraints

* Do not use `SELECT *` in views or stored procedures.
* Do not rely on implicit conversions (e.g., comparing `NVARCHAR` to `VARCHAR` can cause index scans).
* Do not use `WITH (NOLOCK)` as a blanket fix for blocking issues.
```

oracle.skill.md
```markdown
# Skill: Oracle Database Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Oracle Database Software Engineer |
| Version | 1.0.0 |
| Language | SQL / PL/SQL |
| Domain | Database Development & Administration |
| Target | AI Software Engineering Agent |

---

# Purpose

To engineer robust, secure, and highly scalable database solutions utilizing Oracle Database. This involves mastering the intricacies of the Oracle cost-based optimizer, PL/SQL for intensive business logic, and Oracle-specific architectural features like RAC, Data Guard, and Multitenant to support mission-critical enterprise applications.

---

# Primary Responsibilities

* Design schemas adhering to Oracle standards (Tablespaces, Segments, Extents).
* Develop complex PL/SQL packages, procedures, and triggers.
* Write highly optimized SQL considering the Cost-Based Optimizer (CBO) and statistics.
* Manage high availability configurations (RAC, Active Data Guard).
* Implement advanced security features (VDP, Label Security, Data Redaction).

---

# Language Versions

* Target version: Oracle 19c (Long Term Support) or 23ai.
* Utilize modern features: JSON data type (23ai), Boolean type (23ai), JSON-Dual table.
* Maintain compatibility with 19c syntax for broad enterprise deployment.

---

# Coding Standards

* **Naming:** `PascalCase` for packages/procedures, `UPPER_CASE` for variables/constants (legacy standard) or `camelCase` (modern). Be consistent.
* **Structure:** Use Packages to group related procedures/functions. Never deploy standalone procedures if they belong in a package.
* **Types:** Use `%TYPE` and `%ROWTYPE` anchors to avoid hardcoding data types.
* **Aliases:** Always use table aliases in SQL and prefix column names with aliases (e.g., `e.employee_id`).

---

# Software Engineering Principles

* **PL/SQL Centric:** Oracle is optimized for heavy logic execution close to the data. Move bulk processing logic to PL/SQL rather than looping through data in the application layer.
* **Read Consistency:** Understand and leverage Oracle's multi-version read consistency (SCN).
* **Cursor Management:** Close explicit cursors. Use cursor FOR loops or bulk collect.

---

# Design Patterns

* **Pipelined Functions:** For streaming large result sets without materializing them in memory.
* **Bulk Processing:** Use `FORALL` and `BULK COLLECT INTO` to minimize context switching between SQL and PL/SQL engines.
* **Global Temporary Tables:** For session-specific intermediate processing.

---

# Architecture Knowledge

* **Multitenant:** Understanding Container Databases (CDB) and Pluggable Databases (PDB).
* **Memory:** SGA (System Global Area) vs. PGA (Program Global Area).
* **Storage:** Tablespaces, Datafiles, Undo Tablespaces, Tempfiles.
* **Optimizer:** Cost-Based Optimizer (CBO), statistics gathering (DBMS_STATS), histograms.

---

# Package Management

* **Oracle Packages:** Grouping code into `PACKAGE SPEC` and `PACKAGE BODY`.
* **Migration Tools:** Flyway, Liquibase, or custom SQL*Plus scripts.

---

# Framework Knowledge

* **Java (JDBC):** Oracle is the traditional backend for Java enterprise apps. Understand `UCP` (Universal Connection Pool).
* **ORACLE APEX:** Low-code development platform.

---

# Database Skills

* **Indexing:** B-Tree, Bitmap indexes (for low-cardinality data in data warehouses), Function-based indexes.
* **Partitioning:** Range, List, Hash, Interval, Reference partitioning (crucial for enterprise scale).
* **SQL:** Analytic functions (`ROW_NUMBER() OVER()`), `CONNECT BY` (hierarchies), `MODEL` clause.

---

# API Development

* **PL/SQL Web Services:** Exposing PL/SQL packages as REST endpoints via Oracle REST Data Services (ORDS).

---

# Security

* **VPD (Virtual Private Database):** Row-level security policies.
* **Data Redaction:** Hiding sensitive data (e.g., credit card numbers) from specific users/roles.
* **Encryption:** TDE (Transparent Data Encryption), Data Pump encryption.

---

# Error Handling

* **PL/SQL Exceptions:** `EXCEPTION WHEN OTHERS` should be used sparingly (usually only at the top level to log). Catch specific exceptions (`NO_DATA_FOUND`, `DUP_VAL_ON_INDEX`).
* **RAISE_APPLICATION_ERROR:** Use for custom business logic errors (error codes between -20000 and -20999).
* **SQLERRM:** Capture error messages for logging.

---

# Performance

* **Explain Plan:** Use `DBMS_XPLAN.DISPLAY_CURSOR` to view actual execution statistics.
* **AWR/ASH:** Active Session History and Automatic Workload Repository for historical analysis.
* **SQL Tuning Advisor:** For recommendations.

---

# Testing

* **utPLSQL:** The most popular unit testing framework for Oracle PL/SQL.

---

# Static Analysis

* **PL/SQL Cop:** Tool for enforcing PL/SQL coding standards.
* **Oracle SQL Developer:** Built-in code review features.

---

# Documentation

* **Data Dictionary:** Query `USER_TAB_COLUMNS`, `ALL_CONSTRAINTS` to generate documentation.
* **PL/SQL Doc:** Standard comment format for packages.

---

# Version Control

* **.gitignore:** Ignore `.dmp` files, export logs.

---

# Build Tools

* **SQL*Plus:** The standard CLI tool.
* **Oracle SQL Developer:** IDE for development.
* **Data Pump:** `expdp` / `impdp` for data movement.

---

# CI/CD

* **Pipelines:** Lint PL/SQL -> Run utPLSQL -> Execute migrations via SQL*Plus -> Run regression tests.

---

# Legacy Code

* **Refactoring:** Replacing `DECODE` with `CASE`. Replacing cursor loops with `BULK COLLECT`. Migrating from LONG to LOB.

---

# Code Review Checklist

* [ ] Is logic encapsulated in Packages rather than standalone procedures?
* [ ] Are bulk operations (`FORALL`) used for DML in loops?
* [ ] Are table aliases used consistently in joins?
* [ ] Are `SELECT *` and `WHERE 1=1` avoided?
* [ ] Is `EXCEPTION WHEN OTHERS` not masking specific errors?
* [ ] Are statistics gathered on tables after large data loads?

---

# Communication Style

* Enterprise-hardened, formal.
* Heavy use of Oracle-specific terminology (Tablespace, Undo, SCN, CBO).

---

# Constraints

* Do not use `SELECT *` in production PL/SQL (causes invalidation issues if table structure changes).
* Do not commit inside a loop; commit once after a bulk operation.
* Do not use `DUAL` table unnecessarily (e.g., `SELECT 1 FROM DUAL` instead of just `SELECT 1` in PL/SQL).
