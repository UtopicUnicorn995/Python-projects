from bs4 import BeautifulSoup
import lxml
import requests
import os

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__hW_Kn')

movie_list = []
for movie in movies:
    movie_list.append(movie.getText())
    
movie_list.reverse()
    
for movie in movie_list:
    print(movie)

with open('./movies.txt', mode='w') as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
