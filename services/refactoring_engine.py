"""
Refactoring Engine.
Uses LLM to refactor existing code and AST to validate changes.
"""

import ast
from pathlib import Path
from services.llm_service import LLMService


class RefactoringEngine:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def refactor(self, file_path: Path, instruction: str) -> str:
        original_code = file_path.read_text(encoding="utf-8")

        prompt = (
            f"Refactor the following Python code. Instruction: {instruction}. "
            "Ensure the code remains functional and clean. "
            "Return ONLY the raw Python code. "
            "Do not use markdown blocks (```python). "
            "Do not include explanations.\n\n"
            f"{original_code}"
        )

        response = self.llm.generate(prompt)

        # Limpieza de markdown
        if response.startswith("```python"):
            response = response[9:]
        elif response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]

        refactored_code = response.strip()

        # Validación de seguridad: Si el LLM devuelve código inválido, abortamos
        try:
            ast.parse(refactored_code)
        except SyntaxError as ex:
            return (
                f"Refactoring aborted: LLM generated invalid Python code.\nError: {ex}"
            )

        # Si es válido, sobreescribimos el archivo original
        file_path.write_text(refactored_code, encoding="utf-8")
        return "Refactoring applied successfully."
