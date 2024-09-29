# Functions
def my_function():
    print("hey")

my_function()

# Arguments
def my_function2(name):
    print("My name is", name)

my_function2("Byusa")

# Parameters and arguments are the samething
# 2 arguments
def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes")

# Arbitrary Arguments, *args
# if you do not know how the number og arguments that will be passed in you use *
# it will recueve a tuple of arguments
def my_function4(*kids):
    print("The youngest child is " + kids[2])

my_function4("Serge", "Jabo", "Byusa")

# keyword argumenent
def my_function5(name, age, place):
    print("I am " + str(age))
    print("and I live in "+ place)
    print("and my name is "+ name)
    
my_function5(place="Vancouver", age=29, name="Byusa")

# Arbitrary keyword Arguments, **kwargs
# if you do not know how many keyword arguments are there
def my_function6(**kid):
    print("His last name is "+ kid["lname"])

my_function6(fname="Serge", lname="Byusa", age=29)

# default parameter
def my_function7(country="Rwanda"):
    print("I am from " + country)

my_function7("Canada")
my_function7()

# Passing List argument 
def my_function8(food):
    for f in reversed(food):
        print(f)

fruits = ["apple", "banana", "cherry"]
my_function8(fruits)

# return values
def my_function9(x):
    return 5 * x
# print(my_function9(5))
# print(my_function9(2))

# The pass statement 
# functions can not be empty but in case you have no content just put in pass
def function10():
    pass

# Recursion
# function that calls itself
# Becareful cause you might write a reciusive function 
# that never terminates, 
# or one that uses excess amounts of memory 
# or one that uses excess processor power
# However written correctly can be efficient and mathematically elegant

# tri_recursion(), we decrement -1 every time we recurse
def tri_recursion(k):
    if(k>0):
        result = 6 + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)


