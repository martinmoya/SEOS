"""
Sprint Agent.
Triggers autonomous multi-agent workflows.
"""

from agents.base_project_agent import BaseProjectAgent
from services.workflow_engine import WorkflowEngine


class SprintAgent(BaseProjectAgent):
    description = (
        "Execute an autonomous development sprint. Usage: /sprint <requirement>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        if not argument.strip():
            return "Usage: /sprint <high-level requirement>"

        engine = WorkflowEngine(self.context.llm, self.context.agent_service)
        return engine.execute_sprint(argument)
