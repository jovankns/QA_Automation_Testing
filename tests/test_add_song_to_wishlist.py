import requests
from tests.utils import BASE_URL, HEADERS

def test_add_song_to_wishlist():
    # 1. Pošaljite GET zahtev na /users/ endpoint za prikaz liste korisnika
    users_response = requests.get(f"{BASE_URL}/users/", headers=HEADERS)
    assert users_response.status_code == 200, "Failed to fetch users"
    users = users_response.json()

    # 2. Odaberite bilo kog korisnika i uzmite njegov uuid
    assert len(users) > 0, "No users found"
    user_uuid = users[0]["uuid"]

    # 3. Pošaljite GET zahtev na /songs/ endpoint za prikaz liste svih pesama
    songs_response = requests.get(f"{BASE_URL}/songs/", headers=HEADERS)
    assert songs_response.status_code == 200, "Failed to fetch songs"
    songs = songs_response.json()

    # 4. Odaberite pesmu koju želite da dodate i uzmite njen uuid
    assert len(songs) > 0, "No songs found"
    song_uuid = songs[0]["uuid"]

    # 5. Ispunite polje item_uuid sa uuid-om pesme u payload zahtevu
    payload = {
        "item_uuid": song_uuid
    }

    # 6. Koristite uuid korisnika kao parametar u /users/{uuid}/wishlist/add/ endpoint-u
    wishlist_add_url = f"{BASE_URL}/users/{user_uuid}/wishlist/add/"
    add_response = requests.post(wishlist_add_url, headers=HEADERS, json=payload)

    # 7. Proverite da je statusni kod odgovora 200
    assert add_response.status_code == 200, "Failed to add song to wishlist"

    # 8. Potvrdite da je pesma dodata na wishlist-u korisnika
    wishlist_url = f"{BASE_URL}/users/{user_uuid}/wishlist/"
    wishlist_response = requests.get(wishlist_url, headers=HEADERS)
    assert wishlist_response.status_code == 200, "Failed to fetch wishlist"

    # Debug: Ispiši odgovor API-ja za wishlist
    wishlist = wishlist_response.json()
    print("Wishlist response:", wishlist)

    # 9. Proverite da je pesma prisutna na wishlist-i korisnika
    items = wishlist.get("items", [])
    added_song = next((item for item in items if item["uuid"] == song_uuid), None)
    assert added_song is not None, "Song was not added to wishlist"
