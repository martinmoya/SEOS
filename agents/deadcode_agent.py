"""
Dead Code Agent.
Finds files that are never imported by anyone.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.intelligence_service import IntelligenceService


class DeadCodeAgent(BaseProjectAgent):
    description = "Find orphaned files not imported anywhere. Usage: /deadcode"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        print("\nScanning project for dead code... Please wait.\n")

        service = IntelligenceService(Path(project.root))
        dead_files = service.find_dead_code()

        if not dead_files:
            return "✅ No dead code found. All files are connected to the project."

        lines = [
            "🗑️ Dead Code / Isolated Files Found:",
            "These files are not imported by anyone (excluding entry points like main.py):",
        ]
        for f in dead_files:
            lines.append(f"  - {f}")

        return "\n".join(lines)
