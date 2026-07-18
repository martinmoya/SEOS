"""
Knowledge Service.
Loads and caches SEOS knowledge base (Roles, Rules, Capabilities).
Supports nested directories (e.g., capabilities/Languages/python.md).
"""

from pathlib import Path
from core.logger import logger


class KnowledgeService:
    def __init__(self, root: Path):
        self.root = root / "knowledge"
        self.knowledge = {"roles": {}, "rules": {}, "capabilities": {}}

    def load(self) -> dict:
        if not self.root.exists():
            logger.warning(f"Knowledge directory not found at {self.root}")
            return self.knowledge

        for category in self.knowledge.keys():
            cat_dir = self.root / category
            if cat_dir.exists():
                # Usamos rglob para buscar recursivamente en todas las subcarpetas
                for file in cat_dir.rglob("*.md"):
                    # Ej: "Languages/python_skill" o solo "python_skill"
                    relative_path = file.relative_to(cat_dir)
                    key = str(relative_path.with_suffix("")).replace("\\", "/")
                    self.knowledge[category][key] = file.read_text(encoding="utf-8")

        logger.info(f"Knowledge loaded: {self.get_stats()}")
        return self.knowledge

    def get_stats(self) -> str:
        roles = len(self.knowledge["roles"])
        rules = len(self.knowledge["rules"])
        caps = len(self.knowledge["capabilities"])
        return f"{roles} roles, {rules} rules, {caps} capabilities"

    def get_context(self) -> str:
        """Builds a string representation of the knowledge for LLM prompts."""
        lines = []
        for category, items in self.knowledge.items():
            if items:
                lines.append(f"--- {category.upper()} ---")
                for name, content in items.items():
                    # Solo incluimos el nombre del archivo para no saturar el prompt
                    lines.append(f"[{name}]")
                lines.append("")
        return "\n".join(lines)
