"""
Save Agent.
Saves the last chat response to a file.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent


class SaveAgent(BaseProjectAgent):
    description = "Save the last response to a file. Usage: /save <filename>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /save <filename>"

        # Obtener el historial de conversación
        history = self.context.conversation_service.get_history()
        if not history:
            return "There is no recent response to save."

        # La última respuesta del asistente es el último elemento del historial
        last_response = history[-1].get("content", "")

        # Guardar en projects/
        target_dir = Path(project.root) / "projects"
        target_dir.mkdir(parents=True, exist_ok=True)

        filepath = target_dir / filename

        try:
            filepath.write_text(last_response, encoding="utf-8")
            return f"Successfully saved last response to: {filepath}"
        except Exception as ex:
            return f"Error saving file: {ex}"
