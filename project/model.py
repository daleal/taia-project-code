import openai

from project.constants import MAX_TOKENS, MODEL_NAME, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def predict(prompt: str) -> str:
    completion = openai.Completion.create(
        engine=MODEL_NAME,
        prompt=prompt,
        max_tokens=MAX_TOKENS,
    )
    return completion.choices[0].text
