from abc import ABC, abstractmethod



class EmbeddingProvider(ABC):
    """
    Interface for embedding providers.
    """


    @abstractmethod
    def embed(self, text: str):
        pass



class SimpleEmbeddingProvider(EmbeddingProvider):
    """
    Temporary embedding provider.

    Will be replaced later with:
    - OpenAI Embeddings
    - Azure OpenAI
    - Local Models
    """


    def embed(self, text: str):

        return {
            "text": text,
            "vector": []
        }