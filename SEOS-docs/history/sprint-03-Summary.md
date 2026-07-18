## Sprint 03 - Summary
Goal: Implement the document translation pipeline capable of processing TXT, MD, PDF, DOCX, XLSX, and PPTX, preserving format in Office documents.

## Milestone: M2 - Document Engine & Translation

Status: ✅ Completed (v0.3.0)

## Key Deliverables:
Language resolution utility (ISO codes to full names).
TranslationProcessor using LLM.
DocumentTranslationService orchestrating format-specific strategies.
In-Place Translation for DOCX, XLSX, PPTX preserving tables, runs, and styles.
Text pipeline for TXT, MD.

## /translate command functional.
Known Limitations (Backlog for M2):

PDF translation extracts text only; images, tables, and layout are not preserved.
XLSX translation makes one LLM call per cell, which can cause timeouts on very large spreadsheets.
