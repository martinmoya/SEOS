"""
Read Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class ReadAgent(BaseProjectAgent):
    description = "Read a text file. Usage: /read <file>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /read <file>"

        target = Path(project.root) / filename

        if not target.exists():
            return f"File not found: {filename}"

        if target.is_dir():
            return f"Not a file: {filename}"

        try:
            return target.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return "The file is not a UTF-8 text file."
