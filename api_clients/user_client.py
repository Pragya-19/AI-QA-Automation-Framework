import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    return requests.get(f"{BASE_URL}/users")

def create_user():
    payload = {
        "name": "Pragya",
        "username": "pragya19",
        "email": "pragya@example.com"
    }
    return requests.post(f"{BASE_URL}/users", json=payload)