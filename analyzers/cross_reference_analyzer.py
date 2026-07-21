"""
Cross-Reference Analyzer.
Builds a dependency graph by extracting imports from project files.
"""

import re
from pathlib import Path
from collections import defaultdict


class CrossReferenceAnalyzer:
    def __init__(self):
        self.patterns = [
            r"^\s*from\s+([a-zA-Z0-9_.]+)\s+import",
            r"^\s*import\s+([a-zA-Z0-9_.]+)",
            r"import\s+([a-zA-Z0-9_.]+)\s*;",
            r"using\s+([a-zA-Z0-9_.]+)\s*;",
            r'require\(["\']([a-zA-Z0-9_./]+)["\']\)',
            r'from\s+["\']([a-zA-Z0-9_./]+)["\']\s+import',
        ]
        self.compiled_patterns = [re.compile(p, re.MULTILINE) for p in self.patterns]
        self.entry_points = {
            "main.py",
            "app.py",
            "index.js",
            "index.ts",
            "server.js",
            "Main.java",
            "Program.cs",
        }

    def analyze(self, root: Path) -> dict:
        supported_exts = {".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".cs"}
        files = [
            f
            for f in root.rglob("*")
            if f.suffix in supported_exts
            and not any(
                part in {".venv", "node_modules", "__pycache__", ".git", "logs"}
                for part in f.parts
            )
        ]

        # Mapear nombres de módulos a rutas de archivos reales (usando as_posix para Windows/Linux compat)
        file_map = {f.stem: f.relative_to(root).as_posix() for f in files}

        graph = defaultdict(list)

        for f in files:
            # Normalizar la ruta actual a formato POSIX (core/kernel.py en vez de core\kernel.py)
            rel_path = f.relative_to(root).as_posix()
            try:
                content = f.read_text(encoding="utf-8")
            except Exception:
                continue

            for pattern in self.compiled_patterns:
                for match in pattern.finditer(content):
                    imported_module = match.group(1)

                    parts = imported_module.replace("/", ".").split(".")
                    resolved_file = None

                    for i in range(len(parts) - 1, -1, -1):
                        stem = parts[i]
                        if stem in file_map:
                            resolved_file = file_map[stem]
                            break

                    if resolved_file and resolved_file != rel_path:
                        if resolved_file not in graph[rel_path]:
                            graph[rel_path].append(resolved_file)

        return dict(graph)
