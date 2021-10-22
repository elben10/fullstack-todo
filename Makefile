test: test-format test-import test-lint test-types test-unit

test-format:
	@poetry run black --check src

test-import:
	@poetry run isort --check src

test-lint:
	@poetry run flake8 src

test-types:
	@poetry run mypy --strict src

test-unit:
	@poetry run pytest tests