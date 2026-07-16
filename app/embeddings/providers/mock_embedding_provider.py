import hashlib


class MockEmbeddingProvider:
    """
    Local embedding provider for development.

    Used when external embedding APIs
    are unavailable.
    """


    def embed(self, text: str):

        hash_value = hashlib.sha256(
            text.encode()
        ).hexdigest()


        vector = []


        for i in range(0, 32, 2):

            number = int(
                hash_value[i:i+2],
                16
            )

            vector.append(
                number / 255
            )


        return vector