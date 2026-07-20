"""
ADR Generator.
Uses Git history and LLM to draft Architecture Decision Records.
"""

import subprocess
from pathlib import Path
from services.llm_service import LLMService


class AdrGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate_from_git(self, root: Path) -> str:
        # Obtener los últimos 5 commits
        try:
            result = subprocess.run(
                ["git", "log", "--oneline", "-10"],
                cwd=root,
                capture_output=True,
                text=True,
                check=True,
            )
            commits = result.stdout.strip()
        except Exception:
            return "Error: Could not retrieve Git history."

        prompt = (
            "Based on the following recent Git commits, draft an Architecture Decision Record (ADR) in Markdown. "
            "Use the standard ADR format (Context, Decision, Consequences). "
            "Return ONLY the raw Markdown.\n\n"
            f"Git Commits:\n{commits}"
        )

        response = self.llm.generate(prompt)

        # Limpiar markdown si el LLM lo envolvió
        if response.startswith("```markdown"):
            response = response[12:]
        elif response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]

        return response.strip()
