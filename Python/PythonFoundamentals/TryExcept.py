# Try ... Except
# Try block = lets you try 
# except block =lets you handle the error 
# else block = lets you excute the code when there is no error
# Finally block = lets you excutes regardless the Results

# Exception Handling
try:
    print(x)
except:
    print("Exception occurred")

# Many Exceptions
try:
    print(x)
except NameError:
    print("variable x is not defined")
except Exception:
    print("Something else went wrong")

# Else
try:
    print("Hey")
except:
    print("Exception occurred")
else:
    print("Nothing went wrong")


# Finally
try:
    print(x)
except:
    print("Exception occurred")
finally:
    print("The 'try except' is finished")

# This can be usefuul to close object and clean up resoursec
try:
    f = open("demofile.txt")
    try:
        f.write("Hi")
    except:
        print("Something went wrong in writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong in openning the file")

# Raise an exception
# Raise an error and stop the program if x is lower than 0
# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if x is not an integer
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")