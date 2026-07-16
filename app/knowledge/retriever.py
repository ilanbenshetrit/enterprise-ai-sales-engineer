class KnowledgeRetriever:


    def search(self, query, chunks):

        results = []


        query_words = query.lower().split()


        for chunk in chunks:

            content = chunk["content"].lower()


            score = 0


            for word in query_words:

                if word in content:

                    score += 1


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