"""
Summarize Agent.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from processors.summary_processor import SummaryProcessor
from services.document_processing_service import DocumentProcessingService


class SummarizeAgent(BaseProjectAgent):
    description = "Summarize a document or folder. Usage: /summarize <file|folder>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        path_str = argument.strip()
        if not path_str:
            return "Usage: /summarize <file|folder>"

        source = Path(project.root) / path_str
        if not source.exists():
            return f'Path not found: "{path_str}"'

        processor = SummaryProcessor(self.context.llm)
        service = DocumentProcessingService(processor)

        if source.is_dir():
            return self._process_batch(source, service)
        else:
            return self._process_single(source, service)

    def _process_single(self, source: Path, service: DocumentProcessingService) -> str:
        print(f"\nSummarizing {source.name}... Please wait.\n")
        try:
            dest = service.process(source, "summary")
            return f"Summary completed successfully.\nCreated: {dest.name}"
        except Exception as ex:
            return f"Failed to summarize: {ex}"

    def _process_batch(
        self, source_dir: Path, service: DocumentProcessingService
    ) -> str:
        valid_exts = {".txt", ".md", ".pdf", ".docx", ".xlsx", ".pptx"}
        files = [f for f in source_dir.rglob("*") if f.suffix.lower() in valid_exts]

        if not files:
            return f"No supported documents found in folder: {source_dir.name}"

        print(
            f"\n[bold blue]Found {len(files)} documents. Starting batch summarization...[/bold blue]"
        )

        success = 0
        errors = []
        for f in files:
            print(f"   -> Summarizing {f.name}...")
            try:
                service.process(f, "summary")
                success += 1
            except Exception as ex:
                errors.append(f"{f.name}: {ex}")

        report = f"Batch summarization finished. Success: {success}/{len(files)}."
        if errors:
            report += "\n[bold red]Errors:[/bold red]\n" + "\n".join(errors)
        return report
