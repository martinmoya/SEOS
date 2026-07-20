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
from services.agent_service import AgentService
from services.conversation_service import ConversationService
from services.vector_service import VectorService

from managers.agent_manager import AgentManager

from agents.chat_agent import ChatAgent
from agents.open_agent import OpenAgent
from agents.info_agent import InfoAgent
from agents.tree_agent import TreeAgent
from agents.find_agent import FindAgent
from agents.read_agent import ReadAgent
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
from agents.github_agent import GithubAgent
from agents.diagram_agent import DiagramAgent
from agents.example_agent import ExampleAgent
from agents.migrate_agent import MigrateAgent
from agents.sprint_agent import SprintAgent
from agents.ocr_agent import OcrAgent
from agents.mcp_agent import McpAgent

from ui.tui_app import SeosApp


class Kernel:
    def __init__(self):
        self.provider = None
        self.parser = CommandParser()
        self.agent_manager = AgentManager()
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
        conversation_service = ConversationService()

        self.console.print(
            "[bold blue]Indexing project for RAG (Vector DB)...[/bold blue]"
        )
        vector_service = VectorService(Path.cwd())
        vector_service.index_project()

        llm = LLMService(self.provider)
        workspace = Workspace()
        workspace_service = WorkspaceService(workspace)
        workspace_service.open(str(Path.cwd()))

        agent_service = AgentService(self.agent_manager)

        context = AgentContext(
            llm=llm,
            workspace_service=workspace_service,
            knowledge_service=knowledge_service,
            prompt_service=prompt_service,
            agent_service=agent_service,
            conversation_service=conversation_service,
            vector_service=vector_service,
        )

        self.agent_manager.register("chat", ChatAgent(context))
        self.agent_manager.register("open", OpenAgent(context))
        self.agent_manager.register("info", InfoAgent(context))
        self.agent_manager.register("tree", TreeAgent(context))
        self.agent_manager.register("find", FindAgent(context))
        self.agent_manager.register("read", ReadAgent(context))
        self.agent_manager.register("translate", TranslateAgent(context))
        self.agent_manager.register("summarize", SummarizeAgent(context))
        self.agent_manager.register("rewrite", RewriteAgent(context))
        self.agent_manager.register("role", RoleAgent(context))
        self.agent_manager.register("git", GitAgent(context))
        self.agent_manager.register("symbols", SymbolsAgent(context))
        self.agent_manager.register("test", TestAgent(context))
        self.agent_manager.register("create", CreateAgent(context))
        self.agent_manager.register("create_api", ApiAgent(context))
        self.agent_manager.register("create_db", DbAgent(context))
        self.agent_manager.register("refactor", RefactorAgent(context))
        self.agent_manager.register("gentest", GenTestAgent(context))
        self.agent_manager.register("review", ReviewAgent(context))
        self.agent_manager.register("create_docker", DeployAgent(context))
        self.agent_manager.register("serve", ServeAgent(context))
        self.agent_manager.register("github", GithubAgent(context))
        self.agent_manager.register("create_diagram", DiagramAgent(context))
        self.agent_manager.register("create_example", ExampleAgent(context))
        self.agent_manager.register("migrate", MigrateAgent(context))
        self.agent_manager.register("sprint", SprintAgent(context))
        self.agent_manager.register("ocr", OcrAgent(context))
        self.agent_manager.register("mcp", McpAgent(context))

        self.console.print(
            f"[bold green]✓ Knowledge loaded:[/bold green] {knowledge_service.get_stats()}"
        )
        self.console.print(
            "[bold green]✓ Provider connected successfully.[/bold green]"
        )
        self.console.print("[bold blue]Starting TUI...[/bold blue]")

    def run(self):
        try:
            self.initialize()
        except Exception as ex:
            self.console.print(
                f"\n[bold red]FATAL ERROR DURING INITIALIZATION:[/bold red] {ex}\n"
            )
            logger.critical(f"Initialization failed: {ex}")
            return

        app = SeosApp(kernel=self)
        app.run()

        self.shutdown()

    def shutdown(self):
        print("\nShutting down SEOS...")
        logger.info("SEOS terminated.")
