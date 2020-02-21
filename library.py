import math 

class Library:

    def __init__(self, id = None, booksCount= None, initTime= None, rate= None, books= None):
        self.id = id
        self.booksCount = booksCount
        self.initTime = initTime
        self.rate = rate
        self.books = books


    def totalScore(self):
        return sum(map(lambda book: book.score, self.books))

    def workingDays(self):
        return self.initTime + math.ceil(len(self.books) / self.rate)

    def coef(self):
        #return len(self.books) * self.totalScore  / self.workingDays / self.initTime
        return (self.totalScore())  / (self.workingDays() +  self.initTime )

    def sortBooks(self):
        return sorted(self.books, key=lambda l: -l.score)
        