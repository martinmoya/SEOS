"""
Role Agent.
Manages active roles for the Prompt Engine.
"""

from agents.base_agent import BaseAgent


class RoleAgent(BaseAgent):
    def execute(self, argument: str) -> str:
        arg = argument.strip().lower()

        if not arg:
            return (
                f"Current active role: {self.context.prompt_service.get_current_role()}"
            )

        if arg == "clear":
            return self.context.prompt_service.clear_role()

        return self.context.prompt_service.set_role(arg)
