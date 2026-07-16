"""
Enterprise AI Sales Platform
Knowledge Retriever v2

Improved keyword based retrieval.
"""


class KnowledgeRetriever:
    """
    Retrieves relevant knowledge chunks
    using improved scoring.
    """


    STOP_WORDS = {
        "the",
        "is",
        "a",
        "an",
        "of",
        "and",
        "or",
        "how",
        "does",
        "do",
        "what",
        "can",
        "to",
        "for",
        "with"
    }


    def __init__(self, knowledge_store):

        self.knowledge_store = knowledge_store


    def _extract_keywords(self, text: str):

        words = (
            text.lower()
            .replace("?", "")
            .replace(".", "")
            .split()
        )

        return {
            word
            for word in words
            if word not in self.STOP_WORDS
        }


    def search(
        self,
        query: str,
        top_k: int = 3
    ) -> list[dict]:
        """
        Search chunks by relevance score.
        """


        keywords = self._extract_keywords(
            query
        )


        results = []


        for chunk in self.knowledge_store.get_all():

            content = chunk["content"].lower()


            score = 0


            for keyword in keywords:

                if keyword in content:

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


        return [
            item["chunk"]
            for item in results[:top_k]
        ]