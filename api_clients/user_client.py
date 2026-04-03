import requests

BASE_URL = "https://reqres.in/api"

def get_users():
    return requests.get(f"{BASE_URL}/users?page=2")