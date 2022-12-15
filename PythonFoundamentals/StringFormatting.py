# Python String Formatting

# String format()
# format() allows you to format selected parts of the string 
# add placholders {} and run values in format() 
# Example: 
price = 500
txt = "The price is {} dollars"
print(txt.format(price))
# You can parameters to convert the value 
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
price = 500
itemno = 134
count = 5
txt = "I want {} pieces of item number {} for {:.2f} dollars"
print(txt.format(count, itemno, price))

# Index Numbers
# you can use indeces to make sure that values are placed in the correct order
txt = "I want {1} pieces of item number {2} for {0:.2f} dollars"
print(txt.format(price, count, itemno ))

# You can refer the same varaible more than once
name="Byusa"
age=29
txt="His name is {1}. {1} is {0} years old"
print(txt.format(age,name))

# Named Indexes
# {carname} and access as format(carname="Range Rover")
txt= "I have a {carname}, that is {color}"
print(txt.format(carname="Range Rover", color="Grey"))



