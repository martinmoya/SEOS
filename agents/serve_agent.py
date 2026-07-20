"""
Serve Agent.
Starts the SEOS REST API server in a background thread.
"""

import threading
import uvicorn
from rich.console import Console
from agents.base_agent import BaseAgent


class ServeAgent(BaseAgent):
    description = "Start the SEOS REST API server. Usage: /serve"

    def execute(self, argument: str) -> str:
        console = Console()
        try:
            config = uvicorn.Config(
                "api.rest_app:app", host="127.0.0.1", port=8080, log_level="info"
            )
            server = uvicorn.Server(config)

            # Arrancar el servidor en un hilo separado para no bloquear la TUI
            thread = threading.Thread(target=server.run, daemon=True)
            thread.start()

            return "API server started in background on http://127.0.0.1:8080.\nYou can now use the VS Code Extension."
        except Exception as ex:
            return f"Failed to start API server: {ex}"
