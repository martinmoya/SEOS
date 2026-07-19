"""
Diagram Generator.
Uses LLM to generate Mermaid.js diagrams.
"""

from services.llm_service import LLMService


class DiagramGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate(self, description: str) -> str:
        prompt = (
            f"Generate a Mermaid.js diagram for the following architecture or flow: {description}. "
            "Use appropriate diagram types (graph TD, sequenceDiagram, classDiagram, erDiagram). "
            "Return ONLY the raw Mermaid code inside a markdown block. "
            "Do not include explanations."
        )

        response = self.llm.generate(prompt)

        # Extraer el código del bloque markdown
        if "```mermaid" in response:
            response = response.split("```mermaid")[1].split("```")[0]
        elif "```" in response:
            response = response.split("```")[1].split("```")[0]

        return response.strip()
