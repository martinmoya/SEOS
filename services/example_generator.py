"""
Example Generator.
Uses LLM to generate fully functional, documented example files.
"""

from services.llm_service import LLMService


class ExampleGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate(self, concept: str) -> str:
        prompt = (
            f"Generate a complete, fully functional, and well-documented Python example file demonstrating: {concept}. "
            "Include a main block. Use type hints. "
            "Return ONLY the raw Python code. "
            "Do not use markdown blocks (```python). Do not include explanations."
        )

        response = self.llm.generate(prompt)

        if response.startswith("```python"):
            response = response[9:]
        elif response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]

        return response.strip()
