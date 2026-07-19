"""
Database Generator.
Uses LLM to generate SQLAlchemy models and SQL scripts.
"""

from services.llm_service import LLMService


class DbGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate(self, description: str) -> str:
        prompt = (
            f"Generate SQLAlchemy models for the following entities: {description}. "
            "Include relationships and basic types. "
            "Return ONLY the raw Python code. "
            "Do not use markdown blocks (```python). "
            "Do not include explanations."
        )

        response = self.llm.generate(prompt)

        if response.startswith("```python"):
            response = response[9:]
        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()
