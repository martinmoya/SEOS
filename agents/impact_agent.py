"""
Impact Agent.
Shows which files depend on a given file.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.intelligence_service import IntelligenceService


class ImpactAgent(BaseProjectAgent):
    description = "Show files affected by modifying a file. Usage: /impact <file>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /impact <file>"

        print("\nAnalyzing project dependencies... Please wait.\n")

        service = IntelligenceService(Path(project.root))
        affected = service.get_impact(filename)

        if not affected:
            return f"No files depend on {filename}. It is safe to modify or delete."

        lines = [
            f"⚠️ Impact Analysis for {filename}:",
            "The following files import or depend on this file:",
        ]
        for f in affected:
            lines.append(f"  - {f}")

        return "\n".join(lines)
