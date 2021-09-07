import unittest
import web_scrape as web

def sample_movie():
    """Returns a sample movie dictionary for testing"""
    sample_dict = {}
    sample_dict["title"] = "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb"
    sample_dict["year"] = "1964"
    sample_dict["url"] = "https://www.imdb.com/title/tt0057012/?ref_=fn_al_tt_1"
    synopsis = (
        "An insane general triggers a path to nuclear holocaust "
        "that a War Room full of politicians and generals "
        "frantically tries to stop."
    )
    sample_dict["synopsis"] = synopsis

    return sample_dict

class TestScrape(unittest.TestCase):
    """Tests for functions in web_scrape.py"""

