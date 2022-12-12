from typing import Literal, Union, overload

from project.errors import InvalidProvokerModeError
from project.types import ProvokerMode

ProvokerModesWithSteps = Union[
    Literal["specific"],
    Literal["lower-bound"],
    Literal["upper-bound"],
]


@overload
def chain_of_thought_provoker(
    mode: Literal["default"] = "default", steps: None = None
) -> str:
    ...


@overload
def chain_of_thought_provoker(mode: ProvokerModesWithSteps, steps: int) -> str:
    ...


def chain_of_thought_provoker(
    mode: ProvokerMode = "default",
    steps: int | None = None,
) -> str:
    if mode == "default":
        return "Let's think step by step."
    if mode == "specific":
        return f"Let's think step by step, using {steps} steps."
    if mode == "lower-bound":
        return f"Let's think step by step, using at least {steps} steps."
    if mode == "upper-bound":
        return f"Let's think step by step, using no more than {steps} steps."
    raise InvalidProvokerModeError(f"Invalid provoker mode '{mode}'.")
