"""
OCR Agent.
Extracts text from images.
"""

from pathlib import Path
from agents.base_project_agent import BaseProjectAgent
from skills.ocr_skill import OcrSkill


class OcrAgent(BaseProjectAgent):
    description = "Extract text from an image using OCR. Usage: /ocr <image_file>"

    def execute(self, argument: str) -> str:
        try:
            project = self.require_project()
        except RuntimeError as ex:
            return str(ex)

        filename = argument.strip()
        if not filename:
            return "Usage: /ocr <image_file>"

        source = Path(project.root) / filename

        if not source.exists():
            return f"File not found: {filename}"

        print("\nExtracting text from image... Please wait.\n")

        skill = OcrSkill()
        try:
            return skill.extract_text(str(source))
        except Exception as ex:
            return str(ex)
