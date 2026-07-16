import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()



class OpenAIEmbeddingProvider:
    """
    OpenAI based embedding provider.
    """


    def __init__(self):

        api_key = os.getenv(
            "OPENAI_API_KEY"
        )


        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Please check your .env file."
            )


        self.client = OpenAI(
            api_key=api_key
        )



    def embed(self, text: str):

        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )


        return response.data[0].embedding