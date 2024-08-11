"""
#
# Part : Python Comment
#
"""

#this is a comment
# v = s/t
# v = ความเร็ว (m/s)
# S = ระยะทาง (m)
# t = เวลา (s)

"""
this is a comment
v = s/t
v = ความเร็ว (m/s)
S = ระยะทาง (m)
t = เวลา (s)
"""

from typing import Type


print("Hello Word!!!")

"""
#
#Part : Python Variables
#
"""
x = 5 # Integer
y = "Hey bro!!!" # String
print(x,y)

x = str( 3)
y = int (5)
z = float(7)
print(type(x), type(y), type(z))


"""
#
#Part : Python Variables Name
#
"""
myvar = "Tony"
my_var = "Tony"
_my_var = "Tony"
myVar = "Tony"
MYVAR = "Tony"
MY_VAR = "Tony"
my_var2 = "Tony"
#2my_var = "Tony"
#my-var = "Tony"
#my var = "Tony"

#Camal Case
myVariableName = "Tony"
#Pascal Case
myVariableName = "Tony"
#Snake Case
my_variable_name = "Tony"

"""
#
#Part : Python String
#
"""
x = "Hey bro!!!"
print(x)

y = """ 
1 Hey bro!!!
2 Hey bro!!!
3 Hey bro!!!
""" 
print(y)
x = "Hey bro!!!"
print(x[2])
print(len(x))
print("Hey"in x)
print("What 'sup" not in x)
print(x.upper())
print(x.lower())

print(x.replace("bro", "sis"))
print(x.split(" "))

a = "apple"
b = "company"
print(a + " " + b)

price = 20
word = f"Price: {price:.2f}"
print(word)