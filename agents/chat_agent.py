"""
Chat Agent.
"""

from agents.base_agent import BaseAgent


class ChatAgent(BaseAgent):
    def execute(self, argument: str) -> str:
        if not argument:
            return "Usage: /chat <message> or just type your message."
        return self.context.llm.generate(argument)
