import main
from fastapi.testclient import TestClient


def test_health_check():
    main.init_db = lambda: None

    with TestClient(main.app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
