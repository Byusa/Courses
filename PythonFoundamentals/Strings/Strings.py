# Multiline Strings
a = """Assigning a string to a variable is done with the variable 
name followed by an equal sign and the string;
You can assign a multiline string to a variable 
by using three quotes"""
# print(a)
# Strings are arrays 
a = "Hello, World!" #Python does not have char
print(a[1])
#Loop Through a string 
for x in "banana":
    print(x)

# len of string
for c in range(len(a)):
    print(a[c])

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# if
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if not
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")