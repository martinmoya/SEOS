"""
Ls Agent.
Lists files and directories in a given path.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class LsAgent(BaseProjectAgent):
    description = "List files in a directory. Usage: /ls [folder]"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        folder = argument.strip() or "."
        target = Path(project.root) / folder

        if not target.exists() or not target.is_dir():
            return f"Directory not found: {folder}"

        try:
            items = []
            for item in sorted(target.iterdir()):
                prefix = "[D]" if item.is_dir() else "[F]"
                items.append(f"{prefix} {item.name}")
            return "\n".join(items)
        except Exception as ex:
            return f"Error listing directory: {ex}"
