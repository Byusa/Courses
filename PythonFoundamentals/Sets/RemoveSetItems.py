#  Remove Set
# remove() and discard() methods

# remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# thisset.remove("him")  #this will throw an exemption

# discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset.discard("water") # if the element is not there won't throw exceptions
print(thisset)

# pop(), you can also use pop but removes the last element 
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # prints the last element
print(thisset)
# sets are unordered when you use pop, you don't know which one is removed

# clear(), empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del, deletes the set
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) #already deleted
