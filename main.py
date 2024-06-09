# Import necessary libraries
from bs4 import BeautifulSoup  # For parsing HTML
import requests  # For making HTTP requests
from csv import writer  # For writing data to CSV files

# Set the number of seasons to scrape
seasons = 5
# Initialize the season index
index = 1

# Open a CSV file for writing
with open('catalog.csv', 'w', encoding='utf8', newline='') as f:
    # Create a CSV writer object
    the_writer = writer(f)
    # Define the header row of the CSV file
    header = ['Season', 'Episode Title', 'Air Date', 'Rating', 'Description']
    # Write the header row to the CSV file
    the_writer.writerow(header)

    # Loop through each season
    while index <= seasons:
        # Construct the URL for the IMDb page of the current season
        URL = f"https://www.imdb.com/title/tt5626028/episodes?season={index}"
        # Get the HTML content of the IMDb page
        html_text = requests.get(URL).text
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_text, 'html.parser')

        # Find all the episodes listed on the page
        episodes = soup.find_all('div', class_='list_item')

        # Loop through each episode
        for episode in episodes:
            # Extract the title of the episode
            episode_title = episode.find('strong').text
            # Extract the air date of the episode
            episode_air_date = episode.find('div', class_='airdate').text.strip()
            # Extract the rating of the episode
            episode_rating = episode.find('span', class_='ipl-rating-star__rating').text.strip()
            # Extract the description of the episode
            episode_description = episode.find('div', class_='item_description').text.strip()
            # Set the season number of the episode
            episode_season = index

            # Create a list containing the episode details
            contents = [episode_season, episode_title, episode_air_date, episode_rating, episode_description]

            # Write the episode details to the CSV file
            the_writer.writerow(contents)

        # Move to the next season
        index += 1
