"""
Agent Context.
Shared execution context for all agents.
"""

from services.llm_service import LLMService


class AgentContext:
    def __init__(self, llm: LLMService):
        self.llm = llm
