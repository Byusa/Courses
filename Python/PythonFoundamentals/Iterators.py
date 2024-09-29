# Iterator
# Iterato vs Iterable
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

print("With Strings")


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through iterator
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

# StopIteration
class MyNumbers:
    def __iter__(self):
        self.a =1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a =+1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)