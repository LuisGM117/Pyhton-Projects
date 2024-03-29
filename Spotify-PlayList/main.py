import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# MAKE SURE TO FOLLOW THE INSTRUCTIONS BEFORE RUN THE CODE


#CHECK THE INSTRUCTIONS DOCUMENT TO GET YOUR KEYS
CLIENT_ID = #YOUR CLIENT ID
CLIENT_SCRT = #YOUR CLIENT SECRET

chooseDate = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{chooseDate}")
soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")

titles = [song.getText().strip() for song in songs ]

print(titles)

#AUTHENTICATING
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SCRT,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = chooseDate.split("-")[0]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{chooseDate} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)