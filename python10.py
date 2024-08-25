"""
#
# Part : Python Json
# API = Application Programming Interface
#
"""

import json

# make a json (Dictionary string)
x = '{"name": "john", "age 20", "city": "Phuket"}'
print(x)
#parse

y = json.loads(x)

#python dictionary
print(y)
print(type(y))
print(y["city"])

# Python dictionary
a = {
    "name": "Noa",
    "age": 20,
    "city": "Phuket"
}

#convert to Json
b = json.dumps(a)

#json String
print(b)
