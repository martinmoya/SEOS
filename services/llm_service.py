"""
LLM Service.
Wraps provider calls.
"""

from providers.base_provider import BaseLLMProvider


class LLMService:
    def __init__(self, provider: BaseLLMProvider):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
