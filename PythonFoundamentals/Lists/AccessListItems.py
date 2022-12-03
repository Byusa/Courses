# Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing (Means that you start from the end)
print(thislist[-1]) # cherry

# Range of indexes (from start to last but not including the last one)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # ["cherry", "orange", "kiwi"]

print(thislist[:4]) # ["apple", "banana", "cherry", "orange"] (its like [0:4])
print(thislist[2:]) # ["cherry", "orange", "kiwi", "melon", "mango"] (its like [2:lastitem])

# Range of Negative indexes
print(thislist[-4:-1]) #["orange", "kiwi", "melon"]

# Check if Item exists 
if "apple" in thislist:
    print("apple exists")