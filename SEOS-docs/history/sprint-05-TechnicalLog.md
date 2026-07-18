Sprint 05 - Technical Log
Architecture Decisions (ADRs)

ADR-009: Hierarchical Knowledge Loading. The KnowledgeService uses pathlib.rglob to recursively discover .md files. This allows organizing capabilities into nested folders (e.g., capabilities/Languages/python_skill.md) without breaking the loader.

ADR-010: Context Key Namespacing. Loaded knowledge items are keyed by their relative path (e.g., Languages/python_skill) to prevent naming collisions between different domains.

Files Created
services/knowledge_service.py
knowledge/roles/*.md (19 files)
knowledge/rules/*.md (2 files)
knowledge/capabilities/**/*.md (110 files)

Files Modified
core/agent_context.py: Injected KnowledgeService.
core/kernel.py: Initialized KnowledgeService at startup and logged stats.

