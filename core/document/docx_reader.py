"""
Enterprise AI Sales Platform
DOCX Reader
"""

from pathlib import Path

from docx import Document


class DocxReader:
    """
    Reads text from Microsoft Word (.docx) files.
    """

    def read(self, file_path: Path) -> str:

        document = Document(str(file_path))

        paragraphs = []

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)