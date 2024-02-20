import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='ec189d68337241c9a262029930d446bc', client_secret='5490f2e618f541e785f7baad5c30604e', redirect_uri='http://example.com',scope=scope))

userid = sp.current_user()
print(userid["id"])
#
date_str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/"+date_str
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
#
# # get all song titles
titles = soup.select("li ul li h3")
song_names = [t.get_text().strip() for t in titles]
print(song_names)


# get all artists
