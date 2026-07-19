"""
Deploy Agent.
Generates Dockerfiles for the project.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from services.deployment_generator import DeploymentGenerator


class DeployAgent(BaseProjectAgent):
    description = "Generate a Dockerfile. Usage: /create_docker <entrypoint.py>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        entrypoint = argument.strip()
        if not entrypoint:
            return "Usage: /create_docker <entrypoint.py>"

        print("\nGenerating Dockerfile... Please wait.\n")

        generator = DeploymentGenerator(self.context.llm)
        dockerfile_content = generator.generate_dockerfile(entrypoint)

        filepath = Path(project.root) / "Dockerfile"
        try:
            filepath.write_text(dockerfile_content, encoding="utf-8")
            return f"Successfully created: Dockerfile\nPath: {filepath}"
        except Exception as ex:
            return f"Error writing file: {ex}"
