# Unpacking a tuple 
# packing tuple = creating and assiging a tuple
# Packing a tuple
fruits = ("apple", "banana", "cherry")

# We can also extract values back into variables (unpakcing)
(x, y, z) = fruits
print(x)
print(y)
print(z)

# Using Asterisk *
# if the number of variables is less than the number of values, 
# we use *(infront) and that assigns to list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(x, y, *z) = fruits
print(x)
print(y)
print(z) # this becomes the list

#  Add * to a vriable name other than the first or last
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(x, *y, z) = fruits
print(x) # apple
print(y) # ["mango", "papaya", "pineapple"]
print(z) # cherry