#! python3
# web_scrape.py - Scrapes IMDB list of movies to return a list of movies, dates,
# urls, and synopses 

import requests
from bs4 import BeautifulSoup
import json

topRatedUrl = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
res = requests.get(topRatedUrl)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
print("Start program. Downloading from " + topRatedUrl)

top_250 = []
movies = soup.select(".titleColumn a")    

def buildMovieDic(movie) -> dict:
    """Create dictionary of title, url, year, synopsis from IMDB movie list"""
    dic = {}
    IMDB = "https://imdb.com"
    print("Retrieving data for " + movie.text)
    dic["title"] = movie.text
    dic["url"] = IMDB + movie['href']
    years = soup.select('.titleColumn span')
    dic["year"] = years[0].text

    # Retrieve synopsis from each movie's page
    res = requests.get(dic["url"])
    res.raise_for_status()
    new_soup = BeautifulSoup(res.text, 'html.parser')

    synopsis = new_soup.select(".GenresAndPlot__TextContainerBreakpointXL-cum89p-2")
    dic["synopsis"] = synopsis[0].text

    return dic

# Build dictionary and append to list
for movie in movies[:10]:
    dic = buildMovieDic(movie)
    top_250.append(dic)

# Write list to text file (temporary to check progress) using json string
print("Writing list to text file...")
with open("top250.txt", 'w') as f:
    json.dump(top_250, f, indent=2)