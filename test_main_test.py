from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<h>Camera</h>" in response.text
    assert '<a href="camera">Click me</a>' in response.text


def test_camera_endpoint():
    response = client.get("/camera")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert '<a href="/">Go Back</a>' in response.text
    assert '<h1><center>Gorgeous smile detected \(^.^)/</center></h1>' in response.text
