"""
Command Parser.
Parses user input into commands and arguments.
"""


class CommandParser:
    def parse(self, text: str):
        text = text.strip()
        if not text:
            return "chat", ""

        if not text.startswith("/"):
            return "chat", text

        parts = text.split(maxsplit=1)
        command = parts[0][1:].strip().lower()
        argument = parts[1].strip() if len(parts) > 1 else ""

        return command, argument
