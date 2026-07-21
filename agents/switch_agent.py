"""
Switch Agent.
Switches the active project.
"""

from pathlib import Path
from agents.base_agent import BaseAgent


class SwitchAgent(BaseAgent):
    description = "Switch to an open project. Usage: /switch <project_name>"

    def execute(self, argument: str) -> str:
        name = argument.strip()
        if not name:
            return "Usage: /switch <project_name>"

        result = self.context.workspace_service.switch(name)

        if "Switched" in result:
            current_project = self.context.workspace_service.current()
            if current_project:
                # Usamos .root que es el atributo estándar de Project
                new_root = Path(current_project.root)

                # Protección: No indexar unidades enteras como C:\
                if new_root == Path("C:\\") or new_root.parent == new_root:
                    return (
                        result
                        + "\n[yellow]Warning: Skipped RAG indexing for root drive to prevent system freeze.[/yellow]"
                    )

                print("\n[dim]Reindexing Vector DB for new project...[/dim]")
                self.context.vector_service.root = new_root
                self.context.vector_service.index_project()

        return result
