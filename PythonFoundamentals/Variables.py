# Python foundamentals course (https://www.w3schools.com/python/default.asp)
print("Hello world")
# 1) Variables

# A)casting
x = str(3)
y = int(3)
z = float(3)
# get type
print(type(x))
# variable names
my_var = "snake_case"  # Snake Case
MYVAR = "PASCALCASE"  # Pascal Case
myVarName = "CamelCase"  # CamelCase 



# B) Assign Multiple Values
# Many values to multiple variables
x, y, z = 1, 92, 4
print(x)
print(y)
print(z)
# one value to multiple variables
x = y = z = 5
print(x)
print(y)
print(z)

# unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# C) Output Variables
x = "Python "
y = "is "
z = "awesome "
print(x, y, z)
print(x + y + z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x, y)

# D) Global Variables 
# D1)
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# D2) if you use global keyword, x is use globally, 
# this changes the value of x 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

