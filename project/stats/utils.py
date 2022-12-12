import re

from project.predictions.types import PredictionInstance

NUMBERS_EXPRESSION = r"-?\d+\.?\d*"


def find_last_number(prediction: PredictionInstance) -> str | None:
    cleaned = prediction["prediction"].replace(",", "")
    numbers = re.findall(NUMBERS_EXPRESSION, cleaned)
    if not numbers:
        return None
    return numbers[-1].rstrip(".")


def count_steps(prediction: PredictionInstance) -> int:
    cleaned = prediction["prediction"].replace("\n", " ")
    return len(cleaned.split(". "))
