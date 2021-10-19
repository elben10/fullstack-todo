test: format-test unit-test

format-test:
	@poetry run black --check src

unit-test:
	@poetry run pytest tests