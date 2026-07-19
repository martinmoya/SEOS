"""
Agent Service.
Enables inter-agent communication and delegation.
"""

from managers.agent_manager import AgentManager


class AgentService:
    def __init__(self, agent_manager: AgentManager):
        self.agent_manager = agent_manager

    def delegate(self, command: str, argument: str) -> str:
        agent = self.agent_manager.get(command)
        if agent:
            return agent.execute(argument)
        return f"Error: Agent '{command}' not found."
