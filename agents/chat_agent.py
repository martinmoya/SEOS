"""
Chat Agent.
"""

from agents.base_agent import BaseAgent


class ChatAgent(BaseAgent):
    def execute(self, argument: str) -> str:
        if not argument:
            return "Usage: /chat <message>"

        # Usamos el PromptService en lugar de enviar el texto crudo
        prompt = self.context.prompt_service.build_prompt(argument)
        return self.context.llm.generate(prompt)
