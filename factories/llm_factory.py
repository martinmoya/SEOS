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

        raise ConfigurationError(f"Unsupported provider: {provider}")
