"""
Ollama Provider.
"""

import ollama
from config.settings import Settings
from providers.base_provider import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    def __init__(self):
        self.client = None

    def connect(self):
        self.client = ollama.Client(host=Settings.OLLAMA_URL)

    def health(self) -> bool:
        try:
            self.client.list()
            return True
        except Exception:
            return False

    def generate(self, prompt: str) -> str:
        response = self.client.chat(
            model=Settings.MODEL, messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
