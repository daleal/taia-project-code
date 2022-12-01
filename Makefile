POETRY_VERSION = 1.2.1

# Env stuff
.PHONY: get-poetry
get-poetry:
	curl -sSL https://install.python-poetry.org | python3 - --version $(POETRY_VERSION)

.PHONY: build-env
build-env:
	python3 -m venv .venv
	poetry run pip install --upgrade pip
	poetry run poetry install

# Runner
.PHONY: run!
run!:
	poetry run python entrypoint.py

# Passive linters
.PHONY: black
black:
	poetry run black project --check

.PHONY: flake8
flake8:
	poetry run flake8 project

.PHONY: isort
isort:
	poetry run isort project --profile=black --check

.PHONY: pylint
pylint:
	poetry run pylint project

.PHONY: mypy
mypy:
	poetry run mypy project

# Aggresive linters
.PHONY: black!
black!:
	poetry run black project

.PHONY: isort!
isort!:
	poetry run isort project --profile=black
