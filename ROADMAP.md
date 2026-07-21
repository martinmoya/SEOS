# SEOS Roadmap
Welcome to the SEOS roadmap! This document outlines the upcoming features and improvements planned for future versions of SEOS.

✅ Current Status (v2.0.0)
SEOS v2.0.0 is officially released! It provides a robust, local-first AI platform with multi-agent collaboration, RAG, document processing, and enterprise integrations.

🚀 Upcoming Milestones (v2.1+)
SEOS Roadmap
Welcome to the SEOS roadmap! This document outlines the upcoming features and improvements planned for future versions of SEOS.

✅ Current Status (v2.0.0)
SEOS v2.0.0 is officially released! It provides a robust, local-first AI platform with multi-agent collaboration, RAG, document processing, and enterprise integrations.

🚀 Upcoming Milestones (v2.1+)

## Milestone 2.1: Productivity & Polish
* **Goal: Enhance user experience, expand language support, and streamline workflows.** *

- **US-001: Output Redirection (> file)**
- **US-002: Vector DB Hot-Reload (File Watcher)**
- **US-003: Multi-Language RAG Support (Index .js, .java, etc.)**
- **US-004: Multi-Workspace Manager (TUI)**
- **US-005: OCR for Scanned PDFs**
- **US-006: Plugin Marketplace CLI (/install)**
- **US-007: Batch Document Processing (Process entire directories at once).**

## Milestone 2.2: Project Intelligence & Cross-Referencing
* **Goal: Understand how files and modules connect to each other to map the project's architecture, execution flow, and find orphaned code.** *

- **US-008: Cross-Reference Analyzer**
Extracts imports and external function calls across all project files to build a Dependency/Call Graph.

- **US-009: Sequence Diagram Generation**
Generates a Mermaid sequence diagram showing the execution flow from an entry point (e.g., /sequence main.py).

- **US-010: Impact Analysis**
Identifies which files will be affected if a specific module is modified (e.g., /impact llm_service.py).

- **US-011: Isolated Files & Dead Code Detection**
Uses the Dependency Graph to find files, classes, or functions that are never imported or called by the rest of the project (orphaned scripts).

* For technical architecture details, please refer to the **ARCHITECTURE.md** *.

