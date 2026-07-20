"""
Plugin Manager.
Discovers and loads external agents and skills from the plugins/ directory.
"""

import importlib.util
import sys
from pathlib import Path
from core.logger import logger


class PluginManager:
    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = Path(plugins_dir)

    def load_plugins(self, agent_manager, context) -> list[str]:
        if not self.plugins_dir.exists():
            return []

        loaded_plugins = []

        # Buscar todas las carpetas dentro de plugins/
        for plugin_dir in self.plugins_dir.iterdir():
            if not plugin_dir.is_dir() or plugin_dir.name.startswith("_"):
                continue

            plugin_file = plugin_dir / "plugin.py"
            if not plugin_file.exists():
                continue

            try:
                # Cargar dinámicamente el módulo del plugin
                module_name = f"plugins.{plugin_dir.name}.plugin"
                spec = importlib.util.spec_from_file_location(module_name, plugin_file)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                # Si el módulo tiene la función register_plugin, la ejecutamos
                if hasattr(module, "register_plugin"):
                    module.register_plugin(agent_manager, context)
                    loaded_plugins.append(plugin_dir.name)
                    logger.info(f"Loaded plugin: {plugin_dir.name}")
            except Exception as ex:
                logger.error(f"Failed to load plugin {plugin_dir.name}: {ex}")

        return loaded_plugins
