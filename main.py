from bs4 import BeautifulSoup
import requests
from csv import writer

seasons = 5
index = 1

with open('catalog.csv', 'w', encoding='utf8', newline='') as f:
    the_writer = writer(f)
    header = ['Season', 'Episode Title', 'Air Date', 'Rating', 'Description']
    the_writer.writerow(header)

    while index <= seasons:

        URL = f"https://www.imdb.com/title/tt5626028/episodes?season={index}"
        html_text = requests.get(URL).text
        soup = BeautifulSoup(html_text, 'html.parser')

        episodes = soup.find_all('div', class_='list_item')

        for episode in episodes:
            episode_title = episode.find('strong').text
            episode_air_date = episode.find('div', class_='airdate').text.strip()
            episode_rating = episode.find('span', class_='ipl-rating-star__rating').text.strip()
            episode_description = episode.find('div', class_='item_description').text.strip()
            episode_season = index

            contents = [episode_season, episode_title, episode_air_date, episode_rating, episode_description]

            the_writer.writerow(contents)

        index += 1
