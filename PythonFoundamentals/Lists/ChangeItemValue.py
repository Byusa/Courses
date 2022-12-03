# Change Item Value
this_list = ["apple", "banana", "cherry"]
this_list[1] = "Avocado"
print(this_list)

# Change the range of item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) #["apple","blackcurrant", "watermelon", "orange", "kiwi", "mango"]

# Insert more items (items moves accordingly)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #["apple", "blackcurrant", "watermelon", "cherry"]

# Insert less items 
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ["apple", "watermelon"]

# Insert Items 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"Watermellon" )
print(thislist) # ["apple", "banana", "Watermellon", "cherry"]
