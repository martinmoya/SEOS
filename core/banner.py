"""
SEOS Banner.
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def show_banner():
    console = Console()
    title = Text("SEOS", style="bold cyan", justify="center")
    subtitle = Text(
        "Software Engineering Operating System", style="dim", justify="center"
    )

    content = Text.assemble(title, "\n", subtitle)
    console.print(Panel(content, border_style="cyan", padding=(1, 4)))
