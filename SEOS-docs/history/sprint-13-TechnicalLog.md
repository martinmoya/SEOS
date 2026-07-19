## Sprint 13 - Technical Log
Architecture Decisions (ADRs)
ADR-026: Rich Terminal UI. core/kernel.py and core/banner.py now use the rich library for a professional CLI experience.

ADR-027: REST API Core. SEOS can now run as a headless service (/serve) using FastAPI and Uvicorn. This decouples the engine from the CLI, allowing future IDE integrations.

## Files Created
api/__init__.py
api/rest_app.py
agents/serve_agent.py

## Files Modified
core/banner.py: Replaced ASCII print with rich.panel.Panel.
core/kernel.py: Replaced print with rich.console.Console. Registered ServeAgent.
requirements.txt: Added rich, fastapi, uvicorn.
