

import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")  # website to be scraped
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")  # created a soup

all_movies = soup.find_all(name="h3", class_="title")

all_movies_names = [movie.getText() for movie in all_movies]  # putting all movies names into all_movies_list list


all_movies_names.reverse()  # reversed a list

with open("movies.txt", "w") as file:  # created file and writing movies names in it
    for movie in all_movies_names:
        file.write(f"{movie} \n")

