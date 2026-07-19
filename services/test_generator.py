"""
Test Generator.
Uses LLM to generate pytest unit tests for a given file.
"""

from pathlib import Path
from services.llm_service import LLMService


class TestGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate(self, file_path: Path) -> str:
        original_code = file_path.read_text(encoding="utf-8")

        prompt = (
            "Generate comprehensive pytest unit tests for the following Python code. "
            "Include necessary imports and cover edge cases. "
            "Return ONLY the raw Python code. "
            "Do not use markdown blocks (```python). "
            "Do not include explanations.\n\n"
            f"{original_code}"
        )

        response = self.llm.generate(prompt)

        if response.startswith("```python"):
            response = response[9:]
        elif response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]

        return response.strip()
