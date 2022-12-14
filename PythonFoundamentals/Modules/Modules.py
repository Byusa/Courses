# Python Modules
# A module is same as code libray
# A file containing a set of functions you want to include in your application
import MyModule
MyModule.greeting("Serge")
# Syntax
# module_name.function_name
name = MyModule.person1["name"]
print(name)

# renaming a module
import MyModule as dictModule
age = dictModule.person1["age"]
print(age)

# Built in Modules
import platform
x = platform.system()
print(x)

# Using the dir() Function
# Print all functions and variables of modules
import platform
x = dir(platform)
# print(x)

import MyModule
all_functions_variables = dir(MyModule)
print(all_functions_variables)


# Import from Module
from MyModule import person1
print(person1["age"])
# do not do this MyModule.person1["age"] when you use From