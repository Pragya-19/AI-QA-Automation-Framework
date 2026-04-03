from api_clients.user_client import get_users, create_user

def test_get_users():
    response = get_users()
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]
    assert "email" in data[0]

def test_create_user():
    response = create_user()
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Pragya"
    assert data["username"] == "pragya19"
    assert data["email"] == "pragya@example.com"