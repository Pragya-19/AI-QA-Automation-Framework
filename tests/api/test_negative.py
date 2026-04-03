import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid")
    assert response.status_code == 404

def test_create_user_missing_field():
    payload = {
        "name": "Pragya"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == "Pragya"