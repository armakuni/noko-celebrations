# This help screen
show-help:
  @just --list --unsorted

# Run the unit tests
test:
  poetry run python -m pytest

alias fmt := format

# Auto format code
format:
  poetry run black .
  poetry run isort .

# Run linting against the code
lint:
  poetry run black --check .
  poetry run isort --check .
  poetry run python -m mypy .
  poetry run bandit -r --silent -c pyproject.toml .
  poetry run python -m flake8p .
