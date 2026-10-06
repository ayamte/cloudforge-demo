from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "OK"


def test_version(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "test-123")
    client = app.test_client()
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_data(as_text=True) =="test-123"