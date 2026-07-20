"""
OpenAI Cloud Provider.
"""

from openai import OpenAI
from config.settings import Settings
from providers.base_provider import BaseLLMProvider
from core.exceptions import ConfigurationError


class OpenAIProvider(BaseLLMProvider):
    def __init__(self):
        if not Settings.OPENAI_API_KEY:
            raise ConfigurationError("OPENAI_API_KEY is not configured in .env file.")
        self.client = OpenAI(api_key=Settings.OPENAI_API_KEY)

    def connect(self):
        pass  # Client is initialized in __init__

    def health(self) -> bool:
        try:
            self.client.models.list()
            return True
        except Exception:
            return False

    def generate(self, prompt: str, system: str = None, history: list = None) -> str:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=Settings.OPENAI_MODEL,
            messages=messages,
            temperature=Settings.TEMPERATURE,
            max_tokens=Settings.MAX_TOKENS,
        )
        return response.choices[0].message.content
