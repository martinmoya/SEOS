"""
Agent Context.
Provides shared services to every SEOS agent.
"""

from services.llm_service import LLMService
from services.workspace_service import WorkspaceService
from services.knowledge_service import KnowledgeService
from services.prompt_service import PromptService
from services.agent_service import AgentService


class AgentContext:
    def __init__(
        self,
        llm: LLMService,
        workspace_service: WorkspaceService,
        knowledge_service: KnowledgeService,
        prompt_service: PromptService,
        agent_service: AgentService,
    ):
        self.llm = llm
        self.workspace_service = workspace_service
        self.knowledge_service = knowledge_service
        self.prompt_service = prompt_service
        self.agent_service = agent_service

    @property
    def project(self):
        return self.workspace_service.current()
