class KnowledgeRetriever:


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

        query_words = query.lower().split()

        content = chunk["content"].lower()


        score = 0


        for word in query_words:

            if word in content:

                score += 1


        return score