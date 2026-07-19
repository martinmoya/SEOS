# SEOS Post-v1.0 Backlog
This document outlines the features and capabilities planned for future versions of SEOS (v1.x and beyond), picking up after the v1.0.0 release.

## Milestone 1.1: Multi-Language & Legacy Analysis (The "Legacy" Vision)
Goal: Extend SEOS's understanding beyond Python to support legacy systems and modern languages.

US-001: Universal AST Parser: Integrate tree-sitter to parse multiple languages (Java, C#, JavaScript, Go, Rust) uniformly.
US-002: Legacy Code Analyzer: Create analyzers for legacy languages (Perl, COBOL, VB6, PHP) using regex and LLM-assisted structural analysis.
US-003: Universal Knowledge Graph: Update PythonKnowledge to a generic CodeKnowledge graph that stores entities from any language.
US-004: Legacy Auto-Documentation: A specific agent (/legacy_doc) that reads an undocumented legacy file, infers its purpose, and generates a Markdown specification.
US-005: Architecture Diagrams from Code: Automatically generate Mermaid UML diagrams (Class, Sequence, ERD) directly from the Knowledge Graph of any language.

## Milestone 1.2: Code Migration Engine
Goal: Assist in modernizing applications by translating logic between languages.

US-006: Language Translator Agent: /migrate <source_file> <target_language> (e.g., /migrate legacy_login.pl python).
US-007: Dependency Mapping for Migration: Analyze external dependencies (e.g., Perl DBI to Python SQLAlchemy) and suggest modern equivalents.
US-008: Migration Validation Pipeline: Compare the AST and execution output of the original legacy file against the newly generated modern file to ensure logic parity.

## Milestone 1.3: Advanced AI & Memory (RAG)
Goal: Give SEOS long-term memory and project-wide context.

US-009: Vector Database Integration: Embed all project files into a local vector DB (e.g., ChromaDB) for semantic search.
US-010: RAG Agent: Update ChatAgent to automatically query the vector DB for relevant code snippets across the whole project before answering.
US-011: Long-Term Project Memory: Store architectural decisions, user preferences, and past refactoring history in a persistent knowledge base.

## Milestone 1.4: Enterprise Multi-Agent Workflows
Goal: Fully autonomous software engineering teams.

US-012: Team Builder Agent: Dynamically create a team of agents (Backend, QA, DBA) based on the user's high-level request.
US-013: Autonomous Sprint Execution: /sprint "Create user login module" triggers a full workflow: Architect designs -> Coder writes -> Tester tests -> Reviewer approves.
US-014: Conflict Resolution Engine: If the QA agent and Security agent disagree on a code implementation, a Lead Architect agent steps in to break the tie.

## Milestone 1.5: UI & UX Enhancements
Goal: Move beyond the CLI to a rich visual experience.

US-015: Web Dashboard: A React/Next.js frontend consuming the SEOS REST API to visualize the Knowledge Graph, agent logs, and metrics.
US-016: VS Code Extension v2: Inline code diffs for refactoring, sidebar panel for SEOS chat, and automatic error highlighting.
US-017: TUI Dashboard: A full-screen terminal UI (using Textual) with split panes for file tree, chat, and logs.

## Milestone 1.6: Advanced Document Fidelity & Conversion
Goal: Achieve 100% visual fidelity when translating or converting documents, handling complex layouts, images, and scanned files.

US-022: Advanced PDF Translation: Replace the basic pypdf text extraction with a layout-aware parser (like pdfplumber or PyMuPDF) to preserve columns, fonts, and table structures in the translated PDF.
US-023: OCR Integration: Integrate Tesseract or an LLM-based Vision model to translate text embedded in images within DOCX/PPTX files, or entirely scanned PDF documents.
US-024: Cross-Format Conversion Pipeline: Implement true format conversion (e.g., /convert manual.docx pdf) that preserves images, tables, and styling across formats using headless LibreOffice or specialized libraries.
US-025: Image Extraction & Re-insertion: Automatically extract images from source documents, keep them in place, and ensure they are correctly re-inserted into the translated destination document.

## Milestone 1.7: Advanced AI & MCP Ecosystem
Goal: Expand SEOS beyond local text models into a multi-modal, highly connected ecosystem.

US-026: Multi-Cloud AI Routing: Implement a ProviderRegistry to route specific tasks to specialized cloud AIs (e.g., OpenAI for complex logic, Gemini for Vision/Image analysis, ElevenLabs for Audio).
US-027: MCP (Model Context Protocol) Client: Allow SEOS to act as an MCP client, connecting to external MCP servers (e.g., filesystem, external databases, third-party APIs) to expand its toolset.
US-028: Consensus & Conflict Resolution Engine: When multiple agents (e.g., Security and Performance) disagree on a code implementation, a Lead Architect agent evaluates the proposals and breaks the tie.

## Milestone 1.8: Enterprise Metrics & Audit
Goal: Provide observability and control for teams using SEOS.

US-029: Productivity Metrics Dashboard: Track and display statistics (tokens used, lines of code generated, time saved) in a visual dashboard via the REST API.
US-030: Audit Logging System: Maintain an immutable, exportable log of all autonomous actions and file modifications made by SEOS agents.

## Milestone 1.9: Self-Development (Dogfooding)
Goal: Use SEOS to develop SEOS.

US-031: Auto-ADR Generation: SEOS automatically detects significant architectural changes in commits and drafts the corresponding ADR.
US-032: Self-Review Pipeline: SEOS runs /review on its own pull requests before submitting them.
US-033: Autonomous Backlog Grooming: SEOS analyzes closed issues and suggests new User Stories based on code gaps.
Milestone 1.10: Plugin Marketplace & Distribution
Goal: Foster a community-driven ecosystem.

US-034: Plugin Manifest Specification: Define a standard plugin.yaml format for third-party agents and skills.
US-035: Plugin Manager CLI: Commands like /install <plugin_name> and /uninstall <plugin_name> to fetch community plugins from a registry.
