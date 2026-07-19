"""
Info Agent.
"""

from agents.base_project_agent import BaseProjectAgent


class InfoAgent(BaseProjectAgent):
    description = "Show current project information. Usage: /info"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
            return f"Project  : {project.name}\nLocation : {project.root}"
        except RuntimeError as ex:
            return str(ex)
