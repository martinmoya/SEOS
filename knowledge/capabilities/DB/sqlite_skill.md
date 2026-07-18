# Skill: SQLite Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | SQLite Software Engineer |
| Version | 1.0.0 |
| Language: SQL |
| Domain: Embedded Database |
| Target: AI Software Engineering Agent |

---

# Purpose

To effectively utilize SQLite as a lightweight, serverless, self-contained database engine embedded directly into applications. This involves understanding its unique file-locking concurrency model, type affinity system, and optimization techniques to build reliable local storage solutions for mobile, desktop, and edge computing applications.

---

# Primary Responsibilities

* Design schemas optimized for local/edge storage (often denormalized for read speed).
* Manage database connections and transaction lifecycles correctly.
* Optimize queries for embedded hardware constraints (mobile devices).
* Handle schema migrations safely without data loss.
* Implement data synchronization strategies (if applicable) with a backend server.

---

# Language Versions

* Target version: SQLite 3.x (latest stable series).
* Utilize modern features: Window Functions, CTEs, `UPSERT` (`INSERT ... ON CONFLICT`), JSON1 extension.
* Avoid legacy behaviors (e.g., `ALTER TABLE DROP COLUMN` is supported now).

---

# Coding Standards

* **File Location:** Store database files in application-specific directories (not shared locations).
* **Connections:** Keep connections open for the lifetime of the application if possible, but ensure they are closed properly on exit.
* **Types:** While SQLite is dynamically typed, define columns with standard SQL types (`INTEGER`, `TEXT`, `REAL`) to guide the application.

---

# Software Engineering Principles

* **Serverless Reality:** Understand there is no network layer; latency is pure disk I/O.
* **File Locking:** Understand that writes lock the entire database file (unless in WAL mode).
* **Data Gravity:** The database is a file; moving it moves the data.

---

# Design Patterns

* **WAL Mode:** Enable `PRAGMA journal_mode=WAL;` to allow simultaneous readers and one writer (critical for responsive UIs).
* **Upsert:** Use `ON CONFLICT DO UPDATE` for local caching of server data.
* **Normalization vs. Denormalization:** Often denormalize slightly in SQLite to reduce JOINs (disk seeks) on slow mobile storage.

---

# Architecture Knowledge

* **Storage:** Single disk file. Pages (usually 4KB).
* **Locking:** `SHARED` (read), `RESERVED`, `PENDING`, `EXCLUSIVE` (write).
* **Journaling:** ROLLBACK journal (default) vs. WAL (Write-Ahead Logging).
* **Type Affinity:** Rules for storing different type classes in the 5 storage classes (NULL, INTEGER, REAL, TEXT, BLOB).

---

# Package Management

* **Drivers:** `sqlite3` (Python), `System.Data.SQLite` (C#), `FMDB`/`GRDB` (iOS), `Room`/`sqlcipher` (Android).
* **Extensions:** Load extensions like `JSON1`, `FTS5` (Full Text Search).

---

# Framework Knowledge

* **Room (Android):** Abstraction over SQLite.
* **Core Data (iOS):** Wrapper (though SQLite is often used alongside).
* **Entity Framework Core:** Supports SQLite provider.

---

# Database Skills

* **Indexes:** Crucial for performance, especially on unindexed foreign keys.
* **Explain Query Plan:** Use `EXPLAIN QUERY PLAN` to ensure indexes are used.
* **FTS5:** Implement fast, offline full-text search.
* **JSON1:** Store and query JSON documents.

---

# API Development

* **N/A:** SQLite is an embedded library, not a server. It has no network API.

---

# Security

* **SQL Injection:** Prevented via parameterized queries (even though it's local, it's a good habit and prevents crashes
