# For loop
for x in "banana":
  print(x)

# The Break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# Range function
for x in range(6):
  print(x)

# range(a,b) b not included
for x in range(2, 6):
  print(x)

#  Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)

# Else in for loop
for x in range(6):
    print(x)
else:
    print("Finally Finished")

# Break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# Pass statement
for x in [0, 1, 2]:
  pass