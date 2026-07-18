"""
Prompt Service.
Builds prompts dynamically by injecting Roles and Rules.
"""

from services.knowledge_service import KnowledgeService


class PromptService:
    def __init__(self, knowledge_service: KnowledgeService):
        self.knowledge = knowledge_service
        self.current_role_name = None
        self.current_role_content = ""

    def set_role(self, role_name: str) -> str:
        role_content = self.knowledge.knowledge["roles"].get(role_name)
        if role_content:
            self.current_role_name = role_name
            self.current_role_content = role_content
            return f"Role successfully set to: {role_name}"
        available = ", ".join(self.knowledge.knowledge["roles"].keys())
        return f"Role '{role_name}' not found.\nAvailable roles: {available}"

    def clear_role(self) -> str:
        self.current_role_name = None
        self.current_role_content = ""
        return "Role cleared. SEOS is back to default chat mode."

    def get_current_role(self) -> str:
        return self.current_role_name or "None"

    def build_prompt(self, user_input: str) -> str:
        parts = []

        # 1. Inject Role if set
        if self.current_role_content:
            parts.append("You are adopting the following role:\n")
            parts.append(self.current_role_content)
            parts.append("\n---\n")

        # 2. Inject Global Rules
        global_rules = self.knowledge.knowledge["rules"].get("global_rules")
        if global_rules:
            parts.append("You must strictly adhere to these global rules:\n")
            parts.append(global_rules)
            parts.append("\n---\n")

        # 3. Add User Input
        parts.append("User query:")
        parts.append(user_input)

        return "\n".join(parts)
