"""
Migration Engine.
Uses LLM to translate code between languages and validates the output.
"""

import ast
import re
from pathlib import Path
from services.llm_service import LLMService


class MigrationEngine:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def migrate(self, source_path: Path, target_language: str) -> str:
        source_code = source_path.read_text(encoding="utf-8")
        source_lang = source_path.suffix.lower().lstrip(".")

        prompt = (
            f"Translate the following {source_lang} code to {target_language}. "
            "Ensure the code is complete, functional, and follows best practices. "
            "Return ONLY the raw code. "
            "Do not use markdown blocks. "
            "Do not include explanations.\n\n"
            f"{source_code}"
        )

        response = self.llm.generate(prompt)

        # Extracción robusta: si el LLM hace caso omiso y usa markdown,
        # buscamos el bloque de código y lo extraemos.
        code_match = re.search(r"```(?:python)?\s*\n(.*?)```", response, re.DOTALL)
        if code_match:
            migrated_code = code_match.group(1).strip()
        else:
            # Limpieza básica por si puso markdown sin bloque
            if response.startswith("```python"):
                response = response[9:]
            elif response.startswith("```"):
                response = response[3:]
            if response.endswith("```"):
                response = response[:-3]
            migrated_code = response.strip()

        # Validación de seguridad: Si el destino es Python, validamos con AST
        if target_language.lower() == "python":
            try:
                ast.parse(migrated_code)
            except SyntaxError as ex:
                return f"Migration aborted: LLM generated invalid Python code.\nError: {ex}"

        # Generar nombre de archivo destino
        new_extension = (
            ".py"
            if target_language.lower() == "python"
            else f".{target_language.lower()}"
        )
        dest_path = source_path.with_suffix(f".migrated{new_extension}")

        dest_path.write_text(migrated_code, encoding="utf-8")
        return f"Migration completed successfully.\nCreated: {dest_path.name}"
