"""
Code Generator.
Uses LLM to generate boilerplate code.
"""

from services.llm_service import LLMService


class CodeGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate(self, element_type: str, name: str) -> str:
        prompt = (
            f"Generate a Python {element_type} named {name}. "
            "Include type hints, docstrings, and basic boilerplate. "
            "Return ONLY the raw Python code. "
            "Do not use markdown blocks (```python). "
            "Do not include explanations."
        )

        response = self.llm.generate(prompt)

        # Limpiar markdown por si el LLM hizo caso omiso
        if response.startswith("```python"):
            response = response[9:]
        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()
