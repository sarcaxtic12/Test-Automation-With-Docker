import requests

BASE_URL = "http://localhost:5000"

def test_invalid_endpoint():
    # Tests that accessing a non-existent endpoint returns a 404 error.
    response = requests.get(f"{BASE_URL}/invalid")
    assert response.status_code == 404

def test_method_not_allowed():
    # Tests that sending a POST to an endpoint that only allows GET returns a 405 error.
    response = requests.post(f"{BASE_URL}/health")
    assert response.status_code == 405

def test_data_post_without_item():
    # Tests that posting data without the required 'item' key returns a 400 error.
    response = requests.post(f"{BASE_URL}/data", json={})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

def test_invalid_user_endpoint():
    # Tests that requesting a user that is not in our user_list returns a 404 error.
    invalid_user = "nonexistentUser"
    response = requests.get(f"{BASE_URL}/user/{invalid_user}")
    assert response.status_code == 404
    data = response.json()
    assert "error" in data
    assert data["error"] == "User not found"