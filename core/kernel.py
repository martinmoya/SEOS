"""
SEOS Kernel.
Orchestrates application lifecycle.
"""

from pathlib import Path

from rich.console import Console

from core.banner import show_banner
from core.logger import logger
from core.command_parser import CommandParser
from core.agent_context import AgentContext
from core.workspace import Workspace
from core.exceptions import SeosError

from factories.llm_factory import LLMFactory
from services.llm_service import LLMService
from services.workspace_service import WorkspaceService
from services.knowledge_service import KnowledgeService
from services.prompt_service import PromptService

from agents.chat_agent import ChatAgent
from agents.open_agent import OpenAgent
from agents.info_agent import InfoAgent
from agents.tree_agent import TreeAgent
from agents.find_agent import FindAgent
from agents.translate_agent import TranslateAgent
from agents.summarize_agent import SummarizeAgent
from agents.rewrite_agent import RewriteAgent
from agents.role_agent import RoleAgent
from agents.git_agent import GitAgent
from agents.symbols_agent import SymbolsAgent
from agents.test_agent import TestAgent
from agents.create_agent import CreateAgent
from agents.api_agent import ApiAgent
from agents.db_agent import DbAgent
from agents.refactor_agent import RefactorAgent
from agents.gentest_agent import GenTestAgent
from agents.review_agent import ReviewAgent
from agents.deploy_agent import DeployAgent
from agents.serve_agent import ServeAgent


class Kernel:
    def __init__(self):
        self.provider = None
        self.parser = CommandParser()
        self.agent_manager = {}
        self.console = Console()

    def initialize(self):
        show_banner()
        logger.info("Initializing SEOS...")

        self.provider = LLMFactory.create()
        self.provider.connect()

        if not self.provider.health():
            raise SeosError("Failed to connect to LLM provider.")

        logger.info(f"Provider connected: {self.provider.__class__.__name__}")

        knowledge_service = KnowledgeService(Path.cwd())
        knowledge_service.load()

        prompt_service = PromptService(knowledge_service)

        llm = LLMService(self.provider)
        workspace = Workspace()
        workspace_service = WorkspaceService(workspace)
        workspace_service.open(str(Path.cwd()))

        context = AgentContext(
            llm=llm,
            workspace_service=workspace_service,
            knowledge_service=knowledge_service,
            prompt_service=prompt_service,
        )

        self.agent_manager["chat"] = ChatAgent(context)
        self.agent_manager["open"] = OpenAgent(context)
        self.agent_manager["info"] = InfoAgent(context)
        self.agent_manager["tree"] = TreeAgent(context)
        self.agent_manager["find"] = FindAgent(context)
        self.agent_manager["translate"] = TranslateAgent(context)
        self.agent_manager["summarize"] = SummarizeAgent(context)
        self.agent_manager["rewrite"] = RewriteAgent(context)
        self.agent_manager["role"] = RoleAgent(context)
        self.agent_manager["git"] = GitAgent(context)
        self.agent_manager["symbols"] = SymbolsAgent(context)
        self.agent_manager["test"] = TestAgent(context)
        self.agent_manager["create"] = CreateAgent(context)
        self.agent_manager["create_api"] = ApiAgent(context)
        self.agent_manager["create_db"] = DbAgent(context)
        self.agent_manager["refactor"] = RefactorAgent(context)
        self.agent_manager["gentest"] = GenTestAgent(context)
        self.agent_manager["review"] = ReviewAgent(context)
        self.agent_manager["create_docker"] = DeployAgent(context)
        self.agent_manager["serve"] = ServeAgent(context)

        self.console.print(
            f"[bold green]✓ Knowledge loaded:[/bold green] {knowledge_service.get_stats()}"
        )
        self.console.print(
            "[bold green]✓ Provider connected successfully.[/bold green]\n"
        )

    def run(self):
        self.initialize()
        self.console.print(
            "Type [cyan]/help[/cyan] for available commands or [cyan]/exit[/cyan] to quit.\n"
        )

        while True:
            try:
                prompt = input("> ")
            except EOFError:
                break

            command, argument = self.parser.parse(prompt)

            if command in ["exit", "quit", "bye"]:
                break

            if command == "help":
                if argument:
                    agent = self.agent_manager.get(argument)
                    if agent:
                        self.console.print(
                            f"\n[cyan]/{argument}[/cyan]\n  {agent.description}\n"
                        )
                    else:
                        self.console.print(
                            f"\n[red]Unknown command:[/red] /{argument}\n"
                        )
                else:
                    self.console.print("\n[bold]Available commands:[/bold]")
                    for cmd in sorted(self.agent_manager.keys()):
                        self.console.print(f"  [cyan]/{cmd}[/cyan]")
                    self.console.print("  [cyan]/help[/cyan] [command]")
                    self.console.print("  [cyan]/exit[/cyan] (or /quit, /bye)\n")
                continue

            try:
                agent = self.agent_manager.get(command)
                if agent:
                    response = agent.execute(argument)
                    self.console.print(f"\n{response}\n")
                else:
                    self.console.print(f"\n[red]Unknown command:[/red] /{command}\n")
            except Exception as ex:
                logger.error(f"Error executing command {command}: {ex}")
                self.console.print(f"\n[bold red]ERROR:[/bold red] {ex}\n")

        self.shutdown()

    def shutdown(self):
        self.console.print("\n[yellow]Shutting down SEOS...[/yellow]")
        logger.info("SEOS terminated.")
