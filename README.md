# Project for advanced AI topics

## How to run

First, create and activate the virtual environment (you can skip this step if you've already done it before):

```sh
make build-env
```

Then, simply run the `entrypoint.py` python script:

```sh
poetry run python entrypoint.py
```

## Modulating the environment

You can find the constants inside `project/constants.py`. Some of these constants can be changed by creating a `.env` file at the root of the repository and adding environmental variables:

- `OPENAI_API_KEY`: The OpenAI API key to use the model. This variable **is required**.
- `MODEL_NAME`: The OpenAI model to be used. Defaults to `text-davinci-002`.
- `MAX_TOKENS`: The max amount of tokens to be used for the input text + the prediction. It **needs to be an integer**. Defaults to `512`.
- `GENERATE_PREDICTIONS`: Set it to `true` if you want to generate the predictions from the OpenAI API, set it to anything else if you already generated them (not setting it also skips the predictions generation.).
- `PROVOKER_MODE`: Should correspond to one of the provoker modes (`default`, `specific`). Defaults to `default`.
- `PROVOKING_STEPS`: The number of steps for provoking modes other than `default`. If you set it, **it needs to be an integer**. Defaults to `None`.
- `INITIAL_DATA_POINT`: Where to start running the generation. It **needs to be an integer**. Indexes **start from 0**. Defaults to `None` (start from the beginning).
- `FINAL_DATA_POINT`: Where to stop running the generation. The index with the value set for this variable **won't be executed**. It **needs to be an integer**. Indexes **start from 0**. Defaults to `None` (end with the last element).
