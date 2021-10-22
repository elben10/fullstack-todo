test: test-format test-import test-types test-unit

test-format:
	@poetry run black --check src

test-import:
	@poetry run isort --check src

test-types:
	@poetry run mypy --strict src

test-unit:
	@poetry run pytest tests