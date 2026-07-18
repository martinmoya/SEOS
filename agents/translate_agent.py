"""
Translate Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from processors.translation_processor import TranslationProcessor
from services.document_processing_service import DocumentProcessingService


class TranslateAgent(BaseProjectAgent):
    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        args = argument.split()
        if len(args) != 2:
            return "Usage: /translate <file> <language>"

        filename = args[0]
        language = args[1]
        source = Path(project.root) / filename

        if not source.exists():
            return f'File not found: "{filename}"'

        try:
            processor = TranslationProcessor(self.context.llm, language)
            service = DocumentProcessingService(processor)

            print("\nTranslating document... Please wait.\n")
            destination = service.process(source, language)

            return f"Translation completed successfully.\nCreated: {destination.name}"
        except ValueError as ex:
            return f"Error: {ex}"
        except Exception as ex:
            return f"Failed to translate: {ex}"
