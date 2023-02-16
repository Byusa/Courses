# composition

# class BOOK {Title, Price, Author}
# class Author {firstName, lastName}

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter=None):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

    def __str__(self):
        return f"{self.name} {self.pages}"


auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 90))
b1.addchapter(Chapter("Chapter 2", 90))
b1.addchapter(Chapter("Chapter 3", 90))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
print(b1.chapters[0].name)
