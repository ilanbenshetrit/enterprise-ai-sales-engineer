from app.knowledge.loader import KnowledgeLoader
from app.knowledge.chunker import KnowledgeChunker
from app.knowledge.retriever import KnowledgeRetriever
from app.knowledge.vector_store import VectorStore

from app.embeddings.embedding_service import EmbeddingService
from app.embeddings.providers.mock_embedding_provider import MockEmbeddingProvider



class KnowledgeService:


    def __init__(self):

        self.loader = KnowledgeLoader()

        self.chunker = KnowledgeChunker()

        self.retriever = KnowledgeRetriever()

        self.embedding_service = EmbeddingService(
            MockEmbeddingProvider()
        )

        self.vector_store = VectorStore()

        self.index_ready = False



    def build_index(self):

        documents = self.loader.load_documents()


        chunks = self.chunker.chunk_documents(
            documents
        )


        for chunk in chunks:

            chunk["embedding"] = {
                "text": chunk["content"],
                "vector": self.embedding_service.create_embedding(
                    chunk["content"]
                )
            }


        self.vector_store.add_many(
            chunks
        )


        self.index_ready = True


        return self.vector_store.all()



    def get_knowledge_chunks(self):

        if not self.index_ready:

            return self.build_index()


        return self.vector_store.all()



    def search(self, query):

        chunks = self.get_knowledge_chunks()


        results = self.retriever.search(
            query,
            chunks
        )


        return results