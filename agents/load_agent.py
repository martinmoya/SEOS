"""
Load Agent.
Loads a large prompt from a text file and passes it to the ChatAgent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class LoadAgent(BaseProjectAgent):
    description = (
        "Load a large prompt from a text file and process it. Usage: /load <file>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /load <file>"

        filepath = Path(project.root) / filename

        if not filepath.exists() or filepath.is_dir():
            return f"File not found: {filename}"

        try:
            raw_text = filepath.read_text(encoding="utf-8")

            # Envolvemos el texto en un contexto seguro para que el ChatAgent
            # sepa que es una pregunta, no una instrucción de sistema.
            safe_prompt = (
                "The user has loaded the following text from a file to ask you a question. "
                "Please read it and respond to it conversationally. "
                "Do NOT delegate this to other agents unless the user explicitly asks you to write a file.\n\n"
                f"--- FILE CONTENT START ---\n{raw_text}\n--- FILE CONTENT END ---"
            )

            print(
                f"\n[dim]Loaded {len(raw_text)} characters from {filename}. Processing...[/dim]\n"
            )

            # Delegar al ChatAgent con el prompt seguro
            chat_agent = self.context.agent_service.agent_manager.get("chat")
            return chat_agent.execute(safe_prompt)
        except Exception as ex:
            return f"Error loading file: {ex}"
