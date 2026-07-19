"""
GitHub Agent.
Orchestrates GitHub operations using GithubSkill.
"""

from agents.base_agent import BaseAgent
from skills.github_skill import GithubSkill


class GithubAgent(BaseAgent):
    description = "Interact with GitHub. Usage: /github <issue|pr> <owner/repo> <title> [head:base]"

    def execute(self, argument: str) -> str:
        parts = argument.split(maxsplit=3)

        if len(parts) < 3:
            return self.description

        action = parts[0].lower()
        repo_name = parts[1]
        title = parts[2]
        extra = parts[3] if len(parts) > 3 else ""

        try:
            skill = GithubSkill()
        except ValueError as ex:
            return str(ex)

        if action == "issue":
            return skill.create_issue(repo_name, title, extra)
        elif action == "pr":
            if not extra:
                return "For PR, provide head:base as the 4th argument. e.g., /github pr owner/repo 'Title' feature:main"
            if ":" not in extra:
                return "Invalid format. Use head:base (e.g., feature:main)."
            head, base = extra.split(":", 1)
            return skill.create_pr(repo_name, head.strip(), base.strip(), title)
        else:
            return "Unsupported action. Use 'issue' or 'pr'."
