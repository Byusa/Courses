# https://www.w3schools.com/python/python_datatypes.asp
# Python datatypes built-in by default, these categories

# Text Type: # str: 
x = "Hello World"
print(type(x))
# Numeric Types: int, float, complex
x = 5 
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
# Sequence Types: list, tuple, range
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = range(6)
print(x) # range(0, 6)
print(type(x)) # <class 'range'>
# Mapping Types: dict
x = {"name" : "John", "age" : 36}
print(type(x))
# Set Types: set, frozenSet
x = {"apple", "banana", "cherry"}	
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
# Boolean Type: bool
x = True
print(type(x))
# Binary Types: bytes, bytearray, memoryview
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
# None Type: NoneType
x = None	
print(type(x))