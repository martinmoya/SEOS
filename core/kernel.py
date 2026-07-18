"""
SEOS Kernel.
Orchestrates application lifecycle.
"""

from core.banner import show_banner
from core.logger import logger
from core.command_parser import CommandParser
from core.agent_context import AgentContext
from core.exceptions import SeosError

from factories.llm_factory import LLMFactory
from services.llm_service import LLMService

from agents.chat_agent import ChatAgent


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
        context = AgentContext(llm=llm)

        self.agent_manager["chat"] = ChatAgent(context)
        self.agent_manager["exit"] = None  # Special case for breaking loop

        print("Provider connected successfully.\n")

    def run(self):
        self.initialize()
        print("Type '/exit' to quit.\n")

        while True:
            prompt = input("> ")
            command, argument = self.parser.parse(prompt)

            if command == "exit" or command == "quit" or command == "bye":
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
