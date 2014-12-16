from Item import Item
class Film(Item):
    def __init__(self, type_in, call_num, film_title, subjects_in, director_in, notes_in, year_in):
        self.type = type_in
        self.call_no = call_num
        self.title = film_title
        self.subjects = subjects_in
        self.director = director_in
        self.notes = notes_in
        self.year = year_in

    def title_search(self, phrase) :
        return phrase in self.title

    def other_search(self, phrase) :
        return (phrase in self.notes or phrase in self.director or phrase in self.year)

    def print(self) :
        print ("Film: ")
        print ("Title " + self.title)
        print ("Call No: " + self.call_no)
        print ("Subject: " + self.subjects)
        print ("Director: " + self.director)
        print ("Notes: " + self.notes)
        print ("Year: " + self.year)
