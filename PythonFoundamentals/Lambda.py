# Python Lambda
# A lamda function is a small annonymous function
# A lamda function can take any number arguments but can only have one expression

# syntax
#  lambda arguments : expression

# The expression is excuted and the reislt is returned
x = lambda a : a + 10 # add 10 to a and return the results
print(x(5))

# Lambda function can take any number of arguments
x = lambda a, b : a * b
print(x(5,6))

x = lambda a,b ,c : a + b + c
print(x(5,6,2))


# Why use lambda function?
# The power of lambda function is used when it use anonymous function inside
# another function

# eg: function that takes one argument and multiplied with an unknown number
def myfunc(n):
    return lambda a : a* n
# eg we can create one that can always double
mydoubler = myfunc(2)
print(mydoubler(11))
# we can create one that can always triples
mytripler = myfunc(3)
print(mytripler(11))

# sort a 2d list by first value
my_list = [[0,30],[5,10],[15,20]]
# my_list.sort(key=lambda x: x[0])
# sort a 2d list by first value if the first value is the same sort by the second value
my_list2 = [[9,10], [4,9], [4,17]]
my_list2.sort(key=lambda x: (x[0], x[1]))
print(my_list2)


# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:
#  my_list2 = [[9,10], [4,9], [4,17]]
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

