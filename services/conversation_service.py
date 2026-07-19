"""
Conversation Service.
Manages short-term conversational memory for agents.
"""


class ConversationService:
    def __init__(self):
        self._history: list[dict] = []

    def add_message(self, role: str, content: str) -> None:
        """Adds a message to the conversation history."""
        self._history.append({"role": role, "content": content})

    def get_history(self) -> list[dict]:
        """Returns the conversation history."""
        return self._history

    def clear(self) -> None:
        """Clears the conversation history."""
        self._history.clear()
