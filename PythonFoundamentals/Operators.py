# Operators

# 1) Arithmetic Operators
x = 3
y = 2
# Exponentiation
print(x ** y) # 3^2
# the floor division // rounds the result
# down to the nearest whole number
x = 17
y = 3

print(x // y) #math floor(17/3)

# 2) Assignment Operators

# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	

# **=	x **= 3	x = x ** 3	Exponent assign operator
print("exponent", 5**3)
# &=	x &= 3	x = x & 3	
x = 17
x = x & 3
print("AND", x)
# |=	x |= 3	x = x | 3	Bitwise OR operator
a = 5
b = 10
a |= b
print ("OR", a) # a || b = a OR b 
# ^=	x ^= 3	x = x ^ 3   Bitwise XOR operator
a = 5
b = 9
a ^= b
print ("XOR", a) # 1001 XOR 1001 = 1100 (similar zer0)
# >>=	x >>= 3	x = x >> 3	right shift operator.
a = 78
b = 5
x = a >> b
print ("right shift operator", x) # 78/5^2 = 3.12 which is 3
# <<=	x <<= 3	x = x << 3  left shift operator.
a = 78
b = 5
x = a << b
print("left shift operator", x) # 78*2^5 = 2496

# 3)Comparison Operators
# == , <= , >=, !=, <, >=,

# 4) Logical Opearators
# and, or, not

# 5) Identity Opearators
# is, is not, 
print(x is y)
print(x is not y)

# 6) Membership Operators
# in, not in
print(x in [2,5,6,7])
print(x not in [2,5,6,7])

# 7) Bitwise Operators
# &(and), |(or), <<(left shift), >>(right shift), ^(XOR),  ~ NOT 


