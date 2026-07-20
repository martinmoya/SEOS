# SEOS Roadmap
Welcome to the SEOS roadmap! This document outlines the upcoming features and improvements planned for future versions of SEOS.

✅ Current Status (v2.0.0)
SEOS v2.0.0 is officially released! It provides a robust, local-first AI platform with multi-agent collaboration, RAG, document processing, and enterprise integrations.

🚀 Upcoming Milestones (v2.1+)
Milestone 2.1: Productivity & Polish
Goal: Enhance user experience, expand language support, and streamline workflows.

- **US-001: Output Redirection (> file)**
Problem: Copying long text from the TUI is difficult.
Solution: Allow any command to save its output directly to a file (e.g., /chat explain kernel.py > explicacion.txt or /review main.py > review.md).

- **US-002: Vector DB Hot-Reload (File Watcher)**
Problem: If files are modified or created, SEOS doesn't know until restarted, because RAG indexing happens at startup.
Solution: Implement a file watcher that detects disk changes and updates the vector DB in real-time without restarting SEOS.

- **US-003: Multi-Language RAG Support**
Problem: Currently, the RAG indexer only reads .py files.
Solution: Expand the VectorService indexer to read .js, .ts, .java, .cs, .md, etc., giving the ChatAgent real context in any project.

- **US-004: Multi-Workspace Manager (TUI)**
Problem: Changing projects requires restarting SEOS in a different folder.
Solution: Enhance the /open command to keep a history of opened projects in the session. Add commands like /projects (list open) and /switch <name>.

- **US-005: OCR for Scanned PDFs**
Problem: pdfplumber extracts text from digital PDFs, but fails on scanned documents.
Solution: Integrate ocrmypdf or pass PDF page images through the OcrSkill before translation/extraction.

- **US-006: Plugin Marketplace CLI (/install)**
Problem: Plugins must be downloaded and placed in the folder manually.
Solution: Implement /install <github_url> to clone the repository directly into plugins/ and load it hot.

* For technical architecture details, please refer to the **ARCHITECTURE.md** *.

