from __future__ import annotations

import json
import os
import re
from typing import Any

from project.constants import REGENERATE_STATS
from project.predictions.types import PredictionInstance
from project.stats.types import StatInstance
from project.stats.utils import count_steps, find_last_number
from project.types import ProvokerMode


class Stats:
    def __init__(
        self,
        predictions: list[PredictionInstance],
        dataset_name: str,
        provoker_mode: ProvokerMode,
        provoking_steps: int | None = None,
    ) -> None:
        self.__dataset_name = dataset_name
        self.__provoker_mode = provoker_mode
        self.__provoking_steps = provoking_steps
        self.__stats = (
            [Stats.__process_prediction(prediction) for prediction in predictions]
            if REGENERATE_STATS
            else Stats.__open_stats_json(dataset_name, provoker_mode, provoking_steps)
        )

    @property
    def stats(self) -> list[StatInstance]:
        return self.__stats

    def show_summary(self) -> None:
        correct_amount = filter(lambda x: x["correct"], self.__stats)
        correct_percentage = len(list(correct_amount)) / len(self.__stats)
        average_steps = sum(map(lambda x: x["steps"], self.__stats)) / len(self.__stats)
        print(f"Accuracy: {correct_percentage * 100}%")
        print(f"Average steps: {round(average_steps, 2)}")

    def save(self) -> None:
        if not os.path.isdir("stats"):
            os.mkdir("stats")
        if not os.path.isdir(f"stats/{self.__dataset_name}"):
            os.mkdir(f"stats/{self.__dataset_name}")
        file_name = self.__provoker_mode + (
            "" if self.__provoking_steps is None else f"-{self.__provoking_steps}"
        )
        with open(
            f"stats/{self.__dataset_name}/{file_name}.json",
            mode="w",
            encoding="utf-8",
        ) as stats_file:
            json.dump(self.__stats, stats_file)

    @staticmethod
    def __process_prediction(prediction: PredictionInstance) -> StatInstance:
        answer = find_last_number(prediction) or "unknown"
        steps = count_steps(prediction)
        return {
            "id": prediction["id"],
            "answer": answer,
            "correct": answer == prediction["expected_answer"],
            "steps": steps,
        }

    @staticmethod
    def __open_stats_json(
        name: str, provoker_mode: ProvokerMode, provoking_steps: int | None
    ) -> Any:
        try:
            file_name = provoker_mode + (
                "" if provoking_steps is None else f"-{provoking_steps}"
            )
            with open(
                f"stats/{name}/{file_name}.json", mode="r", encoding="utf-8"
            ) as stats_file:
                data = json.load(stats_file)
            return data
        except FileNotFoundError:
            return []

    @staticmethod
    def svamp(
        predictions: list[PredictionInstance],
        provoker_mode: ProvokerMode,
        provoking_steps: int | None = None,
    ) -> Stats:
        return Stats(predictions, "svamp", provoker_mode, provoking_steps)
