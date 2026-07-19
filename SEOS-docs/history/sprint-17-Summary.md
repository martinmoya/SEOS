## Sprint 17 - Summary
Goal: Implement short-term conversational memory to provide context to the LLM across multiple interactions.

## Milestone: M7 - Multi-Agent Collaboration

Status: ✅ Completed (v0.17.0)

## Key Deliverables:

ConversationService to store chat history in memory.
Updated LLM Providers (LMStudio, Ollama) and LLMService to accept and send history (message arrays) to the LLM API.
ChatAgent now saves user prompts and assistant responses to the memory service, and retrieves it for subsequent calls.
Refined delegation prompt to prevent the LLM from inventing non-existent agents for general chat.

## Next Step: Sprint 18 - Unit Testing & Robustness (pytest for SEOS core).
