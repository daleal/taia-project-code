from project import model
from project.constants import (
    FINAL_DATA_POINT,
    GENERATE_PREDICTIONS,
    INITIAL_DATA_POINT,
    PROVOKER_MODE,
    PROVOKING_STEPS,
)
from project.datasets import Datasets
from project.datasets.types import QuestionInstance
from project.predictions import Predictions
from project.provokers import chain_of_thought_provoker
from project.types import ProvokerMode
from project.utils import format_question


class Engine:
    @staticmethod
    def run() -> None:
        if GENERATE_PREDICTIONS:
            Engine.__generate_predictions()

    @staticmethod
    def __generate_predictions() -> None:
        SVAMP_DATASET = Datasets.svamp()
        SVAMP_PREDICTIONS = Predictions.svamp(PROVOKER_MODE)
        scoped_dataset = SVAMP_DATASET[INITIAL_DATA_POINT:FINAL_DATA_POINT]
        try:
            initial_index = INITIAL_DATA_POINT or 0
            print(f"Starting execution from index {initial_index}")
            for index, data_point in enumerate(scoped_dataset):
                data_point_index = initial_index + index
                Engine.__predict_for_data_point(
                    data_point,
                    SVAMP_PREDICTIONS,
                    data_point_index,
                    PROVOKER_MODE,
                    PROVOKING_STEPS,
                )
        except Exception:
            print(f"ERROR: Something happened at index {data_point_index}!")
        finally:
            print(f"Last execution was from index {data_point_index}")
            SVAMP_PREDICTIONS.save()

    @staticmethod
    def __predict_for_data_point(
        data_point: QuestionInstance,
        predictions: Predictions,
        index: int,
        provoker_mode: ProvokerMode,
        steps: int | None,
    ) -> str:
        print(f"\tPredicting challenge with id '{data_point['id']}'")
        prompt = format_question(data_point) + chain_of_thought_provoker(
            provoker_mode, steps  # type: ignore
        )
        prediction = model.predict(prompt)
        predictions.add_prediction(
            {
                "id": data_point['id'],
                "prompt": prompt,
                "prediction": prediction,
                "expected_answer": data_point["answer"],
            }
        )
        return prediction
