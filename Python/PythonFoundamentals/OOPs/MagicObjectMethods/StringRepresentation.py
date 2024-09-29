# String representation
# Using the __str__ and __repr__ magic methods

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: user the __repr__ method to return an obj representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"


b1 = Book("Outliers", "Malcolm Gladwell", 39.95)
b2 = Book("Think and grow rich", "Napoleon Hill", 29.95)

print(b1)
print(b2)

print(str(b1))
print(repr(b1))

# It is usually recommended to create a __repr__
# for class you create to make debugging easier

# it is preferable to use the repr() method over the str() method when
# =>> You need an exact representattion of the object during development and debuggind tasks
