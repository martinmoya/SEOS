"""
List Agent.
Lists registered roles, rules, and capabilities.
"""

from agents.base_agent import BaseAgent


class ListAgent(BaseAgent):
    description = (
        "List registered knowledge. Usage: /list <roles|rules|capabilities> [area]"
    )

    def execute(self, argument: str) -> str:
        parts = argument.split()
        if not parts:
            return "Usage: /list <roles|rules|capabilities> [area]"

        category = parts[0].lower()
        area = parts[1].lower() if len(parts) > 1 else None

        knowledge = self.context.knowledge_service.knowledge

        if category not in knowledge:
            return f"Invalid category: '{category}'. Valid options: roles, rules, capabilities."

        items = knowledge[category]

        # Filtrar por área si es capabilities
        if category == "capabilities" and area:
            items = {
                k: v for k, v in items.items() if k.lower().startswith(area.lower())
            }

        if not items:
            return f"No items found for {category} {area or ''}."

        header = f"--- {category.upper()} ({area if area else 'all'}) ---"
        body = "\n".join(f"- {k}" for k in sorted(items.keys()))

        return f"{header}\n{body}"
