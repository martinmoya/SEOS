# Sprint 37 - Technical Log
## Architecture Decisions (ADRs)
## ADR-074: Session-based Multi-Workspace. WorkspaceService maintains a dictionary of opened projects. SwitchAgent changes the active pointer and triggers VectorService to reindex the new root directory, providing instant context switching.
## ADR-075: Root Drive Protection. SwitchAgent detects if the user is trying to switch to a root drive (e.g., C:\) and skips RAG indexing to prevent the system from freezing trying to read the entire disk.

## Parking Lot (Moved to Backlog)
## OCR for Scanned PDFs: The pdfplumber to image conversion requires Ghostscript. On Windows, the Python binding fails to find the Ghostscript DLLs reliably. This feature is postponed until a pure-Python or cloud-based alternative is evaluated.

## Files Created
agents/projects_agent.py
agents/switch_agent.py
documents/__init__.py

## Files Modified
services/workspace_service.py: Added list_projects() and switch().
services/document_processing_service.py: Routed PDF processing to the new PdfReaderDocument.
documents/pdf_reader.py: Integrated OCR fallback (currently non-functional on Windows).
core/kernel.py: Registered /projects and /switch agents.
