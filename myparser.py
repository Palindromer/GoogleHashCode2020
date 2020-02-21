
from book import Book
from library import Library

class MyParser: 
    def ParseFile(self, fileName):
        f = open("./data/" + fileName, "r")
        fileLines = f.read().split('\n')

        lines = list(map(lambda line: line.split(' '), fileLines))

        booksCount = int(lines[0][0])
        librariesCount = int(lines[0][1])
        days = int(lines[0][2])

        books = []
        for i in range(len(lines[1])):
            book = Book(i, int(lines[1][i]))
            book.isUsed = False
            books.append(book)

        libraries = []

        i = 1
        while i < int(librariesCount) * 2:
            i += 1
            id = i - 2
            library = Library()
            library.id = int((i  - 2) / 2)
            library.booksCount = int(lines[i][0])
            library.initTime = int(lines[i][1])
            library.rate = int(lines[i][2])

            library.books = []
            i += 1
            for id in range(len(lines[i])):
                bookId = int(lines[i][id])
                library.books.append(books[bookId])

            library.totalScore = library.totalScore()
            library.workingDays = library.workingDays()
            library.coef = library.coef()
            library.books = library.sortBooks()

            libraries.append(library)

        return books, libraries