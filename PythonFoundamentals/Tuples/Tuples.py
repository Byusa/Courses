# Access Typles
mytuple = ("apple", "banana", "cherry")
# They are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable
print(mytuple)
# A tuple items are ordered and unchangeable, allow duplicate values
# Ordered, items in a order that won't change 
# Unchangeable, we cannot change, add or remove after being created

# tuple length
print(len(mytuple))

# Create tuple with one item
# You have to add ,
mytuple = ("apple",)
print(type(mytuple))
not_my_tuple = ("apple") #This becomes a string
print(type(not_my_tuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
print(type(tuple1))
tuple2 = (1, 5, 7, 9, 3)
print(type(tuple2))
tuple3 = (True, False, False)
print(type(tuple3))

# Tuple can contain different data types 
tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))

# The tuple () Constructor
tuple = tuple(("apple", "banana", "cherry"))
print(tuple)





