class Item:
    def __init__(self, call_no_in, subject_in, type_in) :
        self.call_no = call_no_in
        self.subject = subject_in
        self.type = type_in

    def call_no_search(self, phrase) :
        return phrase in self.call_no

    def subject_search(self, phrase) :
        return phrase in self.subjects

