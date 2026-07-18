"""
Agent Context.
Provides shared services to every SEOS agent.
"""

from services.llm_service import LLMService
from services.workspace_service import WorkspaceService
from services.knowledge_service import KnowledgeService


class AgentContext:
    def __init__(
        self,
        llm: LLMService,
        workspace_service: WorkspaceService,
        knowledge_service: KnowledgeService,
    ):
        self.llm = llm
        self.workspace_service = workspace_service
        self.knowledge_service = knowledge_service

    @property
    def project(self):
        return self.workspace_service.current()
