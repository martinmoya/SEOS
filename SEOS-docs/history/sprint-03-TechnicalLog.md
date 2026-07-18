Sprint 03 - Technical Log
Architecture Decisions (ADRs)
ADR-005: Format Preservation Strategy. Office formats (DOCX, XLSX, PPTX) use In-Place Translation (modifying the original file's XML runs/cells directly) to ensure zero loss of formatting. Linear formats (TXT, MD, PDF) use a text extraction pipeline.
ADR-006: ISO Language Resolution. The system accepts standard ISO 639-1 codes (es, en, fr) and resolves them internally before sending the prompt to the LLM.
Files Created
core/languages.py
processors/__init__.py
processors/translation_processor.py
services/document_translation_service.py
agents/translate_agent.py
Files Modified
core/kernel.py: Registered TranslateAgent.
requirements.txt: Added python-docx, openpyxl, python-pptx, pypdf, reportlab.
Key Implementations
Run-level translation: In DOCX/PPTX, text is translated at the run level where possible to preserve bold, italic, and font styles.
Robust Prompting: TranslationProcessor uses a strict prompt ("Return ONLY the translated text") to prevent the LLM from adding conversational filler.
