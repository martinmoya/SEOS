"""
Universal Analyzer.
Uses Regex heuristics to parse multiple programming languages.
"""

import re
from pathlib import Path
from knowledge.code_knowledge import CodeKnowledge


class UniversalAnalyzer:
    def __init__(self):
        # Añadimos soporte para 'sub' (Perl) y 'package' (Perl/Ruby)
        self.class_pattern = re.compile(
            r"\b(?:class|interface|struct|enum|record|package)\s+([A-Za-z0-9_]+)",
            re.IGNORECASE,
        )
        self.func_pattern = re.compile(
            r"\b(?:def|func|fun|fn|function|sub|public|private|protected|static|void|int|string|bool|var|let|const)\b.*?\b([A-Za-z0-9_]+)\s*\(",
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
            # Buscar Clases / Packages
            for match in self.class_pattern.finditer(line):
                knowledge.add(
                    {
                        "type": "class",
                        "name": match.group(1),
                        "file": str(file_path),
                        "line": line_num,
                    }
                )

            # Buscar Funciones / Métodos / Subrutinas
            for match in self.func_pattern.finditer(line):
                func_name = match.group(1)
                if func_name not in [
                    "if",
                    "for",
                    "while",
                    "switch",
                    "catch",
                    "return",
                    "my",
                    "our",
                    "local",
                ]:
                    knowledge.add(
                        {
                            "type": "function",
                            "name": func_name,
                            "file": str(file_path),
                            "line": line_num,
                        }
                    )

        return knowledge
