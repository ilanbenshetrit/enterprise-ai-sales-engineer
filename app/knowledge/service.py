from app.knowledge.loader import KnowledgeLoader
from app.knowledge.chunker import KnowledgeChunker
from app.knowledge.retriever import KnowledgeRetriever
from app.knowledge.embeddings import SimpleEmbeddingProvider
from app.knowledge.vector_store import VectorStore



class KnowledgeService:


    def __init__(self):

        self.loader = KnowledgeLoader()

        self.chunker = KnowledgeChunker()

        self.retriever = KnowledgeRetriever()

        self.embedding_provider = SimpleEmbeddingProvider()

        self.vector_store = VectorStore()



    def get_knowledge_chunks(self):

        documents = self.loader.load_documents()


        chunks = self.chunker.chunk_documents(
            documents
        )


        for chunk in chunks:

            chunk["embedding"] = self.embedding_provider.embed(
                chunk["content"]
            )


        self.vector_store.add_many(
            chunks
        )


        return self.vector_store.all()



    def search(self, query):

        chunks = self.get_knowledge_chunks()


        results = self.retriever.search(
            query,
            chunks
        )


        return results