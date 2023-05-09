from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_homepage():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
