import requests
from tests.utils import BASE_URL, HEADERS


def test_delete_user():
    # 1. Pošaljite GET zahtev na /users/ endpoint kako biste dobili listu korisnika.
    response = requests.get(f"{BASE_URL}/users/", headers=HEADERS)
    assert response.status_code == 200, "Failed to fetch users"
    users = response.json()
    assert users, "No users found to delete"

    # 2. Izaberite bilo kog korisnika iz liste i zabeležite njegov user uuid.
    user_to_delete = users[0]["uuid"]  # Prvi korisnik u listi

    # 3. Pošaljite DELETE zahtev na /users/{uuid}/ endpoint sa prethodno uzetim user uuid kao parametrom.
    delete_response = requests.delete(f"{BASE_URL}/users/{user_to_delete}/", headers=HEADERS)

    # 4. Osigurajte da response sa statusom 204 bude primljen.
    assert delete_response.status_code == 204, "Failed to delete user"

    # 5. Validirajte da je korisnik obrisan iz liste korisnika slanjem GET zahteva na /users/ endpoint.
    remaining_users_response = requests.get(f"{BASE_URL}/users/", headers=HEADERS)
    assert remaining_users_response.status_code == 200, "Failed to fetch users after deletion"
    remaining_users = remaining_users_response.json()
    assert user_to_delete not in [user["uuid"] for user in remaining_users], "User still exists in the list"

    # 6. Verifikujte da informacije o korisniku ne budu vraćene slanjem GET zahteva sa user uuid na /users/{uuid}/ endpoint.
    user_check_response = requests.get(f"{BASE_URL}/users/{user_to_delete}/", headers=HEADERS)
    assert user_check_response.status_code == 404, "Deleted user is still accessible"