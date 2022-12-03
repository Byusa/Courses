# Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop through the index numbers (range and len)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# While loop 
thislist = ["apple", "banana", "cherry"]
i = 0
while(i<len(thislist)):
    print(thislist[i])
    i+=1

# Looping using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]