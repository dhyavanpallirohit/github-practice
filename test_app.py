
import pytest

from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


# Test-only API key
TEST_API_KEY = "test-only-api-key"

AUTH_HEADERS = {
    "X-API-Key": TEST_API_KEY
}


# Configure API key for each test
@pytest.fixture(autouse=True)
def configure_test_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", TEST_API_KEY)


# =====================================
# 1. Homepage test
# =====================================

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Risk Prediction API is running"
    }


# =====================================
# 2. GET prediction API tests
# =====================================

def test_high_risk_api():
    response = client.get(
        "/predict?score=85",
        headers=AUTH_HEADERS
    )

    assert response.status_code == 200
    assert response.json() == {
        "score": 85,
        "prediction": "High Risk"
    }


def test_low_risk_api():
    response = client.get(
        "/predict?score=50",
        headers=AUTH_HEADERS
    )

    assert response.status_code == 200
    assert response.json() == {
        "score": 50,
        "prediction": "Low Risk"
    }


def test_invalid_score_api():
    response = client.get(
        "/predict?score=150",
        headers=AUTH_HEADERS
    )

    assert response.status_code == 400


# =====================================
# 3. POST prediction API tests
# =====================================

def test_post_predict_high_risk():
    response = client.post(
        "/predict",
        json={"score": 85},
        headers=AUTH_HEADERS
    )

    assert response.status_code == 200
    assert response.json() == {
        "score": 85,
        "prediction": "High Risk"
    }


def test_post_predict_low_risk():
    response = client.post(
        "/predict",
        json={"score": 40},
        headers=AUTH_HEADERS
    )

    assert response.status_code == 200
    assert response.json() == {
        "score": 40,
        "prediction": "Low Risk"
    }


def test_post_predict_invalid_score():
    response = client.post(
        "/predict",
        json={"score": 150},
        headers=AUTH_HEADERS
    )

    assert response.status_code == 400


def test_post_predict_missing_score():
    response = client.post(
        "/predict",
        json={},
        headers=AUTH_HEADERS
    )

    assert response.status_code == 422


# =====================================
# 4. API key authentication tests
# =====================================

def test_missing_api_key():
    response = client.post(
        "/predict",
        json={"score": 85}
    )

    assert response.status_code == 401


def test_invalid_api_key():
    response = client.post(
        "/predict",
        json={"score": 85},
        headers={"X-API-Key": "wrong-key"}
    )

    assert response.status_code == 401


def test_valid_api_key():
    response = client.post(
        "/predict",
        json={"score": 85},
        headers=AUTH_HEADERS
    )

    assert response.status_code == 200


def test_api_key_not_configured(monkeypatch):
    monkeypatch.delenv(
        "API_KEY",
        raising=False
    )

    response = client.post(
        "/predict",
        json={"score": 85},
        headers=AUTH_HEADERS
    )

    assert response.status_code == 503

def test_application_version():
    response = client.get("/version")

    assert response.status_code == 200

    assert response.json() == {
        "application": "risk-api",
        "version": "1.2.0"
    }