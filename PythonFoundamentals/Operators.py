# # Operators

# # 1) Arithmetic Operators
# x = 3
# y = 2
# # Exponentiation
# print(x ** y) # 3^2
# # the floor division // rounds the result
# # down to the nearest whole number
# x = 17
# y = 3

# print(x // y) #math floor(17/3)

# # 2) Assignment Operators

# # =	x = 5	x = 5	
# # +=	x += 3	x = x + 3	
# # -=	x -= 3	x = x - 3	
# # *=	x *= 3	x = x * 3	
# # /=	x /= 3	x = x / 3	
# # %=	x %= 3	x = x % 3	
# # //=	x //= 3	x = x // 3	

# # **=	x **= 3	x = x ** 3	Exponent assign operator
# print("exponent", 5**3)
# # &=	x &= 3	x = x & 3	
# x = 17
# x = x & 3
# print("AND", x)
# # |=	x |= 3	x = x | 3	Bitwise OR operator
# a = 5
# b = 10
# a |= b
# print ("OR", a) # a || b = a OR b 
# # ^=	x ^= 3	x = x ^ 3   Bitwise XOR operator
# a = 5
# b = 9
# a ^= b
# print ("XOR", a) # 1001 XOR 1001 = 1100 (similar zer0)
# # >>=	x >>= 3	x = x >> 3	right shift operator.
# a = 78
# b = 5
# x = a >> b
# print ("right shift operator", x) # 78/5^2 = 3.12 which is 3
# # <<=	x <<= 3	x = x << 3  left shift operator.
# a = 78
# b = 5
# x = a << b
# print("left shift operator", x) # 78*2^5 = 2496

# # 3)Comparison Operators
# # == , <= , >=, !=, <, >=,

# # 4) Logical Opearators
# # and, or, not

# # 5) Identity Opearators
# # is, is not, 
# print(x is y)
# print(x is not y)

# # 6) Membership Operators
# # in, not in
# print(x in [2,5,6,7])
# print(x not in [2,5,6,7])

# 7) Bitwise Operators
# &(and), |(or), <<(left shift), >>(right shift), ^(XOR),  ~ NOT 

# Exercies
# 1) Reverse bits of a given 32 bits unsigned integer.
# Example 1: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)

def reverseBits(n):
    ret =0
    power = 31
    while n:
        # n%2 = n&1
        # ret = ret +(n%2) *2**power
        ret += (n & 1) << power #  * 2^power
        print(ret)
        # n//2 = floor(n/2) = n>>1
        n = n >> 1 # n//2 = n>>1
        power -= 1
    return ret
    

print(reverseBits(43261596))



