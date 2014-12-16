from Item import Item
class Periodical(Item):
    def __init__(self, type_in, call_num, period_title, subjects_in, author_in, desc_in, pub_in, pub_hist_in, series_in, notes_in, related_titles_in, other_forms_in, govt_doc_num_in):
        self.type = type_in
        self.call_no = call_num
        self.title = period_title
        self.subjects = subjects_in
        self.author = author_in
        self.description = desc_in
        self.publisher = pub_in
        self.publishing_history = pub_hist_in
        self.series = series_in
        self.notes = notes_in
        self.related_titles = related_titles_in
        self.other_forms_of_title = other_forms_in
        self.govt_doc_num = govt_doc_num_in

    def title_search(self, phrase) :
        return phrase in self.title

    def other_search(self, phrase) :
        return (phrase in self.description or phrase in self.notes or phrase in self.series or phrase in self.related_titles)

    def print(self) :
        print ("Periodical: ")
        print ("Title " + self.title)
        print ("Call No: " + self.call_no)
        print ("Subject: " + self.subjects)
        print ("Author: " + self.author)
        print ("Description: " + self.description)
        print ("Publisher: " + self.publisher)
        print ("Publishing History: " + self.publishing_history)
        print ("Series: " + self.series)
        print ("Notes: " + self.notes)
        print ("Related Titles: " + self.related_titles)
        print ("Other Forms of Title: " + self.other_forms_of_title)
        print ("Gov't Doc Number: " + self.govt_doc_num)
