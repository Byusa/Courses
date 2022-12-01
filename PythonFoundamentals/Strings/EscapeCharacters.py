# Escape Character
# we use \ to add quatation in a string
txt = "John said: \"I am tired\" "
print(txt)
txt = 'It\'s alright.' #Single Quote
print(txt) 
txt = "This will insert one \\ (backslash)." #Backslash
print(txt) 
txt = "Hello\nWorld!" #New Line
print(txt) 
txt = "Hello\rWorld!" #Carriage Return
print(txt) 
txt = "Hello\tWorld!" #Tab
print(txt) 
#This example erases one character (backspace):
txt = "Hello \bWorld!" #Backspace
print(txt) 
# \f	Form Feed
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157" #Octal Value
print(txt) 
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f" #Hex value
print(txt) 