from app.knowledge.similarity import SimilarityCalculator

from app.embeddings.embedding_service import EmbeddingService
from app.embeddings.providers.mock_embedding_provider import MockEmbeddingProvider


class KnowledgeRetriever:


    def __init__(
        self,
        top_k=5,
        min_score=0.5
    ):

        self.similarity = SimilarityCalculator()

        self.embedding_service = EmbeddingService(
            MockEmbeddingProvider()
        )

        self.top_k = top_k

        self.min_score = min_score



    def search(
        self,
        query,
        chunks
    ):


        query_vector = self.embedding_service.create_embedding(
            query
        )


        results = []


        for chunk in chunks:


            score = self.calculate_score(
                query_vector,
                chunk
            )


            if score >= self.min_score:

                results.append(
                    {
                        "score": score,
                        "chunk": chunk
                    }
                )


        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return results[:self.top_k]



    def calculate_score(
        self,
        query_vector,
        chunk
    ):


        chunk_vector = chunk["embedding"]["vector"]


        return self.similarity.cosine_similarity(
            query_vector,
            chunk_vector
        )