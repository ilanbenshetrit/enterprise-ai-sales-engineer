from app.llm.providers.openai_provider import OpenAIProvider


class LLMService:


    def __init__(self):

        self.provider = OpenAIProvider()



    def ask(self, prompt):

        return self.provider.ask(
            prompt
        )