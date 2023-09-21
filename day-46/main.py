from bs4 import BeautifulSoup
import requests
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import os


API_LINK = 'https://www.billboard.com/charts/hot-100/2000-08-12/'


# to_year = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(API_LINK)

soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all(name='h3', id='title-of-a-story', class_='a-no-trucate')

# song_titles = []
# for title in titles:
#     song_titles.append(title.getText().strip())

# print(song_titles)

song_titles = [title.getText().strip() for title in titles]
print(song_titles)
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])
# print(os.getenv("SPOTIPY_CLIENT_ID"))

new_paylist = spotify.user_playlist_create(user=os.getenv("SPOTIPY_CLIENT_ID"), name='food', public=False, description="Trieal Shit")

# for song_title in song_titles:
#     results = spotify.search(q=f'track:{song_title}year:2000', type='track')
#     print(results['tracks']['href'])