test: format-test import-test types-test unit-test

format-test:
	@poetry run black --check src

import-test:
	@poetry run isort --check src

types-test:
	@poetry run mypy --strict src

unit-test:
	@poetry run pytest tests