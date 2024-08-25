"""
#
# Part : Python Try Except
#
"""
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
    print(x)
except NameError as e:
    print("Not defined : ", e)
except Exception as e:
    print("Something else went wrong!", e)
    
try:
    print("Hello World")
except :
    print("Something else went wrong!")
else :
    print("Nothing else went wrong!")
    
try:
    print(x)
except :
    print("Something else went wrong!")
finally :
    print("Finished!!!")

#x = -1
#if x < 10:
#   raise Exception("Sorry, number below zero")

x = "Hello"
if not (type(x) is int):
    raise TypeError("Only integers are allowed")