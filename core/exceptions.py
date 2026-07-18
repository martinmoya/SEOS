"""
SEOS Custom Exceptions.
"""


class SeosError(Exception):
    """Base exception for SEOS."""

    pass


class ConfigurationError(SeosError):
    """Configuration related error."""

    pass


class ProviderError(SeosError):
    """LLM Provider communication error."""

    pass
