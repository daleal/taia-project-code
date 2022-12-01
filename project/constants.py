import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
MODEL_NAME = os.getenv("MODEL_NAME", "text-davinci-003")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))
