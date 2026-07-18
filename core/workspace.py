"""
Workspace.
Manages opened projects in the current SEOS session.
"""

from core.project import Project


class Workspace:
    def __init__(self):
        self._projects: dict[str, Project] = {}
        self._active: Project | None = None

    @property
    def active_project(self) -> Project | None:
        return self._active

    def open(self, project: Project) -> None:
        self._projects[project.name] = project
        self._active = project

    def get(self, name: str) -> Project | None:
        return self._projects.get(name)

    def list(self) -> list[str]:
        return sorted(self._projects.keys())
