"""
API Generator.
Uses LLM to generate FastAPI endpoints.
"""

from services.llm_service import LLMService


class ApiGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate(self, description: str) -> str:
        prompt = (
            f"Generate a FastAPI endpoint for the following requirement: {description}. "
            "Include Pydantic models for request and response. Use type hints. "
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
