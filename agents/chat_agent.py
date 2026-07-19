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

        delegation_instructions = (
            "\n\nCRITICAL ORCHESTRATION RULES:\n"
            "You are an orchestrator and a helpful assistant. You can delegate tasks to other agents using the EXACT format: DELEGATE: /<command> <argument>\n"
            "Available agents for delegation:\n"
            "- /create <type> <Name>: ONLY when the user explicitly asks to CREATE, GENERATE, or WRITE a code file.\n"
            "- /review <file>: ONLY when the user explicitly asks to REVIEW or AUDIT a specific code file.\n"
            "- /refactor <file> <instruction>: ONLY when the user explicitly asks to REFACTOR a specific file.\n"
            "- /translate <file> <lang>: ONLY when the user explicitly asks to TRANSLATE a document.\n"
            "IMPORTANT: If the user is greeting you, asking general questions, or discussing concepts, DO NOT DELEGATE. Respond directly to the user.\n"
            "If you delegate, do not add any other text or explanations. Example: User says 'create a class UserDTO'. You MUST respond EXACTLY: DELEGATE: /create class UserDTO"
        )

        if system_prompt:
            system_prompt += delegation_instructions
        else:
            system_prompt = delegation_instructions.strip()

        # Obtenemos el historial de la conversación
        history = self.context.conversation_service.get_history()

        response = self.context.llm.generate(
            user_prompt, system=system_prompt, history=history
        )

        # Verificar si el LLM decidió delegar
        match = re.search(r"DELEGATE:\s*(/\S+)\s*(.*)", response)
        if match:
            command = match.group(1).replace("/", "")
            arg = match.group(2).strip()

            # Verificamos que el agente realmente exista antes de delegar
            if not self.context.agent_service.agent_manager.get(command):
                return response  # Si inventó un agente, devolvemos la respuesta normal

            console = Console()
            console.print(f"\n[bold yellow]Delegating to /{command}...[/bold yellow]")
            final_response = self.context.agent_service.delegate(command, arg)

            # Guardamos en memoria lo que el usuario pidió y el resultado de la delegación
            self.context.conversation_service.add_message("user", user_prompt)
            self.context.conversation_service.add_message("assistant", final_response)

            return final_response

        # Si es una respuesta normal de chat, la guardamos en memoria
        self.context.conversation_service.add_message("user", user_prompt)
        self.context.conversation_service.add_message("assistant", response)

        return response
