"""
Translation Processor.
"""

from core.languages import resolve_language
from services.llm_service import LLMService


class TranslationProcessor:
    def __init__(self, llm: LLMService, language: str):
        self.llm = llm
        self.language = resolve_language(language)

    def process(self, text: str) -> str:
        if not text.strip():
            return text

        prompt = (
            f"Translate to {self.language}. "
            "Return ONLY the translated text. "
            "No explanations. No comments.\n\n"
            f"{text}"
        )
        return self.llm.generate(prompt).strip()
