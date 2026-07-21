"""
Refactor Agent.
Modifies existing source files safely.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.refactoring_engine import RefactoringEngine


class RefactorAgent(BaseProjectAgent):
    description = "Refactor an existing file. Usage: /refactor <file> <instruction>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        parts = argument.split(maxsplit=1)
        if len(parts) != 2:
            return "Usage: /refactor <file> <instruction>"

        filename = parts[0]
        instruction = parts[1]

        filepath = Path(project.root) / filename
        if not filepath.exists():
            return f"File not found: {filename}"

        print("\nRefactoring code... Please wait.\n")

        engine = RefactoringEngine(self.context.llm)
        return engine.refactor(filepath, instruction)
