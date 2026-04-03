import requests
from utils.config import API_BASE_URL
from utils.test_data import NEW_USER_PAYLOAD

def get_users():
    return requests.get(f"{API_BASE_URL}/users")

def create_user():
    return requests.post(f"{API_BASE_URL}/users", json=NEW_USER_PAYLOAD)