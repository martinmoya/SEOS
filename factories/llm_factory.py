"""
LLM Factory.
Creates LLM providers based on configuration.
"""

from config.settings import Settings
from core.exceptions import ConfigurationError


class LLMFactory:
    @staticmethod
    def create():
        provider = Settings.PROVIDER

        if provider == "lmstudio":
            from providers.lmstudio import LMStudioProvider

            return LMStudioProvider()

        elif provider == "ollama":
            from providers.ollama import OllamaProvider

            return OllamaProvider()

        elif provider == "openai":
            from providers.openai_provider import OpenAIProvider

            return OpenAIProvider()

        elif provider == "claude":
            from providers.claude_provider import ClaudeProvider

            return ClaudeProvider()

        elif provider == "gemini":
            from providers.gemini_provider import GeminiProvider

            return GeminiProvider()

        raise ConfigurationError(f"Unsupported provider: {provider}")
