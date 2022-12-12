# Python Inheritance 
# Inheritance allows us to define a class that inherits all the methods
# and properties from another class
# Parent class = class being inherited from (base class)
# Child class = class that inherits (derived class)

# Create a parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a child class
# Class Student inherit properties and methods from the Person class
class Student(Person):
    pass

# use Student to create object and use printname method
s = Student("Serge", "Byusa")
s.printname()

# Add __init__() function
class Student1(Person):
    def __init__(self, fname, lname):
        # add properties
        pass
# when you add __init__() in child it no longer inherit parent's __init__() function
# to keep parent's __init__() function, add a call to the parent's __init__() function

class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) #successfully kept inheritance from parents

x = Student2("inheriting all from Parent", "with Parent.")
x.printname()

# super() function => super() will make child class inherits all the methods and properities 
# from its parent
class Student3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student3("inheriting all from Parent", "with Super.")
x.printname()

# Add properties
# add graduationYear to Student class
class Student4(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear = 2020
x = Student3("add propetry", "graduationYear")
x.printname()

class Student5(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

x = Student5("More propetry", "graduationYear", 2019)
x.printname()
print(x.graduationYear)

# Add Methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
class Student6(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    

  def welcome(self):
        print("Welcome " , self.firstname, self.lastname,  "to the class of ", self.graduationyear )

x = Student6("Jabo Serge", "Byusa", 2020)
x.welcome()
