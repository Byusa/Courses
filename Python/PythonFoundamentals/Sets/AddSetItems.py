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

thisset2 = {"apple", "banana", "cherry"}
myDict = {"name": "Serge", "age":29, "Profession":"Software Engineer"}
thisset2.update(myDict)
print(thisset2)
thisset2 = {"apple", "banana", "cherry"}
# myList = [
# 	{"name": "Serge", "age":29, "Profession":"Software Engineer"},
#     {"name": "Beza", "age":24, "Profession":"Nurse"},
#     {"name": "Taha", "age":23, "Profession":"Software Engineer"}
	
# ]
# thisset2.update(myList)
# print(thisset2)