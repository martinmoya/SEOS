"""
Universal Analyzer.
Uses Regex heuristics to parse multiple programming languages.
"""

import re
from pathlib import Path
from knowledge.code_knowledge import CodeKnowledge


class UniversalAnalyzer:
    def __init__(self):
        # Patrones regex para clases y funciones en múltiples lenguajes
        # Soporta: Python, Java, JS, TS, C#, Go, Rust, C++, PHP
        self.class_pattern = re.compile(
            r"\b(?:class|interface|struct|enum|record)\s+([A-Za-z0-9_]+)", re.IGNORECASE
        )
        self.func_pattern = re.compile(
            r"\b(?:def|func|fun|fn|function|public|private|protected|static|void|int|string|bool|var|let|const)\b.*?\b([A-Za-z0-9_]+)\s*\(",
            re.MULTILINE,
        )

    def analyze(self, file_path: Path) -> CodeKnowledge:
        knowledge = CodeKnowledge()

        try:
            source_code = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return knowledge

        lines = source_code.splitlines()

        for line_num, line in enumerate(lines, start=1):
            # Buscar Clases
            for match in self.class_pattern.finditer(line):
                knowledge.add(
                    {
                        "type": "class",
                        "name": match.group(1),
                        "file": str(file_path),
                        "line": line_num,
                    }
                )

            # Buscar Funciones/Métodos (excluyendo palabras clave de control)
            for match in self.func_pattern.finditer(line):
                func_name = match.group(1)
                # Ignorar estructuras de control que coincidan por accidente
                if func_name not in ["if", "for", "while", "switch", "catch", "return"]:
                    knowledge.add(
                        {
                            "type": "function",
                            "name": func_name,
                            "file": str(file_path),
                            "line": line_num,
                        }
                    )

        return knowledge
