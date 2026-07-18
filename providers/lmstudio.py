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

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=Settings.MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=Settings.TEMPERATURE,
            max_tokens=Settings.MAX_TOKENS,
        )
        return response.choices[0].message.content
