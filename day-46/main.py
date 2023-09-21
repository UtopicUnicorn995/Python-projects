from bs4 import BeautifulSoup
import requests
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials


API_LINK = 'https://www.billboard.com/charts/hot-100/2000-08-12/'
CLIENT_ID = '1bf8c7025249496c9fbd98f8e720937a'
CLIENT_SECRET = 'e1eff8c05845485f8d1dacbf5d8b642a'
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