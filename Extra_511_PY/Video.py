from Item import Item
class Video(Item):
    def __init__(self, type_in, call_num, video_title, subjects_in, description_in, dist_in, notes_in, series_in, label_in):
        self.type = type_in
        self.call_no = call_num
        self.title = video_title
        self.subjects = subjects_in
        self.description = description_in
        self.distributor = dist_in
        self.notes = notes_in
        self.label = label_in
        self.series = series_in

    def title_search(self, phrase) :
        return phrase in self.title

    def other_search(self, phrase) :
        return (phrase in self.notes or phrase in self.description or phrase in self.distributor)

    def print(self) :
        print ("Video: ")
        print ("Title " + self.title)
        print ("Call No: " + self.call_no)
        print ("Subject: " + self.subjects)
        print ("Description: " + self.description)
        print ("Distributor: " +self.distributor)
        print ("Series: " + self.series)
        print ("Notes: " + self.notes)
        print ("Label: " + self.label)
