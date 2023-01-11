from fastapi.testclient import TestClient

from app.main import api

from .helper import load_fixture

client = TestClient(api)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == load_fixture("hello_world.json")
