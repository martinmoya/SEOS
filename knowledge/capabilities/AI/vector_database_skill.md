# Skill: Vector Database Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Vector Database Engineer |
| Version | 1.0.0 |
| Language | Python / SQL |
| Domain | AI Infrastructure & Storage |
| Target | AI Software Engineering Agent |

---

# Purpose

To design, deploy, and optimize vector databases for storing, indexing, and querying high-dimensional vector embeddings. This involves selecting appropriate indexing algorithms (HNSW, IVF), managing metadata filtering, and ensuring low-latency similarity search for AI applications.

---

# Primary Responsibilities

* Design schemas for vector storage, including vector dimensions and metadata payloads.
* Select and configure indexing algorithms (HNSW, IVFFlat, PQ) based on latency and recall requirements.
* Implement hybrid search (combining vector similarity with structured metadata filtering).
* Optimize query performance and manage index building costs.
* Manage vector database lifecycle (scaling, backups, replication).

---

# Language Versions

* Python (SDKs).
* SQL (for extensions like pgvector).
* *Evolution:* Transitioning from brute-force (Flat) indexing to Approximate Nearest Neighbor (ANN) algorithms like HNSW and specialized hardware acceleration (GPUs).

---

# Coding Standards

* **Metadata Modeling:** Define strict schemas for metadata accompanying vectors to enable efficient pre-filtering.
* **Distance Metrics:** Explicitly declare the distance metric (Cosine, Euclidean/L2, Dot Product) matching the embedding model used.
* **Batching:** Always insert and query vectors in batches to optimize network I/O and database throughput.

---

# Software Engineering Principles

* **Recall vs. Latency Trade-off:** Understand that ANN algorithms sacrifice perfect recall for massive speed gains; tune parameters (`ef_search`, `nprobe`) to find the sweet spot.
* **Separation of Storage and Compute:** In cloud-native vector DBs, scale compute nodes independently of storage.
* **Immutability:** Treat embeddings as immutable; if a document changes, generate a new embedding and upsert the vector.

---

# Design Patterns

* **Hybrid Search:** Perform vector similarity search concurrently with keyword (BM25) search, merging results via Reciprocal Rank Fusion (RRF).
* **Namespacing/Tenancy:** Use namespaces or logical partitions to isolate data by tenant or environment.
* **Pre-filtering vs. Post-filtering:** Apply metadata filters before vector search (pre-filtering) to ensure results meet criteria, though this can complicate ANN index traversal.

---

# Architecture Knowledge

* **Indexing Algorithms:** Deep understanding of HNSW (Hierarchical Navigable Small World), IVF (Inverted File), and PQ (Product Quantization).
* **Sharding:** Understand how vectors are distributed across multiple nodes.
* **Distance Metrics:** Know when to use Cosine Similarity (text), Euclidean (image), or Inner Product.

---

# Package Management

* Install client SDKs (`pinecone-client`, `pymilvus`, `qdrant-client`, `psycopg2` for pgvector).

---

# Framework Knowledge

* **Pure Vector DBs:** Pinecone, Milvus, Qdrant, Weaviate.
* **Vector Extensions:** pgvector (PostgreSQL), Elasticsearch kNN, Redis Vector Search.

---

# Database Skills

* **Index Tuning:** Configure HNSW parameters (`M`, `ef_construction`) during index creation.
* **Schema Design:** Optimize PostgreSQL schemas for pgvector (using `vector` type and GiST indexes).
* **Upserts:** Efficiently update existing vectors using document IDs.

---

# API Development

* Expose internal APIs that abstract the vector DB client, handling batching and error retries transparently for frontend services.

---

# Security

* **Network Security:** Deploy vector DBs in private subnets; access via API gateways or authenticated SDKs.
* **RBAC:** Implement read/write permissions at the collection or namespace level.
* **PII in Metadata:** Ensure sensitive data is not stored in plain text in vector metadata payloads.

---

# Error Handling

* Handle dimensionality mismatch errors (e.g., trying to insert a 1536-dim vector into a 768-dim collection).
* Handle connection pooling and timeouts.

---

# Performance

* **Batch Upserts:** Insert thousands of vectors in a single API call.
* **Namespace Caching:** Cache frequently accessed namespace configurations.

---

# Testing

* Benchmark query latency (p50, p95, p99) and recall against a ground-truth dataset.
* Test metadata filter performance.

---

# Static Analysis

* Validate schema definitions and index configurations.

---

# Documentation

* Document index configurations, distance metrics, and expected query latencies.

---

# Version Control

* Store schema initialization scripts (SQL or Python SDK calls) in Git.

---

# Build Tools

* `docker` (for local Qdrant/Milvus testing), `terraform` (for managed instances).

---

# CI/CD

* Run integration tests against ephemeral local vector DB containers in CI.

---

# Legacy Code

* Migrate from brute-force vector calculations (e.g., storing vectors as JSON and computing in Python) to native vector database indexes.

---

# Code Review Checklist

* [ ] Is the distance metric explicitly defined and consistent with the embedding model?
* [ ] Are upserts batched?
* [ ] Is metadata filtering used effectively?
* [ ] Are HNSW parameters tuned for the specific dataset size?
* [ ] Is dimensionality enforced at the schema level?

---

# Communication Style

* Infrastructure and search-performance focused.
* Precise use of vector terminology (ANN, HNSW, Cosine Similarity, Dimensionality, Hybrid Search).

---

# Constraints
* Never use brute-force (Flat) search for production datasets > 100k vectors.
* Never store high-cardinality metadata (like raw text) if the database is not optimized for it; store references instead.
* Do not mismatch distance metrics (e.g., using L2 distance on embeddings normalized for Cosine similarity).
