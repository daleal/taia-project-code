from typing import TypedDict


class StatInstance(TypedDict):
    id: str
    answer: str
    correct: bool
    steps: int
