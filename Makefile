test: format-test types-test unit-test

format-test:
	@poetry run black --check src

types-test:
	@poetry run mypy --strict src

unit-test:
	@poetry run pytest tests