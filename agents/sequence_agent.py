"""
Sequence Agent.
Generates a sequence diagram from an entry file.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.sequence_generator import SequenceGenerator


class SequenceAgent(BaseProjectAgent):
    description = "Generate a sequence diagram from a file. Usage: /sequence <file>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /sequence <file>"

        print(f"\nAnalyzing execution flow for {filename}... Please wait.\n")

        generator = SequenceGenerator(self.context.llm, Path(project.root))
        mermaid_code = generator.generate(filename)

        if not mermaid_code or "Error" in mermaid_code:
            return mermaid_code

        # Guardar en la raíz del proyecto para que se renderice en GitHub/VS Code
        filepath = Path(project.root) / f"sequence_{Path(filename).stem}.md"

        content = f"# Sequence Diagram: {filename}\n\n```mermaid\n{mermaid_code}\n```"

        try:
            filepath.write_text(content, encoding="utf-8")

            # Auditoría
            self.context.audit_service.log_action("CREATE", filepath)
            self.context.metrics_service.add_file_created()

            return f"Successfully generated sequence diagram: {filepath.name}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing diagram: {ex}"
