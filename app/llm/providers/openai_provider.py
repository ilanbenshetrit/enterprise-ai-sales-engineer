import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class OpenAIProvider:


    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )



    def ask(self, prompt):

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000
        )


        return response.choices[0].message.content