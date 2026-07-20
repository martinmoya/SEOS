"""
Google Gemini Provider.
"""

import google.generativeai as genai
from config.settings import Settings
from providers.base_provider import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):
    def __init__(self):
        if not Settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not configured in .env file.")
        genai.configure(api_key=Settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(Settings.GEMINI_MODEL)

    def connect(self):
        pass

    def health(self) -> bool:
        try:
            return self.model is not None
        except Exception:
            return False

    def generate(
        self, prompt: str, system: str = None, history: list = None
    ) -> tuple[str, int]:
        gemini_history = []
        if history:
            for msg in history:
                role = "model" if msg["role"] == "assistant" else "user"
                gemini_history.append({"role": role, "parts": [msg["content"]]})

        chat = self.model.start_chat(history=gemini_history)
        response = chat.send_message(prompt)

        text = response.text
        tokens = response.usage_metadata.total_token_count
        return text, tokens
