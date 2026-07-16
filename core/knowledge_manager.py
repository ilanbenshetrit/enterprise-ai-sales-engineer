"""
Enterprise AI Sales Platform
Knowledge Manager
"""

from pathlib import Path

from core.document.document_loader import DocumentLoader
from core.knowledge.chunker import DocumentChunker
from core.knowledge.knowledge_store import KnowledgeStore
from core.knowledge.retriever import KnowledgeRetriever


class KnowledgeManager:
    """
    Manages document loading,
    chunking and knowledge retrieval.
    """

    def __init__(self):

        self.knowledge_path = Path("knowledge")

        self.loader = DocumentLoader()
        self.chunker = DocumentChunker()
        self.store = KnowledgeStore()

        self._load_knowledge()

        self.retriever = KnowledgeRetriever(
            self.store
        )


    def _load_knowledge(self):

        if not self.knowledge_path.exists():
            return


        for file in self.knowledge_path.glob("*.md"):

            content = self.loader.load(
                str(file)
            )


            chunks = self.chunker.split(
                content,
                source=file.name
            )


            self.store.add_chunks(
                chunks
            )


    def search(self, query: str):

        return self.retriever.search(
            query
        )          
