class VectorStore:
    """
    Temporary in-memory vector store.

    Future implementations:
    - FAISS
    - ChromaDB
    - Pinecone
    - Azure AI Search
    """


    def __init__(self):

        self.vectors = []



    def add(self, item):

        self.vectors.append(
            item
        )



    def add_many(self, items):

        for item in items:
            self.add(item)



    def all(self):

        return self.vectors