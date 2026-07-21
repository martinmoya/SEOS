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

        # --- RAG Integration ---
        vector_context = self.context.vector_service.query(user_prompt)
        if vector_context:
            context_instruction = (
                "\n\nPROJECT CONTEXT (Retrieved from local codebase):\n"
                "Use the following code snippets to answer the user's question if relevant. "
                "Ignore it if the question is general.\n\n"
                f"{vector_context}\n\n---\n"
            )
            if system_prompt:
                system_prompt += context_instruction
            else:
                system_prompt = context_instruction.strip()

            # Aviso visual para saber que el RAG funcionó
            console = Console()
            console.print(
                "\n[dim yellow]💡 RAG Context injected from Vector DB.[/dim yellow]"
            )
        # -----------------------

        delegation_instructions = (
            "\n\nCRITICAL ORCHESTRATION RULES:\n"
            "You are an orchestrator and a helpful assistant. You can delegate tasks to other agents using the EXACT format: DELEGATE: /<command> <argument>\n"
            "Available agents for delegation:\n"
            "- /create <type> <Name>: ONLY when the user explicitly asks to CREATE, GENERATE, or WRITE a code file.\n"
            "- /review <file>: ONLY when the user explicitly asks to REVIEW or AUDIT a specific code file.\n"
            "- /refactor <file> <instruction>: ONLY when the user explicitly asks to REFACTOR a specific file.\n"
            "- /translate <file> <lang>: ONLY when the user explicitly asks to TRANSLATE a document.\n"
            "IMPORTANT: If the user is greeting you, asking general questions, or discussing concepts, DO NOT DELEGATE. Respond directly.\n"
            "If you delegate, do not add any other text or explanations. Example: User says 'create a class UserDTO'. You MUST respond EXACTLY: DELEGATE: /create class UserDTO"
        )

        if system_prompt:
            system_prompt += delegation_instructions
        else:
            system_prompt = delegation_instructions.strip()

        history = self.context.conversation_service.get_history()
        response = self.context.llm.generate(
            user_prompt, system=system_prompt, history=history
        )

        match = re.search(r"DELEGATE:\s*(/\S+)\s*(.*)", response)
        if match:
            command = match.group(1).replace("/", "")
            arg = match.group(2).strip()

            if not self.context.agent_service.agent_manager.get(command):
                return response

            console = Console()
            console.print(f"\n[bold yellow]Delegating to /{command}...[/bold yellow]")
            final_response = self.context.agent_service.delegate(command, arg)

            self.context.conversation_service.add_message("user", user_prompt)
            self.context.conversation_service.add_message("assistant", final_response)

            return final_response

        self.context.conversation_service.add_message("user", user_prompt)
        self.context.conversation_service.add_message("assistant", response)

        return response
