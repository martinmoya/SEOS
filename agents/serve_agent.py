"""
Serve Agent.
Starts the SEOS REST API server.
"""

import uvicorn
from rich.console import Console
from agents.base_agent import BaseAgent


class ServeAgent(BaseAgent):
    description = "Start the SEOS REST API server. Usage: /serve"

    def execute(self, argument: str) -> str:
        console = Console()
        try:
            console.print(
                "\n[bold yellow]Starting SEOS REST API server...[/bold yellow]"
            )
            console.print("[dim]Press CTRL+C to stop the server.[/dim]\n")
            uvicorn.run(
                "api.rest_app:app", host="127.0.0.1", port=8080, log_level="info"
            )
            return "API server stopped."
        except Exception as ex:
            return f"Failed to start API server: {ex}"
