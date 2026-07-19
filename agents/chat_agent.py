"""
Chat Agent.
"""

import re
from rich.console import Console
from agents.base_agent import BaseAgent


class ChatAgent(BaseAgent):
    description = (
        "Talk to the LLM. Can delegate tasks to other agents. Usage: /chat <message>"
    )

    def execute(self, argument: str) -> str:
        if not argument:
            return "Usage: /chat <message>"

        system_prompt, user_prompt = self.context.prompt_service.build_prompt(argument)

        # Instrucciones más estrictas para forzar la delegación
        delegation_instructions = (
            "\n\nCRITICAL ORCHESTRATION RULES:\n"
            "You are an orchestrator. You MUST delegate tasks to other agents using the exact format: DELEGATE: /<command> <argument>\n"
            "- If the user asks to CREATE, GENERATE, or WRITE code: DELEGATE: /create <type> <Name>\n"
            "- If the user asks to REVIEW or AUDIT code: DELEGATE: /review <file>\n"
            "- If the user asks to REFACTOR code: DELEGATE: /refactor <file> <instruction>\n"
            "Example: User says 'create a class UserDTO'. You MUST respond EXACTLY: DELEGATE: /create class UserDTO\n"
            "If you delegate, do not add any other text or explanations."
        )

        if system_prompt:
            system_prompt += delegation_instructions
        else:
            system_prompt = delegation_instructions.strip()

        response = self.context.llm.generate(user_prompt, system=system_prompt)

        # Verificar si el LLM decidió delegar
        match = re.search(r"DELEGATE:\s*(/\S+)\s*(.*)", response)
        if match:
            command = match.group(1).replace("/", "")
            arg = match.group(2).strip()

            console = Console()
            console.print(f"\n[bold yellow]Delegating to /{command}...[/bold yellow]")
            return self.context.agent_service.delegate(command, arg)

        return response
