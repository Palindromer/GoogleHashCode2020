from book import Book
from library import Library
from myparser import MyParser 

fileNames = ["1.txt","2.txt","3.txt","4.txt","5.txt","6.txt"]


def writeLibrary(f, library):
    lineStr = str(library.id) + " " + str(len(library.books))
    f.write(lineStr)
    f.write('\n')

    bookScoreStr = " ".join(map(lambda book: str(book.id), library.books))
    f.write(bookScoreStr)
    f.write('\n')


def process(fileName):
    parseResult = MyParser().ParseFile(fileName)
    books = parseResult[0]
    libraries = parseResult[1]

    sortedLibraries = sorted(libraries, key=lambda l: -l.coef)
    #sortedLibraries  = libraries 
    f = open("./out/" + fileName, "w")


    emptyLibraries = []

    for library in sortedLibraries:
        for book in library.books:
            if (books[book.id].isUsed == True):
                library.books.remove(books[book.id])
            books[book.id].isUsed = True
        
        sortedLibraries.remove(library)

        if len(library.books) > 0:
            writeLibrary(f, library)
        else:
            emptyLibraries.append(library)
        
        library.isUsed = True

    f.close()
    
    with open("./out/" + fileName, "r") as original: data = original.read()
    with open("./out/" + fileName, "w") as modified: modified.write((str(len(sortedLibraries) - len(emptyLibraries)) + '\n' + data))



process(fileNames[0])
process(fileNames[1])
process(fileNames[2])
process(fileNames[3])
process(fileNames[4])   
process(fileNames[5])


pass

