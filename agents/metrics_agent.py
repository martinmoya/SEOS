"""
Metrics Agent.
Displays current session statistics.
"""

from agents.base_agent import BaseAgent


class MetricsAgent(BaseAgent):
    description = "Show current session metrics. Usage: /metrics"

    def execute(self, argument: str) -> str:
        stats = self.context.metrics_service.get_stats()
        return f"--- Session Metrics ---\n{stats}"
