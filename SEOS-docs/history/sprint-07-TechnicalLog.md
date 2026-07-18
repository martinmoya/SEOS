## Sprint 07 - Technical Log
Architecture Decisions (ADRs)
ADR-013: System Message Separation. LLM calls now explicitly use the system role for persona/rules injection, keeping the user role strictly for the query. This aligns with standard LLM APIs (OpenAI, Ollama) and improves instruction adherence.
ADR-014: CLI Wrapping for Skills. GitSkill uses Python's subprocess to interact with the system's Git installation, keeping Python dependencies minimal while leveraging the standard Git CLI.

## Files Created
skills/git_skill.py
agents/git_agent.py

## Files Modified
providers/base_provider.py, providers/lmstudio.py, providers/ollama.py: Added system parameter to generate().
services/llm_service.py: Passes system parameter through.
services/prompt_service.py: Returns a tuple (system_prompt, user_prompt). Added critical instruction to prevent prompt leaking.
agents/chat_agent.py: Updated to unpack the tuple from PromptService.
core/kernel.py: Registered GitAgent.

