import math



class SimilarityCalculator:
    """
    Calculates similarity between vectors.
    """


    def cosine_similarity(
        self,
        vector_a,
        vector_b
    ):

        if not vector_a or not vector_b:
            return 0


        dot_product = sum(
            a * b
            for a, b in zip(vector_a, vector_b)
        )


        magnitude_a = math.sqrt(
            sum(a * a for a in vector_a)
        )


        magnitude_b = math.sqrt(
            sum(b * b for b in vector_b)
        )


        if magnitude_a == 0 or magnitude_b == 0:
            return 0


        return dot_product / (
            magnitude_a * magnitude_b
        )