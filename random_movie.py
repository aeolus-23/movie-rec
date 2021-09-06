#! python3
# random_movie.py - Selects random movie(s) from list to display and watch!

import random, json
import web_scrape as web

def three_random_synopses(data: list) -> list:
    """Returns three random synopses (with no titles)"""
    sel_movies = random.sample(data, 3)
    synopses = [movie["synopsis"] for movie in sel_movies]
    return synopses