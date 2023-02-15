# Inheritance and composition

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    # initialize function  (constructor in other languanges)
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book("Outliers", "Malcolm Gladwell", 300, 29.0)
n1 = Newspaper("ChatGPT vs Barrier", "John", 6.0, "Daily")
m1 = Magazine("Sci fi", "Serge", 300, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
