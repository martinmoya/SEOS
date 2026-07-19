## Sprint 17 - Technical Log
Architecture Decisions (ADRs)

## ADR-034: Short-Term Memory Injection. ConversationService stores a list of message dictionaries ({"role": "user/assistant", "content": "..."}). This list is injected directly into the API call payload, leveraging the LLM's native chat formatting.

## ADR-035: Delegation Safety Check. ChatAgent now verifies if a delegated agent actually exists in the AgentManager before attempting execution. If the LLM hallucinates a command, SEOS gracefully falls back to returning the raw text response.

## Files Created
services/conversation_service.py

## Files Modified
providers/base_provider.py, providers/lmstudio.py, providers/ollama.py: Added history parameter.
services/llm_service.py: Passes history through.
core/agent_context.py: Injected ConversationService.
agents/chat_agent.py: Integrated memory retrieval, storage, and agent validation.
core/kernel.py: Initialized ConversationService.
