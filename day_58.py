#-------- DAY 58 "regular expressions (regEx)2" --------
import re

print("Lesson 58: Regular Expressions (RegEx) 2")
print('Today we have 3 functions with its examples:\n1. findall():')
str = 'The rain in Spain'
x1 = re.findall('Portugal', str)
if (x1):
    print(' Yes, there is at least one match!')
else:
    print(' No match')
x2 = re.search('\s', str)
print('---------------------\n2. search():\n The first white-space character is located in position:', x2.start())
print('', re.search('Portugal', str))
print('---------------------\n3. split():\n', re.split('\s', str))
