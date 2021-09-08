#! python3
# web_scrape.py - Scrapes IMDB list of movies to return a list of movies, dates,
# urls, and synopses 

import requests
from bs4 import BeautifulSoup
import json
import random

# CONSTANTS
MOST_POP_URL = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

def buildMovieDic(movie, verbose=True) -> dict:
    """Create dictionary of title, url, year, synopsis from IMDB movie list"""
    dic = {}
    IMDB = "https://imdb.com"
    if verbose:         # Prints info for each movie
        print("Retrieving data for " + movie.text)
    dic["title"] = movie.text
    dic["url"] = IMDB + movie['href']

    # Retrieve synopsis from each movie's page
    res = requests.get(dic["url"])
    res.raise_for_status()
    new_soup = BeautifulSoup(res.text, 'html.parser')

    # Scrape data from each movie's individual page
    synopsis = new_soup.select(".GenresAndPlot__TextContainerBreakpointXL-cum89p-2")
    dic["synopsis"] = synopsis[0].text
    year  = new_soup.select('.TitleBlockMetaData__MetaDataList-sc-12ein40-0 > li:nth-child(1) > span:nth-child(2)')
    dic["year"] = year[0].text

    return dic

def writeJson(filename: str, data): 
    """Writes data to JSON file"""
    try:
        print("Writing to file " + filename)
        with open(filename, 'w') as out_file:
            json.dump(data, out_file, indent=2)
        print("Finished writing to file.")
    except FileNotFoundError:
        print("Could not find destination file.")
        print("Did not write data.")

def retrieve_top_250_online() -> list:
    """Returns list of movie dictionaries retrieved from IMDB top250"""
    # Retrieves movies and writes list to JSON filename specified
    TOP250URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    res = requests.get(TOP250URL)
    top_250 = []
    if res.status_code == 200:
        print("Connected. Downloading from " + TOP250URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        movies = soup.select(".titleColumn a")  

        # Loop through movies and build dictionary, appending to list
        for movie in movies[:100]:
            dic = buildMovieDic(movie)    
            top_250.append(dic)

        return top_250
    elif res.status_code != 200:
        print("Could not connect to " + TOP250URL)

def retrieve_top_250_offline(filename) -> list:
    """Returns list of movie dictionaries from offline JSON file of top 250"""
    try:
        with open(filename, 'r') as f:
            top_250 = json.load(f)
            return top_250
    except FileNotFoundError:
        print("Could not find your file.")

def retrieve_most_popular_online() -> list:
    """Returns list of movies from the IMDb chart - Most Popular Movies"""

    # TODO: Write function to validate network connection before requests.get
    
    res = requests.get(MOST_POP_URL)
    most_pop_movies = []
    if res.status_code == 200:
        print("Downloading from " + MOST_POP_URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        movies = soup.select(".titleColumn a")

        for movie in movies:
            dic = buildMovieDic(movie)
            most_pop_movies.append(dic)

        return most_pop_movies

    elif res.status_code != 200:
        print("Could not connect to " + MOST_POP_URL)

def simple_random_movies_online(url=MOST_POP_URL) -> list:
    """Returns a list of dictionaries for three randomly chosen movies.
    Requires url argument (Defaults to most popular)."""
    # TODO: Write function to validate url
    try:
        res = requests.get(url)
    except requests.exceptions.RequestException as err:     # Not working??
        print(f"An error occured: {err}")
    except requests.exceptions.ConnectionError:
        print(f"A connection error occured: {requests.ConnectionError}")
    except requests.exceptions.NewConnectionError:
        print(f"Error: {requests.NewConnectionError}")

    three_random_movies = []
    if res.status_code == 200:
        print("Downloading three random movies from " + url)
        soup = BeautifulSoup(res.text, 'html.parser')
        movies = soup.select(".titleColumn a")       # All movies on page list

        sel_movies = random.sample(movies, 3)
        for movie in sel_movies:
            dic = buildMovieDic(movie, verbose=False)
            three_random_movies.append(dic)

        return three_random_movies

    elif res.status_code != 200:
        print("Could not connect to " + url) 