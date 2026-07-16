from openai import OpenAI

from app.config.settings import settings



class OpenAIProvider:


    def __init__(self):

        self.client = OpenAI()



    def ask(self, prompt):

        response = self.client.chat.completions.create(

            model=settings.llm_model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=settings.temperature,

            max_tokens=settings.max_tokens
        )


        return response.choices[0].message.content