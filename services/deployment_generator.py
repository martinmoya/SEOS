"""
Deployment Generator.
Uses LLM to generate Dockerfiles and CI/CD pipelines.
"""

from services.llm_service import LLMService


class DeploymentGenerator:
    def __init__(self, llm: LLMService):
        self.llm = llm

    def generate_dockerfile(self, entrypoint: str) -> str:
        prompt = (
            f"Generate a production-ready Dockerfile for a Python application with entrypoint '{entrypoint}'. "
            "Use a slim Python 3.11 base image. Include requirements installation. "
            "Return ONLY the raw Dockerfile content. "
            "Do not use markdown blocks. Do not include explanations."
        )

        response = self.llm.generate(prompt)

        if response.startswith("```dockerfile"):
            response = response[12:]
        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()
