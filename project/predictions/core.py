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
        name: str,
        provoker_mode: ProvokerMode,
    ) -> None:
        self.__predictions = predictions
        self.__name = name
        self.__provoker_mode = provoker_mode

    @property
    def predictions(self) -> list[PredictionInstance]:
        return self.__predictions

    def add_prediction(self, prediction: PredictionInstance) -> None:
        self.__predictions.append(prediction)

    def save(self) -> None:
        if not os.path.isdir("predictions"):
            os.mkdir("predictions")
        if not os.path.isdir(f"predictions/{self.__name}"):
            os.mkdir(f"predictions/{self.__name}")
        with open(
            f"predictions/{self.__name}/{self.__provoker_mode}.json",
            mode="w",
            encoding="utf-8",
        ) as predictions_file:
            json.dump(self.__predictions, predictions_file)

    @staticmethod
    def __open_prediction_json(name: str, provoker_mode: ProvokerMode) -> Any:
        try:
            with open(
                f"predictions/{name}/{provoker_mode}.json", mode="r", encoding="utf-8"
            ) as predictions_file:
                data = json.load(predictions_file)
            return data
        except FileNotFoundError:
            return []

    @classmethod
    def svamp(cls, provoker_mode: ProvokerMode) -> Predictions:
        if cls.__svamp:
            return cls.__svamp
        NAME = "svamp"
        predictions: list[PredictionInstance] = cls.__open_prediction_json(
            NAME, provoker_mode
        )
        cls.__svamp = cls(predictions, NAME, provoker_mode)
        return cls.__svamp
