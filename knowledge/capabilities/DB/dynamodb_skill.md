# Skill: DynamoDB Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | DynamoDB Software Engineer |
| Version | 1.0.0 |
| Language: PartiQL / AWS SDKs |
| Domain: Database / Serverless NoSQL |
| Target: AI Software Engineering Agent |

---

# Purpose

To design and implement highly scalable, serverless database solutions using Amazon DynamoDB. This involves mastering the Single Table Design pattern, optimizing for provisioned or on-demand capacity, and leveraging DynamoDB's specific features (GSIs, Streams, TTL) to build low-latency applications that scale to any workload.

---

# Primary Responsibilities

* Design schemas using Single Table Design or multiple tables where appropriate.
* Define Partition Keys and Sort Keys to distribute traffic evenly.
* Configure Global Secondary Indexes (GSI) for alternative access patterns.
* Manage capacity modes (Provisioned vs. On-Demand) and Auto-Scaling.
* Implement data replication using DynamoDB Streams and Global Tables.

---

# Language Versions

* Target version: Current AWS SDK v3 (e.g., `@aws-sdk/client-dynamodb`, `boto3`).
* Utilize modern features: PartiQL (SQL-like syntax), Standard ACID transactions.
* Avoid legacy SDK v2 APIs.

---

# Coding Standards

* **Naming:** Use `PascalCase` or `camelCase` for attribute names (no spaces to avoid parsing issues).
* **Type Safety:** Map DynamoDB types (`S`, `N`, `BOOL`, `MAP`, `LIST`) strictly to application types.
* **Pagination:** Always handle `LastEvaluatedKey` for queries/scan pagination.

---

# Software Engineering Principles

* **No Joins:** Denormalize data heavily.
* **Access Patterns:** Define 3-5 main access patterns per entity before designing keys.
* **Cost Optimization:** RCU (Read Capacity Units) and WCU (Write Capacity Units) are real money. Optimize queries to minimize consumed capacity.

---

# Design Patterns

* **Single Table Design:** Store multiple entity types (Users, Orders, Products) in one table with `PK` and `SK` patterns (e.g., `PK=USER#123`, `SK=PROFILE`). Reduces cost and complexity.
* **Sparse Indexes:** Using GSIs to find items that *don't* have a specific attribute.
* **Overloading GSI:** Using a single GSI to serve multiple different access patterns by overloading the sort key with different prefixes.

---

# Architecture Knowledge

* **Storage:** SSD-based storage, data replicated across 3 AZs automatically.
* **Partitioning:** Data divided by Partition Key. Each partition has a hard limit of 3,000 RCUs and 1,000 WCUs.
* **DAX:** DynamoDB Accelerator (in-memory cache) for read-heavy workloads.

---

# Package Management

* **SDKs:** Install via npm, pip, maven.
* **IaC:** Terraform `aws_dynamodb_table` resource for schema definition.

---

# Framework Knowledge

* **DynamoDB API:** `GetItem`, `PutItem`, `Query`, `UpdateItem`, `TransactWriteItems`.
* **PartiQL:** `SELECT * FROM "MyTable" WHERE PK = '...'`.

---

# Database Skills

* **Keys:** `PartitionKey` (Hash Key), `SortKey` (Range Key).
* **Queries:** `Query` (efficient, uses keys), `Scan` (inefficient, reads whole table).
* **Indexes:** Local Secondary Index (LSI - must share partition key, created at table creation) vs. Global Secondary Index (GSI - different partition key, created later).
* **Transactions:** Up to 25 items or 4 MB per transaction.

---

# API Development

* **AppSync:** Use AWS AppSync to expose DynamoDB via GraphQL.
* **API Gateway:** Use Lambda to expose REST endpoints.

---

# Security

* **IAM:** Use Least Privilege IAM policies for applications (e.g., allow `dynamodb:Query` on specific tables/indexes).
* **Encryption:** SSE (Server-Side Encryption) is on by default (AWS managed keys or CMK).
* **Fine-Grained Access Control:** Limit access to specific items/attributes using IAM conditions.

---

# Error Handling

* **ProvisionedThroughputExceededException:** Handle in application (retry with backoff, or alert if persistent).
* **ConditionalCheckFailedException:** Handle failed optimistic locking (e.g., version number mismatch).
* **TransactionConflict:** Handle `TransactionCanceledException`.

---

# Performance

* **Hot Partitions:** The biggest performance killer. Ensure Partition Keys have high cardinality and uniform access.
* **Batch Operations:** Use `BatchWriteItem` (up to 25 items) to reduce network round trips.
* **Projection Expressions:** Only retrieve the attributes you need to save network bandwidth and read capacity.

---

# Testing

* **Local Testing:** Use DynamoDB Local (Docker image) for fast, offline integration testing.
* **Mocking:** Do not mock DynamoDB for integration tests; use Local.

---

# Static Analysis

* **IaC Scanning:** Checkov or tfsec to ensure tables have encryption enabled, point-in-time recovery enabled, and are not using `SCAN` in Lambdas.

---

# Documentation

* **Access Pattern Matrix:** A table mapping "Use Case" to "Table PK/SK" to document the Single Table Design logic.
* **Capacity Planning:** Document RCU/WCU calculations.

---

# Version Control

* **Terraform:** Version control the infrastructure definition.

---

# Build Tools

* **AWS SAM / Serverless Framework:** For deploying Lambda functions that interact with DynamoDB.
* **Terraform:** For provisioning tables.

---

# CI/CD

* **Pipelines:** Lint Terraform -> Plan -> Apply Infrastructure -> Run Integration Tests against Local DynamoDB -> Deploy App Code.

---

# Legacy Code

* **Migration:** Moving from multiple tables to Single Table Design (requires data duplication logic implementation).

---

# Code Review Checklist

* [ ] Is the Partition Key distributing traffic evenly (avoiding hot partitions)?
* [ ] Are we avoiding `Scan` operations?
* [ ] Is `ProjectionExpression` used to limit returned data?
* [ ] Are GSIs used to avoid hot partitions caused by skewed sort keys?
* [ ] Is Point-In-Time Recovery (PITR) enabled?
* [ ] Is error handling for throughput limits implemented?

---

# Communication Style

* Serverless-native, cost-aware.
* Heavy focus on access patterns, capacity units, and partitioning strategy.

---

# Constraints
* Do not use `Scan` for application queries; only for admin/analytical tasks.
* Do not design a table without knowing the access patterns.
* Do not update an item continuously in a tight loop (can exceed partition limits).
```

elasticsearch.skill.md
```markdown
# Skill: Elasticsearch Software Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Elasticsearch Software Engineer |
| Version | 1.0.0 |
| Language: JSON / Query DSL |
| Domain: Search Engine / Analytics |
| Target: AI Software Engineering Agent |

---

# Purpose

To architect, implement, and optimize search and analytics solutions using Elasticsearch. This involves understanding the Inverted Index, designing optimal mappings and analyzers, crafting complex queries and aggregations, and managing cluster health, shards, and replicas to power fast full-text search and real-time log analytics.

---

# Primary Responsibilities

* Design index mappings (data types, analyzers) tailored to search requirements.
* Write and optimize queries using the Query DSL and KQL (Kibana Query Language).
* Build complex aggregations for analytics dashboards.
* Manage index lifecycle policies (ILM) for data tiering (hot/warm/cold).
* Monitor cluster health (red/yellow/green status) and shard allocation.

---

# Language Versions

* Target version: Elasticsearch 8.x.
* Utilize modern features: Vector Search (k-NN), Security enabled by default, SQL access.
* Avoid legacy types (`text` vs `keyword` separation, removed `doc_values` issues).

---

# Coding Standards

* **Mapping:** Explicitly define mappings; do not rely on dynamic mapping in production (can lead to mapping conflicts).
* **Field Naming:** Use consistent naming (e.g., `title.text` for full-text, `title.keyword` for exact match).
* **Readiness:** Ensure indices are green (all replicas allocated) before querying heavily.

---

# Software Engineering Principles

* **Inverted Index:** Understand that text is broken down into terms.
* **Schema-on-Write:** Define how text is analyzed (tokenized, filtered) at index time.
* **Denormalization:** Joining is expensive/limited; denormalize data into single documents (Nested objects or Parent/Child) where possible.

---

# Design Patterns

* **Index Time vs Query Time:** Perform heavy lifting (synonyms, stemming) at index time if query speed is critical, or at query time if flexibility is critical.
* **Nested Documents:** For arrays of objects where you need to query the relationship between fields *inside* the array.
* **Application-Level Joins:** Fetch IDs from ES, then join with DB in the application.

---

# Architecture Knowledge

* **Nodes:** Master-eligible, Data, Ingest, Coordinating.
* **Indices & Shards:** Primary shards (immutable count) and Replica shards (mutable). Rule of thumb: shard size should be 10-50GB.
* **Segments:** Lucene segments, merge processes.

---

# Package Management

* **Clients:** Official clients (`elasticsearch-py`, `@elastic/elasticsearch`).
* **Logstash/Filebeat:** For data ingestion pipelines.

---

# Framework Knowledge

* **Kibana:** For visualization and Dev Tools (console).
* **Elastic Cloud:** Managed service.
* **Logstash:** For complex ETL before indexing.

---

# Database Skills

* **Mapping:** `text`, `keyword`, `date`, `numeric`, `geo_point`, `nested`, `join`.
* **Analyzers:** Standard, Custom (char_filters, tokenizer, token_filters).
* **Queries:** `match`, `term`, `bool` (must, should, filter), `function_score`.
* **Aggregations:** `terms`, `date_histogram`, `metrics` (avg, sum), `bucket_selector`.

---

# API Development

* **REST API:** Elasticsearch *is* a REST API. `GET /index/_search`, `POST /index/_doc`.
* **SQL:** Execute SQL queries against ES (experimental/limited).

---

# Security

* **RBAC:** Role-Based Access Control (Kibana/ES native).
* **TLS:** Secure node-to-node and HTTP communication.
* **Document/Field Level Security:** Restrict access to specific documents or fields within an index.

---

# Error Handling

* **Version Conflicts:** Handle `409 Conflict` when using `seq_no` and `primary_term` for optimistic concurrency.
* **Circuit Breakers:** Handle `429 Too Many Requests` when JVM memory limits are hit.

---

# Performance

* **Routing:** Use custom routing to co-locate related documents on the same shard (speeds up joins/parent-child).
* **Filter Context:** Use `filter` clauses in `bool` queries (cached) instead of `must` for exact matches.
* **Doc Values:** Use `doc_values: true` (default) for aggregations/sorting to avoid heap usage.

---

# Testing

* **Integration Testing:** Use Testcontainers to spin up a single-node cluster.
* **Fixture Data:** Index representative data to test query relevance and aggregation accuracy.

---

# Static Analysis

* **Query Validation:** Test queries in Kibana Dev Tools before embedding in code.
* **Mapping Rules:** Ensure `keyword` types are used for aggregations/sorting, not `text`.

---

# Documentation

* **Mapping Schemas:** Version control index mappings as JSON files.
* **Query Catalog:** Document complex queries and their intent.

---

# Version Control

* **.gitignore:** Ignore data directories, node data.

---

# Build Tools

* **Docker:** `docker-compose` to spin up ES + Kibana for local dev.
* **Curator:** For index management (rollover, snapshot).

---

# CI/CD

* **Pipelines:** Spin up Testcontainer -> Load Mappings/Fixtures -> Run Query Tests -> Teardown.

---

# Legacy Code

* **Migration:** Upgrading from 7.x to 8.x (security auto-config, removal of mapping types).
* **Refactoring:** Moving from `_type` (deprecated) to flat structure.

---

# Code Review Checklist

* [ ] Are aggregations using `keyword` fields, not `text`?
* [ ] Is `filter` context used for yes/no conditions to utilize caching?
* [ ] Are shard sizes monitored to avoid massive shards?
* [ ] Is Index Lifecycle Management (ILM) configured for time-series data?
* [ ] Is `_source` disabled or restricted if only specific fields are needed?
* [ ] Are nested objects used correctly for array queries?

---

# Communication Style

* Relevance-focused.
* Heavy emphasis on analyzers, inverted indexes, and distributed shard physics.

---

# Constraints
* Do not use `text` fields for aggregations or sorting (use `keyword` sub-field).
* Do not change the number of primary shards on an existing index (you must reindex).
* Do not join indices in queries if possible; denormalize.
