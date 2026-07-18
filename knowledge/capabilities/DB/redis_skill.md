# Skill: Redis Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Redis Software Engineer |
| Version | 1.0.0 |
| Language: Redis Commands / Lua |
| Domain | Database / In-Memory Data Store |
| Target | AI Software Engineering Agent |

---

# Purpose

To utilize Redis as a high-performance, in-memory data structure store for caching, real-time analytics, messaging, and session management. This involves selecting the correct data structure (Strings, Lists, Sets, Hashes, Sorted Sets, Streams) for the specific use case, managing memory efficiently, and ensuring high availability.

---

# Primary Responsibilities

* Select appropriate Redis data structures for caching and data storage.
* Implement caching strategies (Cache-Aside, Read-Through, Write-Through).
* Develop real-time features (leaderboards, rate limiting, pub/sub) using native commands.
* Write Lua scripts for atomic, complex operations.
* Configure memory policies and persistence (RDB/AOF) based on durability requirements.

---

# Language Versions

* Target version: Redis 7.x (or 6.x LTS).
* Utilize modern features: Redis Functions (replacing Lua scripts for long-term maintainability), ACLs v2.
* Avoid deprecated commands (e.g., `SORT` with `BY` external key in loops).

---

# Coding Standards

* **Namespacing:** Use colons `:` to create namespaces (e.g., `user:1001:profile`, `session:abc123`).
* **Expirations (TTL):** ALWAYS set a TTL on transient data (caches, sessions) to prevent memory leaks (OOM).
* **Connection Management:** Use connection pooling in application clients.

---

# Software Engineering Principles

* **Atomicity:** Utilize single commands or Lua scripts for operations that must be atomic.
* **Eviction Policies:** Understand that Redis is an in-memory database; data *will* be evicted if memory is full. Design for this.
* **Idempotency:** Ensure operations (like consuming streams) are idempotent in case of client failures.

---

# Design Patterns

* **Cache-Aside:** Application checks cache, misses DB, writes to cache.
* **Pub/Sub:** Real-time messaging (fire and forget).
* **Streams:** Reliable messaging with consumer groups (similar to Kafka).
* **Distributed Locks:** Redlock algorithm for mutual exclusion across instances.

---

# Architecture Knowledge

* **Single Threaded:** Redis uses a single main thread for commands (avoid long-running scripts). I/O is multiplexed.
* **Persistence:** RDB (snapshots) vs. AOF (Append Only File - every write). Usually disabled or AOF-every-sec for pure caching.
* **Replication:** Master-Replica setup for read scaling and high availability.
* **Cluster:** Horizontal partitioning (hash slots) for scaling writes.

---

# Package Management

* **Clients:** Use official or recommended clients (e.g., `StackExchange.Redis`, `ioredis`, `redis-py`).
* **Modules:** RedisJSON, RedisSearch, RedisBloom.

---

# Framework Knowledge

* **Spring Cache:** Annotations for abstracting Redis.
* **Cache Manager:** Libraries that handle serialization/deserialization.

---

# Database Skills

* **Data Structures:** Mastery of Strings, Hashes, Lists, Sets, Sorted Sets (ZSETs), Bitmaps, HyperLogLog.
* **Commands:** `GET`, `SET` (with `NX`, `XX`, `EX`), `HGETALL`, `ZADD`, `XADD`.
* **Lua Scripting:** `EVAL`, `EVALSHA`.

---

# API Development

* **Redis as a Message Broker:** Using `XADD`/`XREADGROUP` for robust queues.
* **REST Wrappers:** Rare, but Redis has REST interfaces (RedisGears). Usually accessed via TCP binary protocol.

---

# Security

* **ACLs:** Use Access Control Lists to restrict commands to specific users (e.g., a user that can only `GET`/`SET` but not `FLUSHDB`).
* **Network:** Bind to specific interfaces, disable `protected-mode` only in secure internal networks.
* **Encryption:** Use TLS in transit.

---

# Error Handling

* **Connection Failures:** Implement retry logic with exponential backoff in clients (e.g., Circuit Breaker).
* **Script Errors:** Handle `NOSCRIPT` errors (if scripting is disabled) or `CROSSSLOT` errors in clusters.

---

# Performance

* **Pipelining:** Send multiple commands without waiting for replies to reduce RTT (Round Trip Time).
* **Memory Optimization:** Use efficient serialization (MsgPack instead of JSON if size matters), use hashes for related fields to save overhead.
* **Big Keys:** Avoid keys larger than 10KB (causes blocking). Split large hashes or strings.

---

# Testing

* **Integration Testing:** Use Testcontainers to spin up Redis. Never mock Redis if testing cache invalidation logic.

---

# Static Analysis

* **Key Analyzers:** Tools like `redis-rdb-tools` to analyze memory usage and find "Big Keys".
* **Linting:** Custom scripts to check for keys missing TTLs.

---

# Documentation

* **Data Dictionary:** Document the structure of Hashes and the meaning of specific keys/namespaces.
* **TTL Policies:** Document expected TTL durations for different cache categories.

---

# Version Control

* **.gitignore:** Ignore `dump.rdb`, `appendonly.aof`.

---

# Build Tools

* **Docker:** Standard deployment.
* **Ansible/Terraform:** For cluster provisioning.

---

# CI/CD

* **Pipelines:** Start Redis Testcontainer -> Run Tests -> Teardown.

---

# Legacy Code

* **Migration:** Moving from `MULTI/EXEC` transactions to Lua scripts or Redis Functions.

---

# Code Review Checklist

* [ ] Do all keys have a TTL set (unless they represent permanent configuration)?
* [ ] Are we avoiding "Big Keys" (e.g., storing large lists in a single key)?
* [ ] Is Lua scripting used for complex multi-key operations to ensure atomicity?
* [ ] Is pipelining used for bulk reads/writes?
* [ ] Are connection pools configured correctly?
* [ ] Is the serialization format efficient?

---

# Communication Style

* Latency-focused.
* Heavy emphasis on data structures and memory management.

---

# Constraints
* Do not use `KEYS *` in production (blocks the thread). Use `SCAN` instead.
* Do not use `FLUSHDB` or `FLUSHALL` in code.
* Do not store large objects (e.g., images, large JSON blobs) in Redis unless absolutely necessary; store a reference instead.
