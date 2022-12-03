# Join two lists

# easiest way is +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x) # O(1)
print(list1)

# we can use extend 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) # O(k), k = len(list2)
print(list1)


