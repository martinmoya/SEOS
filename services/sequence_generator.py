"""
Sequence Generator.
Generates Mermaid.js sequence diagrams from code execution flow.
"""

from pathlib import Path
from services.intelligence_service import IntelligenceService
from services.llm_service import LLMService


class SequenceGenerator:
    def __init__(self, llm: LLMService, root: Path):
        self.llm = llm
        self.intelligence = IntelligenceService(root)

    def generate(self, entry_file: str) -> str:
        # 1. Obtener dependencias directas del archivo inicial
        dependencies = self.intelligence.get_impact(entry_file)

        # Si el archivo no tiene dependencias o no existe en el grafo,
        # intentamos ver si él mismo importa a otros.
        if not dependencies:
            self.intelligence.build_graphs()
            # Accedemos directamente al atributo .graph que es un diccionario
            dependencies = self.intelligence.graph.get(entry_file, [])

        files_to_read = [entry_file] + dependencies

        # 2. Leer el contenido de los archivos involucrados
        code_snippets = []
        root_path = self.intelligence.root

        for rel_path in files_to_read:
            abs_path = root_path / rel_path
            if abs_path.exists() and abs_path.is_file():
                try:
                    content = abs_path.read_text(encoding="utf-8")
                    # Truncar para no exceder tokens
                    code_snippets.append(
                        f"--- File: {rel_path} ---\n{content[:1000]}\n"
                    )
                except Exception:
                    pass

        if not code_snippets:
            return "Error: Could not read the entry file or its dependencies."

        # 3. Pedir al LLM que genere el diagrama
        prompt = (
            "Analyze the execution flow and interactions between the following code files. "
            "Generate a Mermaid.js sequence diagram (```mermaid\nsequenceDiagram\n```) that illustrates "
            "how these modules interact when the application starts or the main function is called. "
            "Focus on the high-level calls between files/modules.\n\n"
            f"Entry File: {entry_file}\n\n"
            f"Code Snippets:\n{''.join(code_snippets)}\n\n"
            "Return ONLY the raw Mermaid.js code block."
        )

        response = self.llm.generate(prompt)

        # Limpiar markdown si el LLM lo envolvió doble
        if response.startswith("```mermaid"):
            response = response.split("```mermaid")[1].split("```")[0]
        elif response.startswith("```"):
            response = response.split("```")[1].split("```")[0]

        return response.strip()
