"""
Enterprise AI Sales Platform
PDF Reader
"""

from pathlib import Path
from pypdf import PdfReader


class PDFReader:
    """
    Reads text from PDF files.
    """

    def read(self, file_path: Path) -> str:

        reader = PdfReader(str(file_path))

        text = []

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text.append(page_text)

        return "\n".join(text)