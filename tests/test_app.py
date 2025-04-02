import requests

BASE_URL = "http://localhost:5000"

def test_home_endpoint():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Hello, world! This is your microservice."

def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "OK"

def test_info_endpoint():
    response = requests.get(f"{BASE_URL}/info")
    assert response.status_code == 200
    data = response.json()
    # Check that expected keys are in the JSON response
    assert "app" in data
    assert "version" in data
    assert "description" in data
    # Optionally, check the values
    assert data["app"] == "Microservice"
    assert data["version"] == "1.0"