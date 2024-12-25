import requests
from tests.utils import BASE_URL, HEADERS


def test_search_songs():
    # 1. Pošaljite GET zahtev na /songs/ endpoint kako biste dobili prikaz liste svih pesama.
    response = requests.get(f"{BASE_URL}/songs/", headers=HEADERS)
    assert response.status_code == 200, "Failed to fetch songs"
    songs = response.json()
    assert songs, "No songs found"

    # 2. Izaberite bilo koju pesmu i kopirajte deo njenog imena.
    selected_song = songs[0]  # Prva pesma u listi
    part_of_title = selected_song["title"][:5]  # Prvih 5 karaktera naslova

    # 3. Pripremite query parametar za pretragu sa preuzetim delom naziva pesme.
    search_query = {"search": part_of_title}

    # 4. Pošaljite GET zahtev na /songs/ endpoint sa prethodno pripremljenim parametrom upita.
    search_response = requests.get(f"{BASE_URL}/songs/", headers=HEADERS, params=search_query)

    # 5. Proverite da je kod statusa respons-a 200.
    assert search_response.status_code == 200, "Search request failed"
    search_results = search_response.json()

    # 6. Proverite da su polja respons-a jednaka poljima iz liste pesama koje sadrže izabranu ključnu reč.
    for result in search_results:
        assert part_of_title.lower() in result["title"].lower(), "Search result does not match query"
