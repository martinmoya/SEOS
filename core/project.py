"""
Project model.
"""

from pathlib import Path


class Project:
    def __init__(self, root: str):
        self.root = str(Path(root).resolve())
        self.name = Path(self.root).name

    def __str__(self):
        return self.name
