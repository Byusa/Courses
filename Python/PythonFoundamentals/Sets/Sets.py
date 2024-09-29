# Sets
myset = {"apple", "banana", "cherry"} 
# Sets are unordered, unchangeable and unindexed
print(myset)
# Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(myset)

# Get length
print(len(myset))

# Set items - Data Types(String, int, boolean)
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)


# Type()
# <type 'set'>
print(type(set1))

# The set() Constructor
set_const = set(("apple", "banana", "cherry"))
print(set_const)
