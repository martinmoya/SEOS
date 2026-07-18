"""
Application Settings.
Reads environment variables from .env file.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from core.exceptions import ConfigurationError

# Asegura que siempre busque el .env en la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Validar que el archivo de configuración exista antes de continuar
if not ENV_FILE.exists():
    raise ConfigurationError("Missing .env file. Please copy .env.example to .env")

load_dotenv(ENV_FILE)


class Settings:
    @staticmethod
    def _get(key: str) -> str:
        value = os.getenv(key)
        if value is None or value.strip() == "":
            raise ConfigurationError(f"Missing environment variable: {key}")
        return value

    PROVIDER = _get.__func__("LLM_PROVIDER").lower()
    LMSTUDIO_URL = _get.__func__("LMSTUDIO_URL")
    OLLAMA_URL = _get.__func__("OLLAMA_URL")
    MODEL = _get.__func__("MODEL")
    TEMPERATURE = float(_get.__func__("TEMPERATURE"))
    MAX_TOKENS = int(_get.__func__("MAX_TOKENS"))
