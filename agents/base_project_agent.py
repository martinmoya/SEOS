"""
Base Project Agent.
"""

from agents.base_agent import BaseAgent


class BaseProjectAgent(BaseAgent):
    @property
    def project(self):
        return self.context.project

    def require_project(self):
        if self.project is None:
            raise RuntimeError("No active project. Use /open <path> first.")
        return self.project
