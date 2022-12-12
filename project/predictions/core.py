from __future__ import annotations

import json
import os
from typing import Any

from project.predictions.types import PredictionInstance
from project.types import ProvokerMode


class Predictions:
    __svamp: Predictions | None = None

    def __init__(
        self,
        predictions: list[PredictionInstance],
        dataset_name: str,
        provoker_mode: ProvokerMode,
        provoking_steps: int | None,
    ) -> None:
        self.__predictions = predictions
        self.__dataset_name = dataset_name
        self.__provoker_mode = provoker_mode
        self.__provoking_steps = provoking_steps

    @property
    def predictions(self) -> list[PredictionInstance]:
        return self.__predictions

    def add_prediction(self, prediction: PredictionInstance) -> None:
        self.__predictions.append(prediction)

    def save(self) -> None:
        if not os.path.isdir("predictions"):
            os.mkdir("predictions")
        if not os.path.isdir(f"predictions/{self.__dataset_name}"):
            os.mkdir(f"predictions/{self.__dataset_name}")
        file_name = self.__provoker_mode + (
            "" if self.__provoking_steps is None else f"-{self.__provoking_steps}"
        )
        with open(
            f"predictions/{self.__dataset_name}/{file_name}.json",
            mode="w",
            encoding="utf-8",
        ) as predictions_file:
            json.dump(self.__predictions, predictions_file)

    @staticmethod
    def __open_prediction_json(
        name: str, provoker_mode: ProvokerMode, provoking_steps: int | None
    ) -> Any:
        try:
            file_name = provoker_mode + (
                "" if provoking_steps is None else f"-{provoking_steps}"
            )
            with open(
                f"predictions/{name}/{file_name}.json", mode="r", encoding="utf-8"
            ) as predictions_file:
                data = json.load(predictions_file)
            return data
        except FileNotFoundError:
            return []

    @classmethod
    def svamp(
        cls, provoker_mode: ProvokerMode, provoking_steps: int | None
    ) -> Predictions:
        if cls.__svamp:
            return cls.__svamp
        NAME = "svamp"
        predictions: list[PredictionInstance] = cls.__open_prediction_json(
            NAME, provoker_mode, provoking_steps
        )
        cls.__svamp = cls(predictions, NAME, provoker_mode, provoking_steps)
        return cls.__svamp
