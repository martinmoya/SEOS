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
    def generate(self, prompt: str) -> str:
        pass
