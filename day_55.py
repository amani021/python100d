#-------- DAY 55 "json1" --------
# 1. Convert from JSON string to python object using loads() method
# 2. Convert from python object to JSON string using dumps() method
import json

print("Lesson 55: JSON 1")
#Some JSON string
x = '{"name":"Amani", "age":22, "city":"Makkah"}'
#Parse x
y = json.loads(x)
print('I love & I live in', y["city"])
#A python object (dictionary)
x = {"name":"Amani", "age":22, "city":"Makkah"}
k = {
    'name': 'Amani',
    'age': 22,
    'programming': True,
    'engineering': False,
    'account': ('facebook', 'twitter'),
    'pets': None,
    'sis': [
        {'name':'Amal', 'age':14},
        {'name':'Hiba', 'age':8}
    ]
}
#Convert into JSON
y = json.dumps(x)
l = json.dumps(k)
print('---------------------\nThis is a JSON string:', y)
print('And look the differnces here:\n', l)
