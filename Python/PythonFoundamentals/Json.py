# JSON
import json
# Parse JSON - Convert JSON to Python
# json.loads() = the result will be python dictionary

# eg
# Some JSON
x = '{ "name" : "Byusa", "age": 29, "Country":"Canada"}'
y = json.loads(x)
print(y)
print(y["age"])

# Convert from Python to JSON
a = { 
    "name" : "Byusa", 
    "age": 29, 
    "Country":"Canada"
    }
b = json.dumps(a)
print(b)
# you can convert the following types into JSON
# dict, list, tuple, string, int, float, True, False, None
# eg:
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Python ====> Json(javascript)
# Python ====> 	JSON
# dict	====> Object
# list	====> Array
# tuple	====> Array
# str	====> String
# int	====> Number
# float	====> Number
# True	====> true
# False	====> false
# None	====> null


# from python to JSON
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Format the Result
# json.dumps has methods that helps us to read the results
print(json.dumps(x, indent=4))
# Separators
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# order the results
# sort_keys
print(json.dumps(x, indent=4, sort_keys=True))
