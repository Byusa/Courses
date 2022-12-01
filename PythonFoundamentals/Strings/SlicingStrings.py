# Slicing 

# Returns a range of characters 
b = "Hello, World!"
# Slice from 2 to 5(not included)
print(b[2:5]) #llo (2,3,4)

# Slice from start
print(b[:5]) #Hello

# Slice to the end
print(b[2:]) #llo, World!

#Negative Indexing (starts from behind) 
print(b[-2:]) #d!
print(b[:-2]) #Hello, Worl
print(b[-5:-2]) #orl