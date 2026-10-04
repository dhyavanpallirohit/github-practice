from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Risk Prediction API is running"
    }


def test_high_risk_api():
    response = client.get("/predict?score=85")

    assert response.status_code == 200
    assert response.json()["prediction"] == "High Risk"


def test_low_risk_api():
    response = client.get("/predict?score=50")

    assert response.status_code == 200
    assert response.json()["prediction"] == "Low Risk"


def test_invalid_score_api():
    response = client.get("/predict?score=150")

    assert response.status_code == 400