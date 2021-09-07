# settings.py - Settings for Movie Recommender

import os

class UISettings():
    """Settings for the terminal-based UI"""
    def __init__(self):
        # Terminal Settings
        self.terminal_size = os.get_terminal_size
        self.terminal_columns = self.terminal_size[0]
        
        

    def print_welcome():
        print("Welcome to movie recommender!")
        print("Enter 'exit' at any time to exit")