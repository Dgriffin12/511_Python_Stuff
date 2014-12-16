from Book import Book
from Periodical import Periodical
from Video import Video
from Film import Film

class Search_Engine :
    def __init__ (self) :
        self.data_container = []
        book_file = open("book.txt", 'r')
        for line in book_file :
            data = []
            parsed_line = line.split('|')
            for i in range(0,10) :
                data.append(parsed_line[i])
            new_book = Book("Book", data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
            del data[:]
            self.data_container.append(new_book)

        periodical_file = open("periodical.txt", 'r')
        for line in periodical_file :
            data = []
            parsed_line = line.split('|')
            for i in range(0,12 ) :
                data.append(parsed_line[i])
            new_periodical = Periodical("Periodical", data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]) 
            del data[:]
            self.data_container.append(new_periodical)

        video_file = open("video.txt", 'r')
        for line in video_file :
            data = []
            parsed_line = line.split('|')
            for i in range(0,8) :
                data.append(parsed_line[i])
            new_video = Video("Video", data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]) 
            del data[:]
            self.data_container.append(new_video)

        film_file = open("film.txt", 'r')
        for line in film_file :
            data = []
            parsed_line = line.split('|')
            for i in range(0, 6) :
                data.append(parsed_line[i])
            new_film = Film("Film", data[0], data[1], data[2], data[3], data[4], data[5]) 
            del data[:]
            self.data_container.append(new_film)
            
    def search(self, search_type, phrase) :
        matches = []
        if(search_type == "call number") :
            for i in self.data_container :
                if(i.call_no_search(phrase)) :
                    matches.append(i)
        if(search_type == "title") :
            for i in self.data_container :
                if(i.title_search(phrase)) :
                    matches.append(i)
        if(search_type == "subject") :
            for i in self.data_container :
                if(i.subject_search(phrase)) :
                    matches.append(i)
        if(search_type == "other") :
            for i in self.data_container :
                if(i.other_search(phrase)) :
                    matches.append(i)

        return matches
