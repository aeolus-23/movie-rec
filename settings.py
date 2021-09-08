# settings.py - Settings for Movie Recommender

import os

class UISettings():
    """Settings for the terminal-based UI"""
    terminal_size = os.get_terminal_size()
    def __init__(self):
        # Terminal Settings
        self.terminal_columns = UISettings.terminal_size[0]
        
        # Menu Settings
        self.menu_title = "MENU OPTIONS"
        self.menu_options = [
            self.menu_title.center(self.terminal_columns),
            "=" * self.terminal_columns,
            "(1) Show me something good! (Quickstart)",
            "(2) Web Scraping Functions",
            "(3) Offline Movie Recommender",
            "(4) Exit"
        ]


    def print_welcome():
        print("Welcome to movie recommender!")
        print("Enter 'exit' at any time to exit")