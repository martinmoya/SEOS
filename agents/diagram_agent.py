"""
Diagram Agent.
Generates and saves Mermaid.js diagrams in Markdown files.
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

        # Nombre de archivo basado en las primeras palabras
        words = argument.lower().split()[:3]
        filename = (
            "diagram_" + "_".join(re.sub(r"[^a-z0-9]", "", w) for w in words) + ".md"
        )
        filepath = Path(project.root) / filename

        # Guardar como Markdown para que se renderice en GitHub/VS Code
        content = f"# Diagram\n\n```mermaid\n{mermaid_code}\n```"

        try:
            filepath.write_text(content, encoding="utf-8")
            return f"Successfully created diagram: {filename}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing file: {ex}"
