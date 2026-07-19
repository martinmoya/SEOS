"""
Base Agent.
"""

from abc import ABC, abstractmethod
from core.agent_context import AgentContext


class BaseAgent(ABC):
    description: str = "No description available."

    def __init__(self, context: AgentContext):
        self.context = context

    @abstractmethod
    def execute(self, argument: str) -> str:
        pass
