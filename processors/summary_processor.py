"""
Summary Processor.
"""

from services.llm_service import LLMService


class SummaryProcessor:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def process(self, text: str) -> str:
        if not text.strip():
            return text

        prompt = (
            "Summarize the following text concisely. "
            "Return ONLY the summary. No explanations.\n\n"
            f"{text}"
        )
        return self.llm.generate(prompt).strip()
