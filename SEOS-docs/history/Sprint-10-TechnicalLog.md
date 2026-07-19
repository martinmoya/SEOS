## Sprint 10 - Technical Log
Architecture Decisions (ADRs)
ADR-020: Standardized Agent Descriptions. All agents now inherit a description attribute from BaseAgent. This decouples help text from the Kernel, making the system self-documenting.

ADR-021: Contextual Help. The Kernel intercepts /help <command> and introspects the agent registry to display the specific agent's description, avoiding bloated if/else chains.

## Files Created
services/api_generator.py
services/db_generator.py
agents/api_agent.py
agents/db_agent.py

## Files Modified
agents/base_agent.py: Added description class attribute.
core/kernel.py: Enhanced /help logic and registered new agents.
All existing agents: Added description attribute.
