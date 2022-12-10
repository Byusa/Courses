# Loop through Dictionary
print("Print all all Keys, one by one")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# print all all values, one by one
print("Print all all values, one by one")
for x in thisdict:
  print(thisdict[x])  

# values() = returns values
print("also Print all all values, one by one")
for x in thisdict.values():
    print(x)

# keys() = returns keys
print("Print the Keys")
for x in thisdict.keys():
    print(x)

# print both keys and values
print("Both values and keys")
for k,v in thisdict.items():
    print(k,v)



