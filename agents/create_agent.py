"""
Create Agent.
Generates and saves new code files.
"""

import re
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.code_generator import CodeGenerator


class CreateAgent(BaseProjectAgent):
    description = (
        "Generate a Python boilerplate file. Usage: /create <type> <Name|path/Name>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        parts = argument.split(maxsplit=1)
        if len(parts) != 2:
            return "Usage: /create <type> <name> (e.g., /create class UserDTO)"

        element_type = parts[0].lower()
        raw_name = parts[1].strip()

        generator = CodeGenerator(self.context.llm)

        print(f"\nGenerating {element_type} '{raw_name}'... Please wait.\n")

        code = generator.generate(element_type, raw_name)

        # Si el usuario pasó una ruta (ej: src/models/User), respetarla
        if "/" in raw_name or "\\" in raw_name:
            clean_path = raw_name.replace("\\", "/").lstrip("./")
            filepath = Path(project.root) / clean_path
            # Asegurar que tenga extensión .py
            if filepath.suffix != ".py":
                filepath = filepath.with_suffix(".py")
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filename = filepath.name
        else:
            # Si no hay ruta, usar el sandbox projects/
            name_clean = re.sub(
                r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", raw_name
            ).lower()
            filename = name_clean + ".py"
            target_dir = Path(project.root) / "projects"
            target_dir.mkdir(parents=True, exist_ok=True)
            filepath = target_dir / filename

        try:
            filepath.write_text(code, encoding="utf-8")

            # Hooks de Auditoría y Métricas
            self.context.audit_service.log_action("CREATE", filepath)
            self.context.metrics_service.add_file_created()

            return f"Successfully created: {filename}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing file: {ex}"
