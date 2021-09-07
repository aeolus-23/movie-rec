#! python3
# movie_rec.py - Main program for Movie Recommender

import web_scrape as web
import random_movie as randmov
from os import get_terminal_size
import sys

def main():
    """Main function for Movie Recommender's interface"""
    print("Welcome to Movie Recommender (v0.1)!")
    print("Type 'exit' at any type to exit the program.")
    terminal_size = get_terminal_size()
    options_txt = "MENU OPTIONS"
    menu_options = [
        options_txt.center(terminal_size[0]),
        "=" * int(terminal_size[0]),
        "(1) Web Scraping Functions",
        "(2) Movie Recommender",
        "(3) Recommend me something good! (Quickstart)",
        "(4) Exit",
        "=" * int(terminal_size[0]),
    ]

    for option in menu_options:
        print(option)

    selection = int(input("Your Selection: "))

    if selection == 1:
        print("You selected web scraping")
    elif selection == 2:
        print("Random movies")
    elif selection == 3:
        sys.exit
    else:
        print("Please enter a valid option (1, 2, 3)")
    

if __name__ == "__main__":
    main()