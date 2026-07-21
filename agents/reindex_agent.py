"""
Reindex Agent.
Manually triggers a full Vector DB reindex.
"""

from agents.base_agent import BaseAgent


class ReindexAgent(BaseAgent):
    description = "Force a full Vector DB reindex. Usage: /reindex"

    def execute(self, argument: str) -> str:
        print("\nReindexing Vector DB... Please wait.\n")
        self.context.vector_service.index_project()
        return f"Vector DB reindexed successfully.\n{self.context.vector_service.last_watcher_message}"
