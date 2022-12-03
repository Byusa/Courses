# List comprehension
# with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = []

for fruit in fruits:
    if 'a' in fruit:
        fruits_with_a.append(fruit)
print(fruits_with_a) #['apple', 'banana', 'mango']

# with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = []
[fruits_with_a.append(fruit) for fruit in fruits if 'a' in fruit]
print(fruits_with_a)

# Syntax
# newlist = [expression for item in iterable if condition == True]
# newlist = [x for x in fruits]

# Iterable
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x > 5]
print(newlist)


# Expression
# add maniputate outcome
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ["Hello" for x in fruits]
print(newlist)
newlist = [x if x!="kiwi" else "orange" for x in fruits ]
print(newlist)


