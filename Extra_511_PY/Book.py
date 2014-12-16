from Item import Item
class Book(Item):
    def __init__(self, type_in, call_num, book_title, subjects_in, author_in, desc_in, pub_in, city_in, year_in, series_in, notes_in):
        self.type = type_in
        self.call_no = call_num
        self.title = book_title
        self.subjects = subjects_in
        self.author = author_in
        self.description = desc_in
        self.publisher = pub_in
        self.city = city_in
        self.year = year_in
        self.series = series_in
        self.notes = notes_in

    def title_search(self, phrase) :
        return phrase in self.title

    def other_search(self, phrase) :
        return (phrase in self.description or phrase in self.notes or phrase in self.year)

    def print(self) :
        print ("Book: ")
        print ("Title " + self.title)
        print ("Call No: " + self.call_no)
        print ("Subject: " + self.subjects)
        print ("Author: " + self.author)
        print ("Description: " + self.description)
        print ("Publisher: " + self.publisher)
        print ("Series: " + self.series)
        print ("Notes: " + self.notes)
        print ("City: " + self.city)
        print ("Year: " + self.year)
    
