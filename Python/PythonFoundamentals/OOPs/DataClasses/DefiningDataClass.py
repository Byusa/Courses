# Data Classes: 3.7


# class Book:
#     def __init__(self, title, author, pages, price):
#         super().__init__()
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price

from dataclasses import dataclass

# same as above
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title}, by {self.author}"


b1 = Book("Outliers", "Malcolm Gladwell", 300, 39.95)
b2 = Book("Think and grow rich", "Napoleon Hill", 292, 29.95)
b3 = Book("Outliers", "Malcolm Gladwell", 300, 39.95)

# print(b1.title)
# print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
# print(b1)

# TODO: comparing two dataclasses - they implement __eq__
# print(b1 == b3)

# TODO: change some fields
b1.title = "Beza Betty"
b1.pages = 864
print(b1.bookinfo)
