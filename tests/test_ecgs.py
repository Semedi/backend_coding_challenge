from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_forbidden_read():
    response = client.get("/ecgs")
    assert response.status_code == 403

def test_forbidden_post():
    response = client.post("/ecgs")
    assert response.status_code == 403
