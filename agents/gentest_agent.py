"""
Gentest Agent.
Generates unit tests for any source file.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.test_generator import TestGenerator


class GenTestAgent(BaseProjectAgent):
    description = "Generate unit tests for a file. Usage: /gentest <file>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /gentest <file>"

        filepath = Path(project.root) / filename
        if not filepath.exists():
            return f"File not found: {filename}"

        print("\nGenerating tests... Please wait.\n")

        generator = TestGenerator(self.context.llm)
        test_code = generator.generate(filepath)

        # Mantener la extensión, pero añadir prefijo test_
        test_filename = f"test_{filepath.name}"
        test_filepath = filepath.with_name(test_filename)

        test_filepath.write_text(test_code, encoding="utf-8")
        return f"Successfully created test file: {test_filename}\nPath: {test_filepath}"
