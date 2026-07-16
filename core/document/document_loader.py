"""
Enterprise AI Sales Platform
Document Loader
"""

from pathlib import Path

from core.document.pdf_reader import PDFReader
from core.document.docx_reader import DocxReader
from core.document.text_reader import TextReader


class DocumentLoader:
    """
    Loads documents based on file extension.
    Supports:
    - PDF
    - DOCX
    - TXT
    - Markdown
    """

    def __init__(self):

        self.pdf_reader = PDFReader()
        self.docx_reader = DocxReader()
        self.text_reader = TextReader()

    def load(self, file_path: str) -> str:
        """
        Load document content and return extracted text.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        extension = path.suffix.lower()

        if extension == ".pdf":
            return self.pdf_reader.read(path).strip()

        if extension == ".docx":
            return self.docx_reader.read(path).strip()

        if extension in [".txt", ".md"]:
            return self.text_reader.read(path).strip()

        raise ValueError(
            f"Unsupported file type: {extension}"
        )