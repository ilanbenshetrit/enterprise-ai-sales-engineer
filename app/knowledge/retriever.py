from app.knowledge.similarity import SimilarityCalculator



class KnowledgeRetriever:


    def __init__(self):

        self.similarity = SimilarityCalculator()



    def search(self, query, chunks):

        results = []


        for chunk in chunks:

            score = self.calculate_score(
                query,
                chunk
            )


            if score > 0:

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


        return results



    def calculate_score(self, query, chunk):

        """
        Future:
        Query embedding vs Chunk embedding

        Current:
        Keyword fallback
        """


        query_words = query.lower().split()

        content = chunk["content"].lower()


        score = 0


        for word in query_words:

            if word in content:

                score += 1


        return score