"""
Projects Agent.
Lists all opened projects in the current session.
"""

from agents.base_agent import BaseAgent


class ProjectsAgent(BaseAgent):
    description = "List all opened projects in the session. Usage: /projects"

    def execute(self, argument: str) -> str:
        projects = self.context.workspace_service.list_projects()
        active = self.context.workspace_service.current()

        if not projects:
            return "No projects open. Use /open <path> to open one."

        lines = ["--- Open Projects ---"]
        for p in projects:
            prefix = "[*]" if p == active else "[ ]"
            lines.append(f"{prefix} {p.name} ({p.root})")

        return "\n".join(lines)
