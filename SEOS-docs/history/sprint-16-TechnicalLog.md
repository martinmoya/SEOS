## Sprint 16 - Technical Log
Architecture Decisions (ADRs)

## ADR-032: Agent Registry and Bus. Agents are no longer isolated. AgentService provides a delegate() method allowing any agent to invoke another, enabling complex workflows.

## ADR-033: LLM Intent Delegation. ChatAgent uses a strict system prompt forcing the LLM to respond with a DELEGATE: /<command> <argument> syntax when the user's request matches an agent's capability. Regular expressions parse this response to trigger the delegation.

## Files Created
managers/agent_manager.py
services/agent_service.py

## Files Modified
core/agent_context.py: Injected AgentService.
core/kernel.py: Replaced internal dictionary with AgentManager and wired AgentService.
agents/chat_agent.py: Added delegation logic and rich console for status messages.
