# Join two sets of
# union() = combines items in both sets 
# update() = inserts items from one set to the other

# union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # any duplicates will delt with 
print(set3)

# update()    
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Keep only the duplicates 
# intersection_update() = list present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# intersection ()= return set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# Keep all but not Duplicates
# symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# symmetric_difference() = retuns a set of differences 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)