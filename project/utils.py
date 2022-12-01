from project.datasets.types import QuestionInstance


def format_question(data_point: QuestionInstance) -> str:
    return f"Q: {data_point['question']}\nA: "
