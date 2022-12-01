# Python Numbers
import random
# int
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# float
x = 35e3 #e indicates the power of 10 so (35e3 = 35x(10^3)=35000.0)
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)

# Random number
print(random.randrange(1,10))




