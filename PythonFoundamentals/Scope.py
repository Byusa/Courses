# Scope
# Local Scope 
def myfunc():
  x = 300
  print(x)

myfunc()

# Function inside funciton
def myfunc():
    x = 400
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

# Global function
x=500

def myfunc():
  print(x)

myfunc()

print(x)

# Naming variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# Global Keyword
# make variable global
b = 800

def myfunc():
  global b
  b = 900

myfunc()

print(b)