"""
Agent Manager.
Manages agent registration and discovery.
"""


class AgentManager:
    def __init__(self):
        self._agents = {}

    def register(self, name: str, agent):
        self._agents[name] = agent

    def get(self, name: str):
        return self._agents.get(name)

    def list(self) -> list[str]:
        return sorted(self._agents.keys())
