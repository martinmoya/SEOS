"""
Role Agent.
Manages active roles for the Prompt Engine and guides the user.
"""

from agents.base_agent import BaseAgent


class RoleAgent(BaseAgent):
    description = "Manage active roles. Usage: /role [name|clear]"

    def execute(self, argument: str) -> str:
        arg = argument.strip().lower()

        if not arg:
            return (
                f"Current active role: {self.context.prompt_service.get_current_role()}"
            )

        if arg == "clear":
            return self.context.prompt_service.clear_role()

        result = self.context.prompt_service.set_role(arg)

        # GUIA DE USO PARA EL USUARIO
        if "successfully set" in result:
            result += "\n\n💡 [Next Step] The role is now active. Try these:"
            result += "\n  • /chat Explain the best architecture for this project"
            result += "\n  • /sprint Create a caching module for the database"

        return result
