"""
LLM Service.
Wraps provider calls.
"""

from providers.base_provider import BaseLLMProvider
from services.metrics_service import MetricsService
from services.audit_service import AuditService


class LLMService:
    def __init__(
        self,
        provider: BaseLLMProvider,
        metrics_service: MetricsService = None,
        audit_service: AuditService = None,
    ):
        self.provider = provider
        self.metrics = metrics_service
        self.audit = audit_service

    def generate(self, prompt: str, system: str = None, history: list = None) -> str:
        # El provider ahora devuelve (texto, tokens)
        text, tokens = self.provider.generate(prompt, system, history)

        if self.metrics:
            self.metrics.add_llm_call(tokens)
        if self.audit:
            self.audit.log_action("LLM_CALL", tokens=tokens)

        return text
