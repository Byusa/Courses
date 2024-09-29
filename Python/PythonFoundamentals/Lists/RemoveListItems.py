# Remove List items

# remove(), it removes specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop(), remove at specific index
thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)
thislist.pop() # removes the last item
print(thislist) 

# del keyword also remove specific index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) 
# del can also delete completely 
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) # not defined since it is deleted completely


# clear(), empty a list but list still remains but with no content
this_list = ["apple", "banana", "cherry"]
# this_list.clear()
del this_list[:]
print(this_list) 



