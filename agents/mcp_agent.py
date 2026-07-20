"""
MCP Agent.
Interacts with external MCP servers.
"""

import json
from agents.base_agent import BaseAgent
from services.mcp_client import MCPClient


class McpAgent(BaseAgent):
    description = (
        "Interact with MCP servers. Usage: /mcp <list|call> <server> [tool] [args_json]"
    )

    def __init__(self, context):
        super().__init__(context)
        self.client = MCPClient()

    def execute(self, argument: str) -> str:
        parts = argument.split(maxsplit=3)
        if not parts:
            return self.description

        action = parts[0]

        if action == "list":
            if len(parts) < 2:
                return "Usage: /mcp list <server_name>"
            server_name = parts[1]
            tools = self.client.list_tools(server_name)
            return json.dumps(tools, indent=2)

        elif action == "call":
            if len(parts) < 4:
                return "Usage: /mcp call <server_name> <tool_name> <args_json>"

            server_name = parts[1]
            tool_name = parts[2]
            try:
                args = json.loads(parts[3])
            except json.JSONDecodeError:
                return "Invalid JSON arguments."

            result = self.client.call_tool(server_name, tool_name, args)
            return json.dumps(result, indent=2)

        return "Unknown action. Use 'list' or 'call'."
