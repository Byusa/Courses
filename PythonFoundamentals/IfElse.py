# if ...else
a = 33
b = 200
if b > a:
    print("b is greater")
elif a > b:
    print("a is greater")
else:
    print("They are equal")

# Short Hand if
if a > b: print("a  is greater")

# Short Hand if ... Else
print("A is greater") if a > b else print("B  is greater")

# 3 Statements
a = 300
b = 300
print("A") if a>b else print("b") if b>a else print("=")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Pass statemenent
a = 33
b = 200

if b > a:
    pass # in case you have nothing to put there cause if can't stay alone

