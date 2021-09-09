#! python3
# random_movie.py - Selects random movie(s) from list to display and watch!

import random
import web_scrape as web
import os

def three_random_synopses(data: list) -> list:
    """Returns three random synopses (with no titles)"""

    # Validate data is a list and check its length
    if type(data) == list:   
        if len(data) > 3:
            sel_movies = random.sample(data, 3)
        elif len(data) < 3:
            sel_movies = data
        return sel_movies
    elif type(data) != list:
        print("Your data type is not a list. Please double check your data.")

def check_for_json():
    """Checks if JSON files with moveie data already exist"""
    json_files = os.listdir(".\data")
    if json_files:
        return json_files
    else:
        return []