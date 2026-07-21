"""
Chat Agent.
"""

import re
from pathlib import Path
from rich.console import Console
from agents.base_agent import BaseAgent
from services.file_writer_service import FileWriterService


class ChatAgent(BaseAgent):
    description = (
        "Talk to the LLM. Autonomously executes file generation. Usage: /chat <message>"
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
                "Use the following code snippets to answer the user's question if relevant.\n\n"
                f"{vector_context}\n\n---\n"
            )
            if system_prompt:
                system_prompt += context_instruction
            else:
                system_prompt = context_instruction.strip()

            console = Console()
            console.print(
                "\n[dim yellow]💡 RAG Context injected from Vector DB.[/dim yellow]"
            )
        # -----------------------

        autonomous_instructions = (
            "\n\nCRITICAL ORCHESTRATION RULES:\n"
            "You are an autonomous AI engineer. If the user asks you to CREATE, GENERATE, WRITE, or MODIFY code or files:\n"
            "1. DO NOT respond with markdown code blocks in text.\n"
            "2. DO NOT explain the code.\n"
            "3. You MUST respond with a valid JSON array containing objects with 'path' and 'code' keys.\n"
            "Example response format:\n"
            '```json\n[\n  {"path": "src/models/user.py", "code": "class User:\\\\n    pass"}\n]\n```\n'
            "If the user asks a general question or wants an explanation, respond normally with text.\n"
        )

        if system_prompt:
            system_prompt += autonomous_instructions
        else:
            system_prompt = autonomous_instructions.strip()

        history = self.context.conversation_service.get_history()
        response = self.context.llm.generate(
            user_prompt, system=system_prompt, history=history
        )

        project = self.context.project
        if project:
            file_writer = FileWriterService(
                Path(project.root),
                self.context.audit_service,
                self.context.metrics_service,
            )
            # Pasamos el user_prompt para que el interceptor busque la ruta si el LLM fue terco
            execution_log = file_writer.process_response(response, user_prompt)

            if execution_log:
                self.context.conversation_service.add_message("user", user_prompt)
                self.context.conversation_service.add_message(
                    "assistant", execution_log
                )
                return execution_log

        self.context.conversation_service.add_message("user", user_prompt)
        self.context.conversation_service.add_message("assistant", response)

        return response
