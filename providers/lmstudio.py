"""
LM Studio Provider.
"""

from openai import OpenAI
from config.settings import Settings
from providers.base_provider import BaseLLMProvider


class LMStudioProvider(BaseLLMProvider):
    def __init__(self):
        self.client = None

    def connect(self):
        self.client = OpenAI(base_url=Settings.LMSTUDIO_URL, api_key="lm-studio")

    def health(self) -> bool:
        try:
            self.client.models.list()
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

        response = self.client.chat.completions.create(
            model=Settings.MODEL,
            messages=messages,
            temperature=Settings.TEMPERATURE,
            max_tokens=Settings.MAX_TOKENS,
        )

        text = response.choices[0].message.content
        # LM Studio usa la API de OpenAI, así que trae el objeto 'usage'
        tokens = response.usage.total_tokens if response.usage else 0
        return text, tokens
