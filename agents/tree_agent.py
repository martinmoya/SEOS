"""
Tree Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class TreeAgent(BaseProjectAgent):
    description = "Display project directory tree. Usage: /tree [folder]"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        folder = argument.strip() or ""
        target_dir = Path(project.root) / folder if folder else Path(project.root)

        if not target_dir.exists() or not target_dir.is_dir():
            return f"Directory not found: {folder or '.'}"

        lines = [target_dir.name]
        for path in sorted(target_dir.rglob("*")):
            if any(
                part
                in {
                    ".git",
                    ".venv",
                    "__pycache__",
                    "logs",
                    "projects",
                    ".seos_vector_db",
                }
                for part in path.parts
            ):
                continue
            relative = path.relative_to(target_dir)
            lines.append(f"[D] {relative}" if path.is_dir() else f"[F] {relative}")

        return "\n".join(lines)
