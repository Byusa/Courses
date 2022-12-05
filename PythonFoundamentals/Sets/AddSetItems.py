# Add to a set 
# add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add sets
# update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add any iterable 
# You can add (tuples, list, dictionary) using update
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

