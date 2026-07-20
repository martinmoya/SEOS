"""
MCP Client.
Connects to external Model Context Protocol servers via JSON-RPC (stdio).
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict


class MCPClient:
    def __init__(self):
        self.processes: Dict[str, subprocess.Popen] = {}

    def load_config(self) -> dict:
        config_path = Path("mcp_config.json")
        if not config_path.exists():
            return {}
        return json.loads(config_path.read_text(encoding="utf-8"))

    def start_server(self, name: str):
        config = self.load_config()
        if name not in config:
            return False, f"Server '{name}' not found in mcp_config.json"

        server_conf = config[name]
        cmd = server_conf.get("command")
        args = server_conf.get("args", [])

        try:
            # En Windows, necesitamos usar shell=True para que encuentre 'npx' o 'npx.cmd'
            if sys.platform == "win32":
                full_cmd = subprocess.list2cmdline([cmd] + args)
                proc = subprocess.Popen(
                    full_cmd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    bufsize=1,
                    shell=True,
                )
            else:
                proc = subprocess.Popen(
                    [cmd] + args,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    bufsize=1,
                )

            self.processes[name] = proc

            # Enviar petición 'initialize'
            init_req = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "seos", "version": "1.8.0"},
                },
            }
            self._send(name, init_req)
            self._read(name)  # Leer respuesta initialize

            # Enviar notificación 'initialized'
            notif = {"jsonrpc": "2.0", "method": "notifications/initialized"}
            self._send(name, notif)

            return True, f"Server '{name}' started successfully."
        except Exception as ex:
            return False, f"Failed to start server '{name}': {ex}"

    def list_tools(self, server_name: str):
        if server_name not in self.processes:
            success, msg = self.start_server(server_name)
            if not success:
                return msg

        req = {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}
        self._send(server_name, req)
        resp = self._read(server_name)

        if resp and "result" in resp:
            return resp["result"].get("tools", [])
        return resp.get("error", "Failed to list tools.")

    def call_tool(self, server_name: str, tool_name: str, arguments: dict):
        if server_name not in self.processes:
            success, msg = self.start_server(server_name)
            if not success:
                return msg

        req = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": arguments},
        }
        self._send(server_name, req)
        resp = self._read(server_name)

        if resp and "result" in resp:
            return resp["result"]
        return resp.get("error", "Failed to call tool.")

    def _send(self, name: str, payload: dict):
        proc = self.processes.get(name)
        if proc and proc.stdin:
            proc.stdin.write(json.dumps(payload) + "\n")
            proc.stdin.flush()

    def _read(self, name: str) -> dict:
        proc = self.processes.get(name)
        if proc and proc.stdout:
            line = proc.stdout.readline()
            if line:
                try:
                    return json.loads(line)
                except json.JSONDecodeError:
                    return {"error": "Invalid JSON response from server"}
        return {"error": "No response from server"}

    def stop_all(self):
        for name, proc in self.processes.items():
            if proc.poll() is None:
                proc.terminate()
