"""
Base Agent.
"""

from abc import ABC, abstractmethod
from core.agent_context import AgentContext


class BaseAgent(ABC):
    def __init__(self, context: AgentContext):
        self.context = context

    @abstractmethod
    def execute(self, argument: str) -> str:
        pass
