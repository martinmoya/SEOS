"""
Example SEOS Plugin.
"""

from agents.base_agent import BaseAgent


class ExampleAgent(BaseAgent):
    description = "An example plugin agent. Usage: /example"

    def execute(self, argument: str) -> str:
        return "Hello from the Example Plugin! I am running outside the SEOS core."


def register_plugin(agent_manager, context):
    """This function is called by PluginManager to register the plugin's agents."""
    agent_manager.register("example", ExampleAgent(context))
