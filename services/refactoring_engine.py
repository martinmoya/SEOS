"""
Refactoring Engine.
Uses LLM to refactor existing code and validates output if Python.
"""

import ast
from pathlib import Path
from services.llm_service import LLMService


class RefactoringEngine:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def refactor(self, file_path: Path, instruction: str) -> str:
        original_code = file_path.read_text(encoding="utf-8")
        lang = file_path.suffix.lstrip(".")

        prompt = (
            f"Refactor the following {lang} code. Instruction: {instruction}. "
            "Ensure the code remains functional and clean. "
            "Return ONLY the raw code. "
            "Do not use markdown blocks. Do not include explanations.\n\n"
            f"{original_code}"
        )

        response = self.llm.generate(prompt)

        if response.startswith("```"):
            response = response.split("```")[1].split("```")[0]
            if response.startswith(lang):
                response = response[len(lang) :]

        refactored_code = response.strip()

        # Validación de seguridad SOLO para Python
        if lang.lower() == "py":
            try:
                ast.parse(refactored_code)
            except SyntaxError as ex:
                return f"Refactoring aborted: LLM generated invalid Python code.\nError: {ex}"

        file_path.write_text(refactored_code, encoding="utf-8")
        return "Refactoring applied successfully."
