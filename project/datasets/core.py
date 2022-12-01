import json
from typing import Any

from project.datasets.types import QuestionInstance, SVAMPInstance


class Datasets:
    __svamp: list[QuestionInstance] = []

    @staticmethod
    def __open_dataset_json(name: str) -> Any:
        with open(f"data/{name}.json", mode="r", encoding="utf-8") as dataset_file:
            data = json.load(dataset_file)
        return data

    @classmethod
    def svamp(cls) -> list[QuestionInstance]:
        if cls.__svamp:
            return cls.__svamp
        dataset: list[SVAMPInstance] = cls.__open_dataset_json("svamp")
        cls.__svamp = list(
            map(
                lambda x: {
                    "question": x["Body"].strip() + " " + x["Question"].strip(),
                    "answer": str(x["Answer"]).rstrip(".0"),
                },
                dataset,
            )
        )
        return cls.__svamp
