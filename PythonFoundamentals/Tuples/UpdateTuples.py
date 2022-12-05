# Change tuple Values
# Tuples are unchangeable or immutable
# To change it, convert it into a list and change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x=tuple(y)

print(x)

# Add, (to list then append)
x = ("apple", "banana", "cherry")
y = list(x)
y.append("kiwi")
x=tuple(y)
print(x)

# add tuple to tuple  
x = ("apple", "banana", "cherry")
y = ("kiwi",)
x+=y
print(x)

# Remove from a tuple (use list)
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("banana")
x = tuple(y)
print(x)

# delete in tuple (use list)
# del can complete delete a tuple 
x = ("apple", "banana", "cherry")
del x
# print(x) # Raises an error because the tuple no longer exists.