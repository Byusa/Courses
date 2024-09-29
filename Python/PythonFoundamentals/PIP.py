# PIP 
# PIP is a package manager for python packages, or modules if you like.
# It is included in python3.4 by default
# comes in Python 3.4 by default    

# Package = contains all the files you need for a module 
# Check if PIP is installed 
# Pip --version
# Pip3 --version

# pip install camelCase

# Using a Package
# now camelCase is installed we can use it to
import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

# Find Packages
# https://pypi.org/

# Remove a Package
# pip unistall camelcase 


# List packages
# pip list
