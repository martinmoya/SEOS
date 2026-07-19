"""
Example Agent.
Generates and saves Python example files.
"""

import re
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.example_generator import ExampleGenerator


class ExampleAgent(BaseProjectAgent):
    description = "Generate a Python example file. Usage: /create_example <concept>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        if not argument.strip():
            return "Usage: /create_example <concept>"

        generator = ExampleGenerator(self.context.llm)

        print("\nGenerating example... Please wait.\n")
        code = generator.generate(argument)

        # Nombre de archivo
        words = argument.lower().split()[:3]
        filename = (
            "example_" + "_".join(re.sub(r"[^a-z0-9]", "", w) for w in words) + ".py"
        )
        filepath = Path(project.root) / filename

        try:
            filepath.write_text(code, encoding="utf-8")
            return f"Successfully created example: {filename}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing file: {ex}"
