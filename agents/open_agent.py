"""
Open Agent.
"""

from agents.base_project_agent import BaseProjectAgent


class OpenAgent(BaseProjectAgent):
    description = "Open a project directory. Usage: /open <path>"

    def execute(self, argument: str) -> str:
        path = argument.strip()
        if not path:
            return "Usage: /open <project_path>"
        return self.context.workspace_service.open(path)
