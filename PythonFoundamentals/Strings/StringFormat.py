# Format Strings
# you can't concatenate String and numbers
# we use format() and replace place holder with {}
age = 29
txt = "I am {} years old"
print(txt.format(age))
# it take unlimited number of args
amount = 1000000
new_age = 30
txt = "I am {} years old, I want to have a ${}USD before I turn {}"
print(txt.format(age, amount, new_age))

# you can use indeces to make sure they are placed corectly
txt = "I am {2} years old, I want to have a ${0}USD before I turn {1}"
print(txt.format(amount,  new_age, age))
