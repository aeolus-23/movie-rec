#! python3
# random_movie.py - Selects random movie(s) from list to display and watch!

import random
import web_scrape as web
import os

def three_random_synopses(data: list) -> list:
    """Returns three random synopses (with no titles)"""
    sel_movies = random.sample(data, 3)
    synopses = [movie["synopsis"] for movie in sel_movies]
    return synopses

def check_for_json():
    """Checks if JSON files with moveie data already exist"""
    json_files = os.listdir(".\data")
    if json_files:
        return json_files
    else:
        return []