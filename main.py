from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/film/best-movies-of-all-time"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
h3_element = soup.find_all(name="h3", class_="_h3_cuogz_1")
all_movies = [movie.getText() for movie in h3_element]
all_movies_cleaned = [movie.replace('\xa0', ' ') for movie in all_movies]


with open ("movies.txt", mode="w") as file:
    for movie in all_movies_cleaned:
        file.write(f"{movie}\n")





















