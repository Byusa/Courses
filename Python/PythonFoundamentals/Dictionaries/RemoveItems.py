# Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.pop("model"))
print(thisdict)

# popitem() = removes the last items in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.popitem())
print(thisdict)

# del = removes the item with specified key name
thisdict = {
  "id":1,
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
del thisdict["year"]
print(thisdict)

# del = also deletes the dictionary completely 
thisdict = {
  "id":1,
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
del thisdict
print("After deleting the dictionary")
# print(thisdict) # it won't exist

# clear() empties the dictionary
thisdict = {
  "id":1,
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
thisdict.clear()
print(thisdict)

