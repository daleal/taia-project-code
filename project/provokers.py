from typing import Literal, Union, overload

from project.errors import InvalidProvokerModeError

ProvokerMode = Union[
    Literal["default"],
    Literal["specific"],
]


@overload
def chain_of_thought_provoker(mode: Literal["default"] = "default") -> str:
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
