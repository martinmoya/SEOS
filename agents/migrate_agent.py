"""
Migrate Agent.
Translates code files from one language to another.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.migration_engine import MigrationEngine


class MigrateAgent(BaseProjectAgent):
    description = "Migrate a code file to another language. Usage: /migrate <file> <target_language>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        parts = argument.split()
        if len(parts) != 2:
            return "Usage: /migrate <file> <target_language> (e.g., /migrate login.java python)"

        filename = parts[0]
        target_lang = parts[1]

        source_path = Path(project.root) / filename

        if not source_path.exists():
            return f"File not found: {filename}"

        print(f"\nMigrating {filename} to {target_lang}... Please wait.\n")

        engine = MigrationEngine(self.context.llm)
        return engine.migrate(source_path, target_lang)
