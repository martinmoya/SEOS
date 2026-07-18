"""
Python Analyzer.
Extracts symbols from Python source files using AST.
"""

import ast
from pathlib import Path


class PythonAnalyzer:
    def analyze(self, file_path: Path) -> dict:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        symbols = {"classes": [], "functions": [], "methods": []}

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                symbols["classes"].append(node.name)
                for member in node.body:
                    if isinstance(member, ast.FunctionDef):
                        symbols["methods"].append(f"{node.name}.{member.name}")
            elif isinstance(node, ast.FunctionDef):
                symbols["functions"].append(node.name)

        return symbols
