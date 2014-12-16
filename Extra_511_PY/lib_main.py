from Book import Book
from Periodical import Periodical
from Video import Video
from Film import Film
from Search_Engine import Search_Engine

searcher = Search_Engine()
search_type = input("Please enter a search type: ")
search_phrase = input("Please enter a search phrase: ")

matches = []
if(len(search_phrase) <= 2400) :
    matches = searcher.search(search_type, search_phrase)

for i in matches :
    i.print()
    print("")
