from project import model
from project.datasets import Datasets
from project.provokers import chain_of_thought_provoker
from project.utils import format_question


class Engine:
    @staticmethod
    def run() -> None:
        SVAMP = Datasets.svamp()
        example = SVAMP[0]
        prompt = format_question(example) + chain_of_thought_provoker()
        text = model.predict(prompt)
        print(prompt + text)
