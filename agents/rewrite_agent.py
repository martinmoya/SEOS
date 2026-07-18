"""
Rewrite Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from processors.rewrite_processor import RewriteProcessor
from services.document_processing_service import DocumentProcessingService


class RewriteAgent(BaseProjectAgent):
    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /rewrite <file>"

        source = Path(project.root) / filename
        if not source.exists():
            return f'File not found: "{filename}"'

        try:
            processor = RewriteProcessor(self.context.llm)
            service = DocumentProcessingService(processor)

            print("\nRewriting document... Please wait.\n")
            destination = service.process(source, "rewrite")

            return f"Rewrite completed successfully.\nCreated: {destination.name}"
        except Exception as ex:
            return f"Failed to rewrite: {ex}"
