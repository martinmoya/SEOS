"""
SEOS Kernel.
Orchestrates application lifecycle.
"""

from pathlib import Path

from core.banner import show_banner
from core.logger import logger
from core.command_parser import CommandParser
from core.agent_context import AgentContext
from core.workspace import Workspace
from core.exceptions import SeosError

from factories.llm_factory import LLMFactory
from services.llm_service import LLMService
from services.workspace_service import WorkspaceService

from agents.chat_agent import ChatAgent
from agents.open_agent import OpenAgent
from agents.info_agent import InfoAgent
from agents.tree_agent import TreeAgent
from agents.find_agent import FindAgent


class Kernel:
    def __init__(self):
        self.provider = None
        self.parser = CommandParser()
        self.agent_manager = {}

    def initialize(self):
        show_banner()
        logger.info("Initializing SEOS...")

        self.provider = LLMFactory.create()
        self.provider.connect()

        if not self.provider.health():
            raise SeosError("Failed to connect to LLM provider.")

        logger.info(f"Provider connected: {self.provider.__class__.__name__}")

        llm = LLMService(self.provider)
        workspace = Workspace()
        workspace_service = WorkspaceService(workspace)

        # Open current directory by default
        workspace_service.open(str(Path.cwd()))

        context = AgentContext(llm=llm, workspace_service=workspace_service)

        self.agent_manager["chat"] = ChatAgent(context)
        self.agent_manager["open"] = OpenAgent(context)
        self.agent_manager["info"] = InfoAgent(context)
        self.agent_manager["tree"] = TreeAgent(context)
        self.agent_manager["find"] = FindAgent(context)

        print("Provider connected successfully.\n")

    def run(self):
        self.initialize()
        print("Type '/exit' to quit.\n")

        while True:
            prompt = input("> ")
            command, argument = self.parser.parse(prompt)

            if command in ["exit", "quit", "bye"]:
                break

            try:
                agent = self.agent_manager.get(command)
                if agent:
                    response = agent.execute(argument)
                    print(f"\n{response}\n")
                else:
                    print(f"\nUnknown command: /{command}\n")
            except Exception as ex:
                logger.error(f"Error executing command {command}: {ex}")
                print(f"\nERROR: {ex}\n")

        self.shutdown()

    def shutdown(self):
        print("\nShutting down SEOS...")
        logger.info("SEOS terminated.")
