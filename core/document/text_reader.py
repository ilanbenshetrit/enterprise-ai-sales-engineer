"""
Enterprise AI Sales Platform
Text Reader
"""

from pathlib import Path


class TextReader:
    """
    Reads plain text files.
    """

    def read(self, file_path: Path) -> str:

        return file_path.read_text(
            encoding="utf-8"
        )