#! python3
# movie_rec.py - Main program for Movie Recommender

import web_scrape as web
import random_movie as randmov
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

    # Quickstart - shows 3 random movies from online
    elif int(selection) == 1:
        movies = web.simple_random_movies_online()
        print("=" * settings.terminal_columns)
        for movie in movies:
            print(movie["synopsis"] + "\n")
        print("=" * settings.terminal_columns)
        
        new_menu = True        # Flag for running while loop for showing titles
        while new_menu == True:
            print("Enter a number to see that movie's title, or 'all' to see all")
            prompt = input("Your selection: ")
            # Shows movies corresponding to list slice (e.g. 1 -> movies[0])
            if type(prompt) == int:
                if int(prompt) in range(0, len(movies)):
                    print(movies[int(prompt)-1]["title"])
                    break
            elif prompt.lower() == 'all':
                for movie in movies:
                    print(movie["title"])
                break
            elif prompt.lower() == "exit":
                sys.exit()
            else:
                print("Please enter a correct option.")
                continue

    # Displays options for online movie recommendations
    elif int(selection) == 2:
        # Show the online service sub-menu
        for option in settings.web_scrape_menu:
            print(option)
        sub_select = input("Your Selection: ")

        if sub_select.lower() == "exit" or "quit":
            sys.exit()

        # Random movies from Top 250 (online)
        elif int(sub_select) == 1:
            movs = randmov.three_random_synopses(web.retrieve_top_250_online())
            for movie in movs:
                print(movie["synopsis"])

        # Random movies from a custom URL
        elif int(sub_select) == 2:
            print("[NOT READY YET]")
            movs = randmov.three_random_synopses(web.retrieve_from_custom_url())
            for movie in movs:
                print(movie["synopsis"])

    # Displays options for offline movie recommendations
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
        print("Please enter a valid option.")
    

if __name__ == "__main__":
    main()
