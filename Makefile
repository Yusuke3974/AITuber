.PHONY: format
format:
	poetry run isort .
	poetry run black .

.PHONY: static-validation
static-validation:
	poetry run black --check .
	poetry run flake8 .
	poetry run mypy .


.PHONY: dep
dep:
	pip install poetry
	poetry install