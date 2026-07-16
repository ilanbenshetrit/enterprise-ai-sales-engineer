from app.knowledge.loader import KnowledgeLoader
from app.knowledge.chunker import KnowledgeChunker
from app.knowledge.retriever import KnowledgeRetriever


class KnowledgeService:


    def __init__(self):

        self.loader = KnowledgeLoader()
        self.chunker = KnowledgeChunker()
        self.retriever = KnowledgeRetriever()



    def get_knowledge_chunks(self):

        documents = self.loader.load_documents()

        chunks = self.chunker.chunk_documents(
            documents
        )

        return chunks



    def search(self, query):

        chunks = self.get_knowledge_chunks()

        results = self.retriever.search(
            query,
            chunks
        )

        return results