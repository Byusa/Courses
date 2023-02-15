
# TODO: create a basic class
class Book:
    # initialize function  (constructor in other languanges)
    def __init__(self, title, author, pages, price):
        self.title = title
        #  TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        # this property can not be seen outside the class
        self.__secret = "This is a secret attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price*self._discount)
        return self.price

    def setdiscount(self, amount):
        # _ means that it is internal to the the class not used outside of the class
        self._discount = amount


# TODO: create instances of the class
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.9)
b2 = Book("Outlers", "Malcolm Gladwell", 300, 40.0)

print(b2.title)

# TODO: print the price
print("Getting the price ", b2.getprice())

# TODO: try setting the discount
b2.setdiscount(0.25)
print("Price after applying discount ", b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
# print("getting secret ", b2.__secret) # This can not be  accessed outside the class
print("getting secret ", b2._Book__secret) # here is how you can access

###### TypeCheck######


class NewsPaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
# b11 = Book("I will teach you to be rich", )
# b22 = Book("Desinging data intensive applications")
n1 = NewsPaper("ChatGPT vs barrier")
n2 = NewsPaper("M23 vs FDRL")

print(type(b1))
print(type(n1))

# types
print(type(b1) == type(b2))
print(type(b1) == type(n1))

# TODO: use isinstance to compare a specifit instanfe to known type
print(isinstance(b1, Book))
print(isinstance(n1, NewsPaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))  # all classes is instance of object




#  ########### Book2 ###############

class Book2:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod  # this works on class instance not object
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book2.__booklist == None:
            Book2.__booklist = []
        return Book2.__booklist

    # instance methods recieve a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (booktype not in Book2.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


print("Book types: ", Book2.getbooktypes())
b3 = Book2("Title 1", "HARDCOVER")
b4 = Book2("Title 2", "EBOOK")
# b5 = Book2("Title 2", "SOMEBOOK")  # This will throw the error

# TODO: Use the static method to access a singleton object (can be accessed but not modifieable)
thebooks = Book2.getbooklist()
print(thebooks)
thebooks.append(b3)
thebooks.append(b4)
print(thebooks)






