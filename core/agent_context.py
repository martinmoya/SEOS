"""
Agent Context.
Provides shared services to every SEOS agent.
"""

from services.llm_service import LLMService
from services.workspace_service import WorkspaceService
from services.knowledge_service import KnowledgeService
from services.prompt_service import PromptService
from services.agent_service import AgentService
from services.conversation_service import ConversationService
from services.vector_service import VectorService
from services.metrics_service import MetricsService
from services.audit_service import AuditService


class AgentContext:
    def __init__(
        self,
        llm: LLMService,
        workspace_service: WorkspaceService,
        knowledge_service: KnowledgeService,
        prompt_service: PromptService,
        agent_service: AgentService,
        conversation_service: ConversationService,
        vector_service: VectorService,
        metrics_service: MetricsService,
        audit_service: AuditService,
    ):
        self.llm = llm
        self.workspace_service = workspace_service
        self.knowledge_service = knowledge_service
        self.prompt_service = prompt_service
        self.agent_service = agent_service
        self.conversation_service = conversation_service
        self.vector_service = vector_service
        self.metrics_service = metrics_service
        self.audit_service = audit_service

    @property
    def project(self):
        return self.workspace_service.current()
