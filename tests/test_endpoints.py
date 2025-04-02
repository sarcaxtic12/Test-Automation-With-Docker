import requests
import random

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
    assert "app" in data and "version" in data and "description" in data
    assert data["app"] == "Microservice"
    assert data["version"] == "1.0"

# def test_user_endpoint():
    # username = "testuser"
    # response = requests.get(f"{BASE_URL}/user/{username}")
    # assert response.status_code == 200
    # data = response.json()
    # assert data.get("username") == username
    # assert "role" in data
    # assert "status" in data

def test_data_get_endpoint():
    # Initially, the data store should be empty.
    response = requests.get(f"{BASE_URL}/data")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

def test_data_post_endpoint():
    payload = {"item": "sample"}
    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data.get("message") == "Item added"
    assert "data" in data
    assert "sample" in data["data"]

def test_valid_user_endpoint():
    # Pick a random valid user from the list: e.g., user45, user73, etc.
    valid_user = f"user{random.randint(1, 100)}"
    response = requests.get(f"{BASE_URL}/user/{valid_user}")
    assert response.status_code == 200
    data = response.json()
    assert data.get("username") == valid_user
    assert "role" in data
    assert "status" in data