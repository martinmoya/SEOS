"""
Intelligence Service.
Uses the dependency graph to provide project insights.
"""

from pathlib import Path
from analyzers.cross_reference_analyzer import CrossReferenceAnalyzer
from collections import defaultdict


class IntelligenceService:
    def __init__(self, root: Path):
        self.root = root
        self.analyzer = CrossReferenceAnalyzer()
        self.graph = {}
        self.reverse_graph = defaultdict(list)

    def build_graphs(self):
        """Builds forward and reverse dependency graphs."""
        self.graph = self.analyzer.analyze(self.root)

        # Build reverse graph (who imports me)
        self.reverse_graph = defaultdict(list)
        for file, imports in self.graph.items():
            for imp in imports:
                self.reverse_graph[imp].append(file)

        return "Intelligence graphs built."

    def get_impact(self, file_path: str) -> list:
        """Returns files that depend on the given file."""
        if not self.graph:
            self.build_graphs()

        return sorted(self.reverse_graph.get(file_path, []))

    def find_dead_code(self) -> list:
        """Returns files that are not imported by anyone and are not entry points."""
        if not self.graph:
            self.build_graphs()

        all_files = set(self.graph.keys())
        all_files.update(self.reverse_graph.keys())

        dead_files = []
        for f in all_files:
            # Si nadie lo importa y no es un punto de entrada
            if (
                not self.reverse_graph.get(f)
                and Path(f).name not in self.analyzer.entry_points
            ):
                dead_files.append(f)

        return sorted(dead_files)
