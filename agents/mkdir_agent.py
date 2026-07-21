"""
Mkdir Agent.
Creates a new directory.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class MkdirAgent(BaseProjectAgent):
    description = "Create a new directory. Usage: /mkdir <folder>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        folder = argument.strip()
        if not folder:
            return "Usage: /mkdir <folder>"

        target = Path(project.root) / folder

        try:
            target.mkdir(parents=True, exist_ok=True)
            return f"Directory created successfully: {target}"
        except Exception as ex:
            return f"Error creating directory: {ex}"
