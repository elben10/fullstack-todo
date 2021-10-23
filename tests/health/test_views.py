from fastapi.testclient import TestClient


def test_health(test_client: TestClient) -> None:
    r = test_client.get("/health")
    assert r.status_code == 200
