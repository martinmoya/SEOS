# Skill: Retrieval-Augmented Generation (RAG) Engineer

## Metadata

| Field | Value |
|--------|-------|
| Name | Retrieval-Augmented Generation (RAG) Engineer |
| Version | 1.0.0 |
| Language | Python / TypeScript |
| Domain | AI Engineering & Knowledge Management |
| Target | AI Software Engineering Agent |

---

# Purpose

To build accurate, grounded, and hallucination-free AI systems by connecting Large Language Models to external, proprietary knowledge bases. This involves orchestrating document ingestion, chunking, embedding, retrieval, and prompt augmentation to provide context-aware responses.

---

# Primary Responsibilities

* Implement document ingestion pipelines (PDF, HTML, Markdown, DB rows).
* Apply text splitting/chunking strategies (recursive, semantic, fixed-size).
* Integrate vector databases and retrieval algorithms (semantic, hybrid, keyword).
* Construct dynamic prompts that inject retrieved context.
* Evaluate and optimize RAG pipelines (retrieval recall, generation fidelity).

---

# Language Versions

* Python 3.10+ / TypeScript 5+.
* *Evolution:* Transitioning from naive semantic search (RAG 1.0) to advanced patterns like Hybrid Search, Re-ranking, RAG-Fusion, and GraphRAG.

---

# Coding Standards

* **Modular Pipelines:** Separate ingestion (load, split, embed, store) from retrieval (query, embed, search, augment).
* **Metadata Attachment:** Attach rich metadata (source, page number, date) to chunks during ingestion to enable pre-filtering during retrieval.
* **Configuration:** Parameterize chunk sizes (`chunk_size`, `chunk_overlap`) and retrieval limits (`top_k`).

---

# Software Engineering Principles

* **Grounding:** Ensure LLM responses are strictly derived from the retrieved context; instruct the model to say "I don't know" if context is insufficient.
* **Decoupling:** Separate the retrieval mechanism from the LLM generation step to allow independent tuning.
* **Idempotent Ingestion:** Ensure re-ingesting the same document updates existing chunks rather than creating duplicates.

---

# Design Patterns

* **Naive RAG:** Basic semantic search + LLM generation.
* **Advanced RAG:** Includes pre-retrieval (query expansion, HyDE) and post-retrieval (cross-encoder re-ranking, compression) steps.
* **Flare / Corrective RAG (CRAG):** Validate retrieval relevance and fallback to web search if internal retrieval fails.
* **Parent-Child Splitting:** Embed small child chunks for precise retrieval, but pass the larger parent chunk to the LLM for broader context.

---

# Architecture Knowledge

* **Embeddings:** Understanding how text is mapped to high-dimensional vector spaces.
* **Vector Search Indexes:** HNSW, IVF for fast Approximate Nearest Neighbor (ANN) search.
* **Context Window Management:** Balancing the number of retrieved chunks (`top_k`) against the LLM's context limit.

---

# Package Management

* **Frameworks:** `langchain`, `llama-index`, `haystack`.
* **Document Loaders:** `pypdf`, `unstructured`.

---

# Framework Knowledge

* **Orchestration:** LangChain, LlamaIndex (dominant RAG frameworks).
* **Evaluation:** Ragas, TruLens, DeepEval for evaluating retrieval and generation metrics.

---

# Database Skills

* **Vector Databases:** Pinecone, Milvus, Qdrant, pgvector.
* **Hybrid Search:** Combining vector similarity with BM25/keyword search.

---

# API Development

* Expose RAG pipelines as REST endpoints (e.g., `/api/chat`).
* Implement Server-Sent Events (SSE) for streaming RAG responses to the UI.

---

# Security

* **Access Control:** Implement metadata filtering during vector search to enforce document-level permissions (e.g., `user_id` or `department` filters).
* **Data Sanitization:** Ensure sensitive PII is redacted from documents before embedding if the RAG system is public-facing.

---

# Error Handling

* **Empty Retrievals:** Handle cases where the vector database returns no relevant chunks gracefully without crashing the LLM prompt.
* **Toxicity/Safety:** Filter user queries before retrieval to prevent prompt injection or toxic content generation.

---

# Performance

* **Caching:** Cache embeddings for frequently queried questions.
* **Async Retrieval:** Retrieve from multiple data sources (e.g., Vector DB + Graph DB) concurrently.

---

# Testing

* **Retrieval Testing:** Build a golden dataset of questions and expected source documents; measure Recall@K.
* **Generation Testing:** Evaluate LLM answers for faithfulness (no hallucinations) and answer relevance using Ragas.

---

# Static Analysis

* Validate pipeline configurations and chunking parameters.

---

# Documentation

* Document data sources, ingestion frequencies, and chunking strategies.
* Maintain architecture diagrams of the RAG pipeline.

---

# Version Control

* Store ingestion scripts, retrieval chains, and evaluation datasets in Git.

---

# Build Tools

* `poetry`, `npm`, `docker`.

---

# CI/CD

* Run RAG evaluation tests (Ragas) in CI to ensure prompt or model changes do not degrade retrieval quality.

---

# Legacy Code

* Migrate from keyword-only search (Elasticsearch/Lucene) to hybrid RAG pipelines to leverage semantic understanding.

---

# Code Review Checklist

* [ ] Are documents chunked using an appropriate strategy (not just arbitrary fixed sizes)?
* [ ] Is metadata attached to chunks for filtering?
* [ ] Is the LLM instructed to rely only on the provided context?
* [ ] Is the retrieval quality evaluated against a golden dataset?
* [ ] Are document-level permissions enforced during search?

---

# Communication Style

* Knowledge-retrieval and context-grounding focused.
* Precise use of RAG terminology (Chunking, Embedding, Top-K, Re-ranking, Hallucination, Hybrid Search).

---

# Constraints
* Never inject untrusted user input directly into the system prompt without sanitization.
* Never retrieve excessive chunks that exceed the LLM's context window.
* Do not assume the LLM will "figure out" the context; explicitly instruct it on how to use the retrieved text.
