# Arrays
# Python does not have built in for array
cars = ["Ford", "Volvo", "BMW"]
print(cars)
# Access array element
x = cars[0]
# modify
cars[0] = "Toyota"
print(cars)

# Lenght of array
x = len(cars)
print(x)

# Looping Array Elements
for x in cars:
  print(x)

# Adding Array Elements
cars.append("Honda")
print(cars)

# Removing array elements
cars.pop(1)
print(cars)
# remove() can also be used to remove array elements
cars.remove("BMW")
print(cars)


# Array Methods
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Python does not have built-in support for Arrays, but Python Lists can be used instead.



# example
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = new int[m][n];
        grid = [[0 for x in range(n)] for y in range(m)]
        print(grid)
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    grid[i][j] = 1 #if it was a straigh line it will be one path
                else:
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[m-1][n-1]

        # (3,7)
        # [
        #   [1, 1, 1, 1,  1,  1,  1], 
        #   [1, 2, 3, 4,  5,  6,  7], 
        #   [1, 3, 6, 10, 15, 21, 28]
        # ]
