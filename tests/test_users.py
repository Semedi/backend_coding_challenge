
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login():
        response = client.post(
            "users/login/",
            json={
                "username": "admin",
                "password": "admin",
            },
        )
        assert response.status_code == 200
        assert 'access_token' in response.json()


