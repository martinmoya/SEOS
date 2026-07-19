"""
Tree Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class TreeAgent(BaseProjectAgent):
    description = "Display the project directory tree. Usage: /tree"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
            root = Path(project.root)

            lines = [project.name]
            for path in sorted(root.rglob("*")):
                if any(
                    part in {".git", ".venv", "__pycache__", "logs"}
                    for part in path.parts
                ):
                    continue
                relative = path.relative_to(root)
                lines.append(f"[D] {relative}" if path.is_dir() else f"[F] {relative}")

            return "\n".join(lines)
        except RuntimeError as ex:
            return str(ex)
