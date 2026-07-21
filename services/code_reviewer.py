"""
Code Reviewer.
Uses LLM to perform code reviews and detect issues.
"""

from pathlib import Path
from services.llm_service import LLMService


class CodeReviewer:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def review(self, file_path: Path) -> str:
        code = file_path.read_text(encoding="utf-8")
        lang = file_path.suffix.lstrip(".")

        prompt = (
            f"Act as a strict Senior Software Engineer. "
            f"Review the following {lang} code. "
            "Identify bugs, security vulnerabilities, and code smells. "
            "Provide actionable recommendations for improvement. "
            "Be concise and direct.\n\n"
            f"{code}"
        )

        return self.llm.generate(prompt)
