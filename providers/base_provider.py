"""
Base LLM Provider.
"""

from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def health(self) -> bool:
        pass

    @abstractmethod
    def generate(
        self, prompt: str, system: str = None, history: list = None
    ) -> tuple[str, int]:
        """Returns a tuple of (response_text, total_tokens_used)."""
        pass
