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

    def generate(
        self, prompt: str, system: str = None, history: list = None
    ) -> tuple[str, int]:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat(model=Settings.MODEL, messages=messages)

        text = response["message"]["content"]

        # Ollama devuelve eval_count (tokens de respuesta) y prompt_eval_count (tokens del prompt)
        response_tokens = response.get("eval_count", 0)
        prompt_tokens = response.get("prompt_eval_count", 0)
        total_tokens = response_tokens + prompt_tokens

        return text, total_tokens
