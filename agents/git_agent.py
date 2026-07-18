"""
Git Agent.
Orchestrates Git operations using GitSkill.
"""

from agents.base_project_agent import BaseProjectAgent
from skills.git_skill import GitSkill


class GitAgent(BaseProjectAgent):
    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        parts = argument.split(maxsplit=1)
        subcommand = parts[0].lower() if parts else ""
        args = parts[1] if len(parts) > 1 else ""

        skill = GitSkill(project.root)

        if subcommand == "status":
            return skill.status()
        elif subcommand == "add":
            return skill.add(args)
        elif subcommand == "commit":
            return skill.commit(args)
        elif subcommand == "diff":
            return skill.diff()
        elif subcommand == "log":
            return skill.log()
        else:
            return "Usage: /git <status|add|commit|diff|log> [args]"
