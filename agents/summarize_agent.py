"""
Summarize Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from processors.summary_processor import SummaryProcessor
from services.document_processing_service import DocumentProcessingService


class SummarizeAgent(BaseProjectAgent):
    description = "Generate a summary of a document. Usage: /summarize <file>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /summarize <file>"

        source = Path(project.root) / filename
        if not source.exists():
            return f'File not found: "{filename}"'

        try:
            processor = SummaryProcessor(self.context.llm)
            service = DocumentProcessingService(processor)

            print("\nSummarizing document... Please wait.\n")
            destination = service.process(source, "summary")

            return f"Summary completed successfully.\nCreated: {destination.name}"
        except Exception as ex:
            return f"Failed to summarize: {ex}"
