class EmbeddingService:
    """
    Abstraction layer for generating embeddings.
    """


    def __init__(self, provider):

        self.provider = provider



    def create_embedding(self, text: str):

        return self.provider.embed(
            text
        )