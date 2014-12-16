class Date:
    def __init__(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    def display(self):
        print(str(self.month) + "/" + str(self.day) + "/" + str(self.year))
