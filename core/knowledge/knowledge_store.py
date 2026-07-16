"""
Enterprise AI Sales Platform
Knowledge Store

Stores processed document chunks.
"""


class KnowledgeStore:
    """
    Stores and manages knowledge chunks.
    """

    def __init__(self):

        self.chunks = []


    def add_chunks(self, chunks: list[dict]):
        """
        Add document chunks into knowledge store.
        """

        self.chunks.extend(chunks)


    def get_all(self) -> list[dict]:
        """
        Return all stored chunks.
        """

        return self.chunks


    def count(self) -> int:
        """
        Return number of stored chunks.
        """

        return len(self.chunks)