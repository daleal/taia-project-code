from typing import Literal, overload

from project.errors import InvalidProvokerModeError
from project.types import ProvokerMode


@overload
def chain_of_thought_provoker(
    mode: Literal["default"] = "default", steps: None = None
) -> str:
    ...


@overload
def chain_of_thought_provoker(mode: Literal["specific"], steps: int) -> str:
    ...


def chain_of_thought_provoker(
    mode: ProvokerMode = "default",
    steps: int | None = None,
) -> str:
    if mode == "default":
        return "Let's think step by step."
    if mode == "specific":
        return f"Let's think step by step, using {steps} steps."
    raise InvalidProvokerModeError(f"Invalid provoker mode '{mode}'.")
