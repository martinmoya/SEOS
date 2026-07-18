## Sprint 06 - Technical Log
Architecture Decisions (ADRs)
ADR-011: Dynamic Prompt Composition. Prompts are no longer static. PromptService dynamically concatenates active Role context, Global Rules, and the user's query. This prepares SEOS for future Multi-Agent prompting.

ADR-012: Stateful Role Management. The active role is maintained in memory by PromptService until explicitly cleared (/role clear), simulating a continuous session with a specific specialist.

## Files Created
services/prompt_service.py
agents/role_agent.py

## Files Modified
core/agent_context.py: Injected PromptService.
core/kernel.py: Initialized PromptService and registered RoleAgent.
agents/chat_agent.py: Updated to use context.prompt_service.build_prompt().

