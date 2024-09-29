# sort list, sort()
# Sort list alphanumericallly 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# sort descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# Customise Sort Functions 
# Sort the list based on how close the number is to 50:

def closeTo50(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = closeTo50)
print(thislist)

# case insensitve sort order
# All Capital letters are sorted before the lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# When case-sensitve we use lower() to sort 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Reverse Order
thislist = [100, 50, 65, 82, 23]
thislist.reverse()
print(thislist)

