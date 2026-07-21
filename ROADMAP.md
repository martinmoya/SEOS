# SEOS Roadmap

Welcome to the **SEOS roadmap**! This document outlines the upcoming features and improvements planned for future versions of SEOS.

---

# ✅ Current Status (v2.0.0)

SEOS **v2.0.0** is officially released!

It provides a robust, local-first AI platform with:

- Multi-agent collaboration
- RAG
- Document processing
- Enterprise integrations

---

# 🚀 Upcoming Milestones

# Version 2.1 — Quality Suprema & Polyglot Engine

---

## Milestone 2.1 — UX Polish & Knowledge Visibility

**Goal:** Eliminate user friction, allow large prompt handling, expose the internal knowledge base, and fix UI bugs.

### US-001 — Output Redirection (`> file`)

Allow command outputs to be saved directly to files.

**Example**

```text
/review main.py > review.md
```

---

### US-002 — Large Prompt Handling (`/load <file>`)

Bypass TUI copy/paste limitations by allowing users to load massive prompts from text files.

---

### US-003 — Knowledge Visibility (`/list`)

Command to list registered roles, rules, and capabilities filtered by area.

**Example**

```text
/list capabilities AI
```

---

### US-004 — Enhanced Filesystem Commands

- `/tree <folder>` to target specific directories.
- `/mkdir <folder>` for directory creation.
- `/ls <folder>` for directory listing.

---

### US-005 — Diagram Filename Bugfix

Sanitize arguments in `/create_diagram` to prevent malformed filenames when paths are used.

---

## Milestone 2.2 — Polyglot Engine & Productivity

**Goal:** Break Python exclusivity and improve project management workflows.

### US-006 — Multi-Language Code Processing

Remove Python constraints from:

- `/create_example`
- `/gentest`
- `/refactor`
- `/review`

The LLM will adapt to the target language dynamically.

---

### US-007 — Universal Symbols Analysis

Ensure `/symbols` works flawlessly with the UniversalAnalyzer for:

- Java
- JavaScript
- C#
- Go
- Other supported languages

Remove the `.py` restriction.

---

### US-008 — Polyglot Test Runner (`/test`)

Automatically detect the project language/framework and execute the correct test runner.

Supported project indicators include:

- `pom.xml`
- `package.json`
- `go.mod`
- `requirements.txt`

---

### US-009 — Vector DB Hot-Reload (File Watcher)

Implement a file watcher that detects disk changes and updates the vector database in real time without restarting SEOS.

---

### US-010 — Multi-Language RAG Support

Expand the `VectorService` indexer to process:

- `.py`
- `.js`
- `.ts`
- `.java`
- `.cs`
- `.md`

and additional supported formats.

---

### US-011 — Multi-Workspace Manager (TUI)

Enhance the `/open` command to keep a history of opened projects during the session.

New commands:

- `/projects`
- `/switch <name>`

---

### US-012 — OCR for Scanned PDFs

Integrate `ocrmypdf` or process PDF page images through the `OcrSkill` before translation or extraction.

---

### US-013 — Plugin Marketplace CLI (`/install`)

Implement:

```text
/install <github_url>
```

to clone repositories directly into the `plugins/` directory and load them dynamically.

---

### US-014 — Batch Document Processing

Modify the `DocumentProcessingService` and related agents to accept directories.

**Example**

```text
/translate docs/ en
```

---

## Milestone 2.3 — Project Intelligence & Cross-Referencing

**Goal:** Understand how files and modules connect to each other in order to map the project's architecture and identify orphaned code.

### US-015 — Cross-Reference Analyzer

Extract imports and external function calls across all project files to build a Dependency/Call Graph.

---

### US-016 — Sequence Diagram Generation

Generate a Mermaid sequence diagram showing the execution flow from a given entry point.

**Example**

```text
/sequence main.py
```

---

### US-017 — Impact Analysis

Identify which files will be affected if a specific module is modified.

**Example**

```text
/impact llm_service.py
```

---

### US-018 — Isolated Files & Dead Code Detection

Use the Dependency Graph to identify:

- Files that are never imported
- Classes that are never referenced
- Functions that are never called
- Dead code throughout the project
  