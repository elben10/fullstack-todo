dev:
	docker-compose up

docker-build:
	docker compose -f docker-compose.yml build

test: test-format test-import test-lint test-types test-unit

test-format:
	@poetry run black --check src tests

test-import:
	@poetry run isort --check src tests

test-lint:
	@poetry run flake8 src tests

test-types:
	@poetry run mypy --strict src tests

test-unit:
	@poetry run pytest tests
	@yarn run test - --watchAll=false