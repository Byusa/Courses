# Boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#A) Most Values are True
# Any string is true except empty Strings
print(bool("abc"))
# Any number is true except 0
print(bool(123))
# Any list, tuple, set, and dictionary are true, except empty ones
print(bool(["apple", "cherry", "banana"]))

#B) Some values are False 
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# value or obj evaluate False, if have obj from class __len__() fnc that return 0 or Flase:
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))


# C) Functions can return a boolean value
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("Yes")
else:
    print("No")

# built in functions
x = 200
print(isinstance(x,int))