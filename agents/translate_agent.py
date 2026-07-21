"""
Translate Agent.
Translates supported documents or entire folders.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from processors.translation_processor import TranslationProcessor
from services.document_processing_service import DocumentProcessingService


class TranslateAgent(BaseProjectAgent):
    description = (
        "Translate a document or folder. Usage: /translate <file|folder> <lang>"
    )

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        args = argument.split()
        if len(args) != 2:
            return "Usage: /translate <file|folder> <language>"

        path_str = args[0]
        language = args[1]
        source = Path(project.root) / path_str

        if not source.exists():
            return f'Path not found: "{path_str}"'

        processor = TranslationProcessor(self.context.llm, language)
        service = DocumentProcessingService(processor)

        if source.is_dir():
            return self._process_batch(source, service, language)
        else:
            return self._process_single(source, service, language)

    def _process_single(
        self, source: Path, service: DocumentProcessingService, lang: str
    ) -> str:
        print(f"\nTranslating {source.name}... Please wait.\n")
        try:
            dest = service.process(source, lang)
            return f"Translation completed successfully.\nCreated: {dest.name}"
        except ValueError as ex:
            return f"Error: {ex}"
        except Exception as ex:
            return f"Failed to translate: {ex}"

    def _process_batch(
        self, source_dir: Path, service: DocumentProcessingService, lang: str
    ) -> str:
        valid_exts = {".txt", ".md", ".pdf", ".docx", ".xlsx", ".pptx"}
        files = [f for f in source_dir.rglob("*") if f.suffix.lower() in valid_exts]

        if not files:
            return f"No supported documents found in folder: {source_dir.name}"

        print(
            f"\n[bold blue]Found {len(files)} documents in {source_dir.name}. Starting batch translation...[/bold blue]"
        )

        success = 0
        errors = []
        for f in files:
            print(f"   -> Translating {f.name}...")
            try:
                service.process(f, lang)
                success += 1
            except Exception as ex:
                errors.append(f"{f.name}: {ex}")

        report = f"Batch translation finished. Success: {success}/{len(files)}."
        if errors:
            report += "\n[bold red]Errors:[/bold red]\n" + "\n".join(errors)
        return report
