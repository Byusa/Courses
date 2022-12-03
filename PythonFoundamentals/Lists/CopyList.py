# Copy Lists
# Copy a list, 
# you can not copy list like list1=list2, it will only reference it
fruits_list = ["apple", "banana", "cherry"]
fruits_list_copy = fruits_list.copy()
print(fruits_list_copy)

# Another way is to use a built in method called list
fruits_list = ["apple", "banana", "cherry"]
fruits_list_copy = list(fruits_list)
print(fruits_list_copy)

# or
fruits_list = ["apple", "banana", "cherry"]
my_fruits_copy = fruits_list[:]
print(my_fruits_copy)

