"""
Find Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class FindAgent(BaseProjectAgent):
    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
            pattern = argument.strip().lower()

            if not pattern:
                return "Usage: /find <text>"

            root = Path(project.root)
            results = []

            for path in root.rglob("*"):
                if any(
                    part in {".git", ".venv", "__pycache__", "logs"}
                    for part in path.parts
                ):
                    continue
                if pattern in path.name.lower():
                    relative = path.relative_to(root)
                    results.append(
                        f"[D] {relative}" if path.is_dir() else f"[F] {relative}"
                    )

            if not results:
                return f'No matches found for "{pattern}".'

            return "\n".join(results)
        except RuntimeError as ex:
            return str(ex)
