# Heaps
# https://www.tutorialspoint.com/python_data_structure/python_heaps.htm
# Min_Heap = Parent node <= child node.
# Max_heap = Parent node >= child node.
# So useful in priority Queue
# Heapify = convert regular list to heap (smallest element is pushed to the top)
# heappush = add element to the heap
#  heappop = returns the smallest data from heap
# heapreplace = replaces the smallest with new value

# creating a heap
import heapq

H = [21, 1, 45, 78, 3, 5]
heapq.heapify(H)  # puts the smallest element to the top
print(H)

# insert into a heap
heapq.heappush(H, 8)
print(H)  # put 8 at the end

# Removing from heap
heapq.heappop(H)
print(H)  # removes the top most element

# Replacing in a Heap
heapq.heapreplace(H, 6)
print(H)  # replaces the top(smallest) most element and the heap replaces with new one


