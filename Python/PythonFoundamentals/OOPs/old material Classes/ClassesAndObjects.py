# Classes/Objects
# Python is OOPs
# Almost everything in Python is object, with its propeties and methods
# A class is like an object constructor, or a "blueprint" for creating objects

# class, use class to create class
class MyClass:
    x = 5

# Create Object
p1 = MyClass()
print(p1.x)

# The __init__() Function
# All classes have function called __init()__, 
# which is always executed when the class is being initiated
# Use the __init__() function to assign values to object properties,
# or other operations that are neccessary to do when the object is being created:

# __init__() is a => constructor in Java
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Byusa", 29)
print(p1.name)
print(p1.age)

# The __str__() function
# the __str__() fn controls what should be returned when the class object is represented as a string
#  If the __str__() is not set, the string representation of the object is returned

# Without string representation
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Byusa", 29)
print(p1) # returns <__main__.Person1 object at 0x100565350>

# With string representation
# __str__() => is toString() in java
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})" #returns Byusa(29)

p2 = Person2("Byusa", 29)
print(p2)

# Object Methods
# Methods in objects are functions that belong to the object
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def my_function(self, city):
        print("My name is " + self.name + " I am "+ str(self.age) +" and I live in "+ city)
        # We use self paramter to access variables that belong to the class

p3 = Person3("Serge", 29)
p3.my_function("Vancouver")

# The Self Parameter
# The self parameter is a reference to the current instance of the class,
# and is used to access variabls that belongs to the class
# eg: let replace abc with self
class Person4:
  def __init__(abc, name, age):
    abc.name = name
    abc.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p4 = Person4("John", 36)
p4.myfunc()

# You can modify object properties
p4.age = 29
print("Age " + str(p4.age))

# Delete Object Properties
# del
del p4.age

# Delete Objects
del p4

# Pass Statement
# class definition can be empty
class Person5:
    pass


