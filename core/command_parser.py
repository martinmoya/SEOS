"""
Command Parser.
Parses user input into commands, arguments, and output redirection.
"""


class CommandParser:
    def parse(self, text: str) -> tuple[str, str, str | None]:
        text = text.strip()
        if not text:
            return "chat", "", None

        if not text.startswith("/"):
            return "chat", text, None

        parts = text.split(maxsplit=1)
        command = parts[0][1:].strip().lower()
        rest = parts[1].strip() if len(parts) > 1 else ""

        redirect_file = None
        if ">" in rest:
            cmd_parts = rest.split(">", 1)
            argument = cmd_parts[0].strip()
            redirect_file = cmd_parts[1].strip()
        else:
            argument = rest

        return command, argument, redirect_file
