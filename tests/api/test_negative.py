import requests
from utils.config import API_BASE_URL
from utils.test_data import INCOMPLETE_USER_PAYLOAD

def test_invalid_endpoint():
    response = requests.get(f"{API_BASE_URL}/invalid")
    assert response.status_code == 404

def test_create_user_missing_field():
    response = requests.post(f"{API_BASE_URL}/users", json=INCOMPLETE_USER_PAYLOAD)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == "Pragya"