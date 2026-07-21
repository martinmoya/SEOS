"""
Advanced PDF Reader.
Uses pdfplumber to preserve layout. Falls back to OCR for scanned PDFs.
"""

import pdfplumber
import pytesseract
from PIL import Image

# Aseguramos que Python encuentre el ejecutable de Tesseract en Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class PdfReaderDocument:
    """
    Reads PDF documents preserving layout and tables. Falls back to OCR if no text is found.
    """

    def read(self, filename) -> str:
        lines = []
        needs_ocr = False

        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text and text.strip():
                    lines.append(text)
                else:
                    needs_ocr = True
                    break

            if needs_ocr:
                lines.append("[Scanned PDF detected. Attempting OCR...]")
                for page in pdf.pages:
                    try:
                        # Convertir página a imagen (requiere Ghostscript instalado en el sistema)
                        im = page.to_image(resolution=200).original

                        # Extraer texto con Tesseract
                        text = pytesseract.image_to_string(im)
                        if text.strip():
                            lines.append(text)
                    except Exception as ex:
                        lines.append(f"[OCR Failed for page {page.page_number}: {ex}]")
                        lines.append(
                            "Note: PDF to Image rendering requires Ghostscript installed on your OS."
                        )

        return "\n".join(lines)
