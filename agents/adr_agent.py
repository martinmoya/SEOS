"""
ADR Agent.
Generates Architecture Decision Records from Git history.
"""

from datetime import datetime
from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.adr_generator import AdrGenerator


class AdrAgent(BaseProjectAgent):
    description = "Generate an ADR from recent Git commits. Usage: /adr"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        print("\nAnalyzing Git history and generating ADR... Please wait.\n")

        generator = AdrGenerator(self.context.llm)
        markdown_content = generator.generate_from_git(Path(project.root))

        # Guardar en SEOS-docs/architecture/
        docs_dir = Path("SEOS-docs/architecture")
        docs_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ADR_{timestamp}.md"
        filepath = docs_dir / filename

        try:
            filepath.write_text(
                f"# ADR: Auto-Generated {timestamp}\n\n{markdown_content}",
                encoding="utf-8",
            )

            # Auditoría y Métricas
            self.context.audit_service.log_action("CREATE", filepath)
            self.context.metrics_service.add_file_created()

            return f"Successfully generated ADR: {filename}\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing ADR: {ex}"
