"""
Workspace Service.
Implements workspace use cases, including multi-project management.
"""

from pathlib import Path
from core.project import Project
from core.workspace import Workspace


class WorkspaceService:
    def __init__(self, workspace: Workspace):
        self.workspace = workspace

    def open(self, path: str) -> str:
        root = Path(path).resolve()
        if not root.exists():
            return f"Path does not exist: {root}"
        if not root.is_dir():
            return f"Not a directory: {root}"

        project = Project(str(root))
        self.workspace.open(project)
        return f"Project opened: {project.name}"

    def current(self):
        return self.workspace.active_project

    def list_projects(self) -> list:
        return list(self.workspace._projects.values())

    def switch(self, name: str) -> str:
        project = self.workspace.get(name)
        if project:
            self.workspace._active = project
            return f"Switched to project: {project.name}"
        return f"Project '{name}' not found in session. Use /projects to see open projects."
