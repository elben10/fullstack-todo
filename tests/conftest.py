from typing import Generator

import pytest
from fastapi.testclient import TestClient

from fullstack_todo.api import app


@pytest.fixture(scope="module")
def test_client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c
