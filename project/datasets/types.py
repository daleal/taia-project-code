from typing import TypedDict


class SVAMPInstance(TypedDict):
    ID: str
    Body: str
    Question: str
    Equation: str
    Answer: str
    Type: str


class QuestionInstance(TypedDict):
    id: str
    question: str
    answer: str
