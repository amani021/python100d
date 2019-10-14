#-------- DAY 56 "json2" --------
import json

print("Lesson 56: JSON 2")
# You can format a JSON string better than previous Lesson to be readable
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
# The syntax & meaning of each parameter of dumps() method is:
#     a. indent: define the numbers of indents
#     b. separators('value to separate each object', 'value to separate keys from values')
#     c. sort_keys: to be the result in order based on keys
print('You can read better now ^^\n', json.dumps(k, indent=2, separators=('', ' = '), sort_keys=True))
