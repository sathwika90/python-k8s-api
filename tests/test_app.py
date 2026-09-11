from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["version"] == "1.0"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_task():
    client = app.test_client()

    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.get_json()["id"] == 1


def test_task_not_found():
    client = app.test_client()

    response = client.get("/tasks/999")

    assert response.status_code == 404