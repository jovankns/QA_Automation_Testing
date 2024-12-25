import requests
from tests.utils import BASE_URL, HEADERS


def test_update_user_conflict():
    # 1. Pošaljite GET zahtev na /users/ endpoint za prikaz liste korisnika.
    response = requests.get(f"{BASE_URL}/users/", headers=HEADERS)
    assert response.status_code == 200, "Failed to fetch users"
    users = response.json()
    assert len(users) >= 2, "Not enough users to test conflict scenario"

    # 2. Odaberite dva korisnika (jednog za ažuriranje, drugog za podatke).
    user_to_update = users[0]  # Prvi korisnik u listi
    conflicting_user = users[1]  # Drugi korisnik u listi

    # 3. Ispunite payload zahtev sa već zauzetim email-om ili nadimkom.
    payload = {
        "email": conflicting_user["email"]  # Koristimo email drugog korisnika
    }

    # 4. Koristite uuid prvog korisnika u /users/{uuid}/ endpoint-u.
    update_user_uuid = user_to_update["uuid"]

    # 5. Pošaljite PATCH zahtev sa payload-om na endpoint /users/{uuid}/.
    patch_response = requests.patch(
        f"{BASE_URL}/users/{update_user_uuid}/",
        headers=HEADERS,
        json=payload
    )

    # 6. Osigurajte da odgovor sa statusom 409 bude primljen i da poruka "already taken" bude prikazana.
    assert patch_response.status_code == 409, "Expected status code 409 but got something else"
    error_message = patch_response.json().get("message", "")
    assert "already taken" in error_message, "Conflict error message not found in response"
    assert conflicting_user["email"] in error_message, "Conflicting email not mentioned in error message"
