import requests
from tests.utils import BASE_URL, HEADERS


def test_create_user():
    # Bonus:Proveri da li korisnik sa zadatim email-om postoji i obriši ga
    email_to_delete = "john.doe@gmail.com"

    users_response = requests.get(f"{BASE_URL}/users/", headers=HEADERS)
    assert users_response.status_code == 200, "Failed to fetch users"
    users = users_response.json()

    # Pronađi korisnika sa datim email-om
    existing_user = next((user for user in users if user["email"] == email_to_delete), None)

    # Ako korisnik postoji, obriši ga
    if existing_user:
        delete_response = requests.delete(f"{BASE_URL}/users/{existing_user['uuid']}/", headers=HEADERS)
        assert delete_response.status_code == 204, f"Failed to delete existing user: {delete_response.json()}"

    # 1. Priprema payload-a za zahtev
    payload = {
        "email": "john.doe@gmail.com",
        "password": "securepassword123",
        "name": "John Doe",
        "nickname": "johndoe"
    }

    # 2. Pošaljite POST zahtev na /users/ endpoint
    response = requests.post(f"{BASE_URL}/users/", headers=HEADERS, json=payload)

    # 3. Proverite da je statusni kod odgovora 200
    assert response.status_code == 200, "Failed to create user"

    # 4. Proverite da polja u odgovoru odgovaraju očekivanim poljima
    created_user = response.json()
    assert created_user["email"] == payload["email"], "Email mismatch"
    assert created_user["name"] == payload["name"], "Name mismatch"
    assert created_user["nickname"] == payload["nickname"], "Nickname mismatch"
    assert "uuid" in created_user, "UUID not returned in response"

    user_uuid = created_user["uuid"]

    # 5. Potvrdite da je novi korisnik kreiran i da postoji u listi korisnika
    users_response = requests.get(f"{BASE_URL}/users/", headers=HEADERS)
    assert users_response.status_code == 200, "Failed to fetch users"
    users = users_response.json()
    assert any(user["uuid"] == user_uuid for user in users), "Created user not found in user list"

    # 6. Proverite da je korisnik ispravno vraćen kada se dohvati pomoću svog uuid-a
    user_response = requests.get(f"{BASE_URL}/users/{user_uuid}/", headers=HEADERS)
    assert user_response.status_code == 200, "Failed to fetch created user by UUID"
    fetched_user = user_response.json()
    assert fetched_user["email"] == payload["email"], "Email mismatch in fetched user"
    assert fetched_user["name"] == payload["name"], "Name mismatch in fetched user"
    assert fetched_user["nickname"] == payload["nickname"], "Nickname mismatch in fetched user"
