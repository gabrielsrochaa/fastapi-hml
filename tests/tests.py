from starlette.testclient import TestClient

from fastapi_hml.main import app

client = TestClient(app)

def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_main_json():
    response = client.get("/")
    assert response.json() == {"hello": "world"}