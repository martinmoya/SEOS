"""
Audit Agent.
Displays the recent file modification history.
"""

from pathlib import Path
from agents.base_agent import BaseAgent


class AuditAgent(BaseAgent):
    description = "Show recent file modifications made by SEOS. Usage: /audit"

    def execute(self, argument: str) -> str:
        log_path = Path("logs/audit.jsonl")
        if not log_path.exists():
            return "No audit records found."

        lines = log_path.read_text(encoding="utf-8").strip().splitlines()
        if not lines:
            return "No audit records found."

        # Mostrar las últimas 10 acciones
        recent = lines[-10:]
        output = ["--- Recent Audit Log ---"]
        for line in recent:
            output.append(line)

        return "\n".join(output)
