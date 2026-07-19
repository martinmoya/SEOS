"""
Chat Agent.
"""

from agents.base_agent import BaseAgent


class ChatAgent(BaseAgent):
    description = "Talk to the LLM. Usage: /chat <message> (or just type your message)"

    def execute(self, argument: str) -> str:
        if not argument:
            return "Usage: /chat <message>"

        system_prompt, user_prompt = self.context.prompt_service.build_prompt(argument)
        return self.context.llm.generate(user_prompt, system=system_prompt)
