"""
Rewrite Processor.
"""

from services.llm_service import LLMService


class RewriteProcessor:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def process(self, text: str) -> str:
        if not text.strip():
            return text

        prompt = (
            "Rewrite the following text to improve clarity, grammar, and professionalism. "
            "Return ONLY the rewritten text. No explanations.\n\n"
            f"{text}"
        )
        return self.llm.generate(prompt).strip()
