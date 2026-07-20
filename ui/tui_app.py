"""
SEOS TUI Application.
Full-screen terminal user interface built with Textual.
"""

import os
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, RichLog, Tree
from textual.containers import Horizontal


class SeosApp(App):
    CSS = """
    Screen {
        layout: vertical;
    }
    #main {
        height: 1fr;
    }
    #tree-view {
        width: 30%;
        border: round cyan;
        padding: 1;
    }
    #chat-view {
        width: 70%;
        border: round green;
        padding: 1;
    }
    Input {
        dock: bottom;
        border: solid white;
    }
    """

    def __init__(self, kernel):
        super().__init__()
        self.kernel = kernel

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="main"):
            yield Tree("SEOS Project", id="tree-view")
            yield RichLog(id="chat-view", markup=True)
        yield Input(
            placeholder="Enter command (e.g., /help or /chat Hello)", id="cmd-input"
        )
        yield Footer()

    def on_mount(self) -> None:
        self.title = "SEOS"
        self.sub_title = "Software Engineering Operating System"
        self.build_tree()
        chat = self.query_one("#chat-view")
        chat.write("[bold green]✓ Provider connected successfully.[/bold green]")
        chat.write(
            "Type [cyan]/help[/cyan] for available commands or [cyan]/exit[/cyan] to quit.\n"
        )
        self.query_one("#cmd-input").focus()

    def build_tree(self):
        tree = self.query_one("#tree-view")
        tree.root.expand()
        root_path = os.getcwd()

        # Construir árbol de directorios (1 nivel de profundidad para no congelar la UI)
        for item in sorted(os.listdir(root_path)):
            if item.startswith(".") or item in [
                "node_modules",
                "__pycache__",
                ".seos_vector_db",
                "logs",
                "projects",
            ]:
                continue
            full_path = os.path.join(root_path, item)
            if os.path.isdir(full_path):
                # En Textual, se usa .add() para crear una rama
                branch = tree.root.add(item, allow_expand=True)
                try:
                    for sub_item in sorted(os.listdir(full_path)):
                        if sub_item.startswith(".") or sub_item == "__pycache__":
                            continue
                        branch.add_leaf(sub_item)
                except PermissionError:
                    pass
            else:
                tree.root.add_leaf(item)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd_text = event.value.strip()
        self.query_one("#cmd-input").value = ""

        if not cmd_text:
            return

        chat = self.query_one("#chat-view")
        chat.write(f"\n[bold blue]> {cmd_text}[/bold blue]")

        if cmd_text.lower() in ["/exit", "/quit", "/bye"]:
            self.exit()
            return

        command, argument = self.kernel.parser.parse(cmd_text)

        if command == "help":
            if argument:
                agent = self.kernel.agent_manager.get(argument)
                if agent:
                    chat.write(f"[cyan]/{argument}[/cyan]\n  {agent.description}")
                else:
                    chat.write(f"[red]Unknown command:[/red] /{argument}")
            else:
                chat.write("[bold]Available commands:[/bold]")
                for cmd in sorted(self.kernel.agent_manager.list()):
                    chat.write(f"  [cyan]/{cmd}[/cyan]")
                chat.write("  [cyan]/help[/cyan] [command]")
                chat.write("  [cyan]/exit[/cyan] (or /quit, /bye)")
            return

        agent = self.kernel.agent_manager.get(command)
        if agent:
            try:
                response = agent.execute(argument)
                chat.write(response)
            except Exception as ex:
                chat.write(f"[bold red]ERROR:[/bold red] {ex}")
        else:
            chat.write(f"[red]Unknown command:[/red] /{command}")
