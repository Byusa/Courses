
# How will you test if a high-order bit is set in a byte.
def is_bit_set(byteval,idx):
    return ((byteval&(1<<idx))!=0)

print(is_bit_set(4,2)) # True
# 4 = 0100, in bytes = 00000100
# at index 2, the index is 1, so it is true
# bit are read from left to right
# hex are read from right to left

my_dict = [ { 
    "first_name": "Michael", 
    "last_name": "Jordan" ,
    "age": 33
    }, { 
    "first_name": "Elsa", 
    "last_name": "Emilien" ,
    "age": 10
    }
]

# sort by age
my_dict.sort(key=lambda x: x['age'])


# draw a christmas tree with print statements with n levels
def draw_tree(n):
    for x in range(n):
        print(" "*(n-x-1) + "*"*(2*x+1) + " "*(n-x-1))

draw_tree(4)


# create a linkedlist in python 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# reverse a linkedlist
def reverse(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

# insert a node between the first and second node
def insert_between(first, second, data):
    new_node = Node(data)
    first.next = new_node
    new_node.next = second

# Determine if a linkedlist is circular
def is_circular(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# add the end of a linkedlist
def add_end(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
    return head


# add the beginning of a linkedlist
def add_infront(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head




# find the middle of a linkedlist
def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


# find the nth node from the end of a linkedlist
def find_nth_from_end(head, n):
    slow = head
    fast = head
    for i in range(n):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


# find the intersection of two linkedlists
def find_intersection(head1, head2):
    len1 = 0
    len2 = 0
    current = head1
    while current is not None:
        len1 += 1
        current = current.next
    current = head2
    while current is not None:
        len2 += 1
        current = current.next
    if len1 > len2:
        for i in range(len1-len2):
            head1 = head1.next
    else:
        for i in range(len2-len1):
            head2 = head2.next
    while head1 is not None and head2 is not None:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

# find the length of a linkedlist
def find_length(head):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length



# convert hex to integer
def hex_to_int(hex):
    return int(hex, 16)

print(hex_to_int("0F81"))

# convert hex to int
def hex_to_hex(numb):
    return hex(numb)

print(hex_to_hex(0x0F81))

# OOP
# hex
# Recursion
# DFS