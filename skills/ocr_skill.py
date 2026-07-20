"""
OCR Skill.
Uses Tesseract to extract text from images.
"""

import pytesseract
from PIL import Image
from pathlib import Path

# Aseguramos que Python encuentre el ejecutable de Tesseract en Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OcrSkill:
    def extract_text(self, image_path: str) -> str:
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        try:
            img = Image.open(path)
            text = pytesseract.image_to_string(img)
            return text.strip()
        except pytesseract.TesseractNotFoundError:
            return "Error: Tesseract is not installed or not in PATH. Please install it system-wide."
        except Exception as ex:
            return f"Error during OCR: {ex}"
