"""
API Agent.
Generates and saves FastAPI endpoint files.
"""

import re
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.api_generator import ApiGenerator


class ApiAgent(BaseProjectAgent):
    description = "Generate a FastAPI endpoint file. Usage: /create_api <description>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        if not argument.strip():
            return "Usage: /create_api <description>"

        generator = ApiGenerator(self.context.llm)

        print("\nGenerating API endpoint... Please wait.\n")
        code = generator.generate(argument)

        words = argument.lower().split()[:3]
        filename = "api_" + "_".join(re.sub(r"[^a-z0-9]", "", w) for w in words) + ".py"

        target_dir = Path(project.root) / "projects"
        target_dir.mkdir(parents=True, exist_ok=True)

        filepath = target_dir / filename

        try:
            filepath.write_text(code, encoding="utf-8")
            return f"Successfully created API endpoint: {filename}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing file: {ex}"
