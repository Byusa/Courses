# Copy a dictionary
# copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
copy_dict = thisdict.copy()
print(copy_dict)
# dict()
copy_dict_fn = dict(thisdict)
print(copy_dict_fn)