class KnowledgeChunker:


    def __init__(self, chunk_size=300):

        self.chunk_size = chunk_size



    def chunk_documents(self, documents):

        chunks = []


        chunk_id = 1


        for document in documents:

            content = document["content"]


            words = content.split()


            for i in range(
                0,
                len(words),
                self.chunk_size
            ):

                chunk_text = " ".join(
                    words[i:i + self.chunk_size]
                )


                chunks.append(
                    {
                        "chunk_id": chunk_id,
                        "source": document["source"],
                        "content": chunk_text
                    }
                )


                chunk_id += 1


        return chunks