"""
Review Agent.
Performs code reviews on Python files.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.code_reviewer import CodeReviewer


class ReviewAgent(BaseProjectAgent):
    description = (
        "Review a Python file for bugs and vulnerabilities. Usage: /review <file>"
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
        if not filepath.exists() or filepath.suffix != ".py":
            return f"File not found or not a Python file: {filename}"

        print("\nReviewing code... Please wait.\n")

        reviewer = CodeReviewer(self.context.llm)
        return reviewer.review(filepath)
