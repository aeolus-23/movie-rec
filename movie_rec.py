#! python3
# movie_rec.py - Main program for Movie Recommender

import web_scrape as web
import random_movie as randmov
from os import get_terminal_size
import sys
from random import choice
from settings import UISettings

def main():
    """Main function for Movie Recommender's interface"""
    UISettings.print_welcome()
    settings = UISettings()
    terminal_size = get_terminal_size()

    for option in settings.menu_options:
        print(option)

    selection = input("Your Selection: ")

    if selection.lower() == "exit":
        sys.exit()

    if int(selection) == 1:
        print("You selected web scraping [NOT READY]")
    elif int(selection) == 2:
        print("Random movies [NOT READY]")
    
    # Displays 3 synopses from a randomly chosen movie data JSON file in .\data
    elif int(selection) == 3:
        print("Quickstart [NOT READY]")
        movie_data = randmov.check_for_json()
        if movie_data:
            selected_file = choice(movie_data)
            # TODO: Check for better way to format filename argument
            movies = web.retrieve_top_250_offline(".\data\\" + selected_file)
            synopses = randmov.three_random_synopses(movies)
            for synopsis in synopses:
                print("=" * int(terminal_size[0]))
                print(synopsis.center(terminal_size[0]))
        elif movie_data == False:
            print("No downloaded movie data found.")

    elif int(selection) == 4:
        sys.exit()
    else:
        print("Please enter a valid option (1, 2, 3)")
    

if __name__ == "__main__":
    main()
