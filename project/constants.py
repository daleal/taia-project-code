import os
from typing import cast

from project.types import ProvokerMode

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
MODEL_NAME = os.getenv("MODEL_NAME", "text-davinci-002")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))
GENERATE_PREDICTIONS = os.getenv("GENERATE_PREDICTIONS") == "true"
REGENERATE_STATS = os.getenv("REGENERATE_STATS") == "true"
PROVOKER_MODE = cast(ProvokerMode, os.getenv("PROVOKER_MODE", "default"))
PROVOKING_STEPS = (
    None if os.getenv("PROVOKING_STEPS") is None else int(os.environ["PROVOKING_STEPS"])
)
INITIAL_DATA_POINT = (
    None
    if os.getenv("INITIAL_DATA_POINT") is None
    else int(os.environ["INITIAL_DATA_POINT"])
)
FINAL_DATA_POINT = (
    None
    if os.getenv("FINAL_DATA_POINT") is None
    else int(os.environ["FINAL_DATA_POINT"])
)
