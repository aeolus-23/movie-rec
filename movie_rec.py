#! python3
# movie_rec.py - Main program for Movie Recommender

import web_scrape as web
import random_movie as randmov
import sys
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

    if selection.lower() in settings.exit_words:
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
            if prompt.isdigit() and int(prompt) in range(1, len(movies)+1):
                print(movies[int(prompt)-1]["title"])
                break
            elif prompt.lower() == 'all':
                for movie in movies:
                    print(movie["title"])
                break
            elif prompt.lower() in settings.exit_words:
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

        if sub_select.lower() in settings.exit_words:
            sys.exit()

        # Random movies from Top 250 (online)
        elif int(sub_select) == 1:
            movs = web.simple_random_movies_online(url=web.TOP250URL)
            print("=" * settings.terminal_columns)
            for movie in movs:
                print(movie["synopsis"] + "\n")    

        # Random movies from a custom URL
        elif int(sub_select) == 2:
            url = input("Paste your url here: ")       # TODO: Add validation
            movs = web.simple_random_movies_online(url)
            print("=" * settings.terminal_columns)
            for movie in movs:
                print(movie["synopsis"] + "\n")

    # Displays options for offline movie recommendations
    elif int(selection) == 3:
        print("Offline Movie Recommendations [NOT READY]")

    elif int(selection) == 4:
        sys.exit()
    else:
        print("Please enter a valid option.")
    

if __name__ == "__main__":
    main()
