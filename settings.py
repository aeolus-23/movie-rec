# settings.py - Settings for Movie Recommender

import os
import web_scrape, movie_rec

class UISettings():
    """Settings for the terminal-based UI"""
    terminal_size = os.get_terminal_size()
    def __init__(self):
        # Terminal Settings
        self.terminal_columns = UISettings.terminal_size[0]
        
        # Menu Settings
        self.menu_title = "MENU OPTIONS"
        self.menu_options = [           # Change to dictionary of key: func?
            self.menu_title.center(self.terminal_columns),
            "=" * self.terminal_columns,
            "(1) Show me something good! (Quickstart)",
            "(2) Online Movie Recommendations",
            "(3) Offline Movie Recommendions",
            "(4) Exit",
            "=" * self.terminal_columns,
        ]

        # SubMenu Settings
        self.web_scrape_menu = [
            self.menu_title.center(self.terminal_columns),
            "=" * self.terminal_columns,
            "(1) Random selections from IMDb Top 250"
            "(2) Random selections from today's most popular movies",
            "(3) Random selections from custom IMDb list [NOT WORKING]"
        ]


    def print_welcome():
        print("Welcome to movie recommender!")
        print("Enter 'exit' at any time to exit")

    def format_menu(self, menu: dict):
        """Takes dictionary of menu items and prints pretty menu"""
        print(self.menu_title.center(self.terminal_columns))    # Menu Title
        print("=" * self.terminal_columns)          # Adds nice line break
        for item in menu:
            print(item["text"])
        print("=" * self.terminal_columns)
