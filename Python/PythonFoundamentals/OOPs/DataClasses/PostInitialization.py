# post initialization
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties (pages in this case)
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


b1 = Book("Outliers", "Malcolm Gladwell", 300, 39.95)
b2 = Book("Think and grow rich", "Napoleon Hill", 292, 29.95)
b3 = Book("Outliers", "Malcolm Gladwell", 300, 39.95)

#  TODO: use the description attribute
print(b1.description)
print(b2.description)

