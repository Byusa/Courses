# Equality and comparison

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objecs
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book ")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book ")

        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book ")

        return self.price < value.price


b1 = Book("I will teach you to be rich", "Raj", 40)
b2 = Book("Think and grow rich", "Napoleon Hill", 29.95)
b3 = Book("I will teach you to be rich", "Raj", 40)
b4 = Book("Designing Data Intensive Apps", "Someone", 45)

# TODO: to check for equality
print(b1 == b2)
print(b1 == b3)
# print(b1 == 4) # this will raise value error

# TODO: to check for greater and lesser value
print(b1 >= b2)
print(b1 < b2)

# TODO: Now we can sort them too
books = [b1, b3, b2, b4]
books.sort()  # books are sorted from the high price to low price
print([book.title for book in books])
