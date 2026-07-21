"""
Diagram Agent.
"""

import re
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.diagram_generator import DiagramGenerator


class DiagramAgent(BaseProjectAgent):
    description = (
        "Generate a Mermaid.js diagram file. Usage: /create_diagram <description>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        if not argument.strip():
            return "Usage: /create_diagram <description>"

        generator = DiagramGenerator(self.context.llm)

        print("\nGenerating diagram... Please wait.\n")
        mermaid_code = generator.generate(argument)

        # Sanitizar nombre de archivo: quitar espacios y caracteres especiales
        words = argument.lower().split()[:3]
        clean_name = "_".join(re.sub(r"[^a-z0-9]", "", w) for w in words)
        if not clean_name:
            clean_name = "diagram"

        filename = f"diagram_{clean_name}.md"
        filepath = Path(project.root) / filename

        content = f"# Diagram\n\n```mermaid\n{mermaid_code}\n```"

        try:
            filepath.write_text(content, encoding="utf-8")
            return f"Successfully created diagram: {filename}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing file: {ex}"
