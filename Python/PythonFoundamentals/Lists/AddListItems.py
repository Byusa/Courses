# Add List Items
# append()
this_list = ["apple", "banana", "cherry"]
this_list.append("Orange")
print(this_list)

# Insert items into list
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
# you can extend a list to a tuple, sets, dictionary etc ...
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
this_dict = {"name": "Serge", "Age":29}
thislist.append(this_dict)
print(thislist)
