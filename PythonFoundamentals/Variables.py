# Python foundamentals course (https://www.w3schools.com/python/default.asp)
print("Hello world")
# 1) Variables
# casting
x = str(3)
y = int(3)
z = float(3)
# get type
print(type(x))
# variable names
my_var = "Byusa"  # Snake Case
MYVAR = "Byusa"  # Pascal Case
myVarName = "BYUSA"  # CamelCase
# Many valiues to multiple variables
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
# output variables
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x, y)
