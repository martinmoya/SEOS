"""
Language utilities.
"""

LANGUAGES = {
    "es": "Spanish",
    "en": "English",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ja": "Japanese",
    "zh": "Chinese",
    "ru": "Russian",
    "ar": "Arabic",
    "hi": "Hindi",
}


def resolve_language(code: str) -> str:
    value = code.strip().lower()
    if not value:
        raise ValueError("Missing language.")
    if value in LANGUAGES:
        return LANGUAGES[value]
    for name in LANGUAGES.values():
        if name.lower() == value:
            return name
    raise ValueError(f'Unsupported language: "{code}"')
