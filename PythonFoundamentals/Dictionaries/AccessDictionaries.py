# Accessing items
# refer to the key name in the square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["brand"]
print(x)
# we can also use get
x = thisdict.get("brand")
print(x)

# keys() = will return a list of keys
x = thisdict.keys()
print(x)

# update dict and check list of keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
thisdict["make"] = "some make"

x = thisdict.keys()
print(x)

# get values
# values()

x = thisdict.values()
print(x)

# items() = Get Items
x = thisdict.items()
print(x)

# Check if key is in dictionary
if "make" in thisdict:
  print("yes, it is")

# getting the first key 
my_dict = {1:"Water", 2:"Alcohol", 3:"beer"}
keys  = list(my_dict.keys())
print(keys)
first_key = list(my_dict.keys())[0]
print(first_key)
last_key = list(my_dict.keys())[-1]
print(last_key)





