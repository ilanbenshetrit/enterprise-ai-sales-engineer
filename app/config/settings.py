import os

from dotenv import load_dotenv


load_dotenv()



class Settings:


    def __init__(self):

        self.llm_provider = os.getenv(
            "LLM_PROVIDER",
            "openai"
        )


        self.llm_model = os.getenv(
            "LLM_MODEL",
            "gpt-4.1-mini"
        )


        self.temperature = float(
            os.getenv(
                "LLM_TEMPERATURE",
                "0.2"
            )
        )


        self.max_tokens = int(
            os.getenv(
                "LLM_MAX_TOKENS",
                "1000"
            )
        )



settings = Settings()