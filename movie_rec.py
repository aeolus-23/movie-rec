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
    settings = UISettings()
    # Display the main menu
    UISettings.print_welcome()
    for option in settings.menu_options:
        print(option)
    selection = input("Your Selection: ")

    # TODO: Fix selections and add corresponding functions (change to loop?)

    if selection.lower() == "exit":
        sys.exit()

    if int(selection) == 1:
        print("You selected web scraping [NOT READY]")

    # Recommend from Online (web scraping)
    elif int(selection) == 2:
        # Show the online service sub-menu
        for option in settings.web_scrape_menu:
            print(option)

        sub_select = input("Your Selection: ")
    
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
                print("=" * settings.terminal_columns)
                print(synopsis.center(settings.terminal_columns))
        elif movie_data == False:
            print("No downloaded movie data found.")

    elif int(selection) == 4:
        sys.exit()
    else:
        print("Please enter a valid option (1, 2, 3)")
    

if __name__ == "__main__":
    main()
