# Data Default

from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book("Outliers", "Malcolm Gladwell", 1225)
b2 = Book("Think and grow rich", "Napoleon Hill", 234)
# attribut without default comes first
print(b1)
print(b2)

# NB: defautl values comes first
