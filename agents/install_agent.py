"""
Install Agent.
Clones a plugin from a GitHub URL and loads it dynamically.
"""

import subprocess
from pathlib import Path
from rich.console import Console
from agents.base_agent import BaseAgent


class InstallAgent(BaseAgent):
    description = "Install a plugin from a URL. Usage: /install <github_url>"

    def execute(self, argument: str) -> str:
        url = argument.strip()
        if not url or not url.startswith("http"):
            return "Usage: /install <github_url> (must start with http/https)"

        console = Console()
        plugins_dir = Path("plugins")
        plugins_dir.mkdir(exist_ok=True)

        # Extraer el nombre del repo para la carpeta local
        repo_name = url.split("/")[-1].replace(".git", "")
        target_dir = plugins_dir / repo_name

        if target_dir.exists():
            return f"Plugin '{repo_name}' is already installed in plugins/{repo_name}."

        try:
            console.print(f"\n[bold blue]Cloning {repo_name} from URL...[/bold blue]")
            # Clonar silenciosamente
            result = subprocess.run(
                ["git", "clone", url, str(target_dir)],
                capture_output=True,
                text=True,
                check=True,
            )

            # Cargar el plugin en caliente usando el PluginManager
            from core.plugin_manager import PluginManager

            pm = PluginManager()
            loaded = pm.load_plugins(
                self.context.agent_service.agent_manager, self.context
            )

            if repo_name in loaded:
                return f"✅ Plugin '{repo_name}' installed and loaded successfully!"
            else:
                return f"Plugin cloned to {target_dir}, but failed to load. Ensure it has a plugin.py with a register_plugin() function."

        except subprocess.CalledProcessError as ex:
            return f"Git clone failed: {ex.stderr}"
        except Exception as ex:
            return f"Error installing plugin: {ex}"
