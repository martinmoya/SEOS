"""
Test Generator.
Uses LLM to generate unit tests for a given file.
"""

from pathlib import Path
from services.llm_service import LLMService


class TestGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate(self, file_path: Path) -> str:
        original_code = file_path.read_text(encoding="utf-8")
        lang = file_path.suffix.lstrip(".")

        prompt = (
            f"Generate comprehensive unit tests for the following {lang} code. "
            f"Use the standard testing framework for {lang} (e.g., JUnit for Java, Jest for JS, pytest for Python). "
            "Include necessary imports and cover edge cases. "
            "Return ONLY the raw code. Do not use markdown blocks.\n\n"
            f"{original_code}"
        )

        response = self.llm.generate(prompt)

        if response.startswith("```"):
            response = response.split("```")[1].split("```")[0]
            if response.startswith(lang):
                response = response[len(lang) :]

        return response.strip()
