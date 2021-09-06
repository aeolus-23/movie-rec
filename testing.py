# testing.py - Temp file for testing functions for MovieRec program
import web_scrape as web
import random_movie as select

movie_list = web.retrieve_top_250_online()
web.writeJson("top250.json", movie_list)


# rand_syn = select.three_random_synopses(movie_list)
# for synopsis in rand_syn:
#     print("\n" + synopsis)