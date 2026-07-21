"""
Review Agent.
Performs code reviews on any source file.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.code_reviewer import CodeReviewer


class ReviewAgent(BaseProjectAgent):
    description = (
        "Review a code file for bugs and vulnerabilities. Usage: /review <file>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /review <file>"

        filepath = Path(project.root) / filename
        if not filepath.exists():
            return f"File not found: {filename}"

        print("\nReviewing code... Please wait.\n")

        reviewer = CodeReviewer(self.context.llm)
        # Pasamos la extensión al reviewer para que el LLM sepa el contexto
        return reviewer.review(filepath)
