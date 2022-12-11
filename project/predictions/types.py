from typing import TypedDict


class PredictionInstance(TypedDict):
    id: str
    prompt: str
    prediction: str
    expected_answer: str
