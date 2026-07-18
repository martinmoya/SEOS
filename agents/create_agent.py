"""
Create Agent.
Generates and saves new code files.
"""

import re
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.code_generator import CodeGenerator


class CreateAgent(BaseProjectAgent):
    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        parts = argument.split(maxsplit=1)
        if len(parts) != 2:
            return "Usage: /create <type> <name> (e.g., /create class UserDTO)"

        element_type = parts[0].lower()
        name = parts[1].strip()

        generator = CodeGenerator(self.context.llm)

        print(f"\nGenerating {element_type} '{name}'... Please wait.\n")

        code = generator.generate(element_type, name)

        # Conversión robusta a snake_case usando Regex
        # Ej: UserDTO -> user_dto, XMLHttpRequest -> xml_http_request
        name_clean = re.sub(
            r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", name
        ).lower()
        filename = name_clean + ".py"
        filepath = Path(project.root) / filename

        try:
            filepath.write_text(code, encoding="utf-8")
            return f"Successfully created: {filename}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing file: {ex}"
