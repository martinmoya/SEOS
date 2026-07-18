## Sprint 09 - Technical Log
Architecture Decisions (ADRs)
ADR-017: LLM Code Generation. CodeGenerator uses strict prompting to ensure the LLM returns only raw Python code without markdown blocks. It includes a fallback cleanup in case the LLM disobeys.

ADR-018: Regex Snake Case Conversion. Filenames are generated from class names using re.sub to handle edge cases like UserDTO -> user_dto.py correctly.

ADR-019: Centralized Help. The /help command is intercepted by the Kernel, which dynamically lists all registered agents. This ensures the help menu is always up to date without manual maintenance.

## Files Created
services/code_generator.py
agents/create_agent.py

## Files Modified
core/kernel.py: Added /help command logic and registered CreateAgent.
