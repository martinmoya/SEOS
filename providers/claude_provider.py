"""
Anthropic Claude Provider.
"""

import anthropic
from config.settings import Settings
from providers.base_provider import BaseLLMProvider
from core.exceptions import ConfigurationError


class ClaudeProvider(BaseLLMProvider):
    def __init__(self):
        if not Settings.CLAUDE_API_KEY:
            raise ConfigurationError("CLAUDE_API_KEY is not configured in .env file.")
        self.client = anthropic.Anthropic(api_key=Settings.CLAUDE_API_KEY)

    def connect(self):
        pass

    def health(self) -> bool:
        try:
            self.client.models.list()
            return True
        except Exception:
            return False

    def generate(self, prompt: str, system: str = None, history: list = None) -> str:
        messages = []
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": prompt})

        response = self.client.messages.create(
            model=Settings.CLAUDE_MODEL,
            system=system or "",
            messages=messages,
            max_tokens=Settings.MAX_TOKENS,
            temperature=Settings.TEMPERATURE,
        )
        return response.content[0].text
