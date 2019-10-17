#-------- DAY 59 "regular expressions (regEx)3" --------
import re

print("Lesson 59: Regular Expressions (RegEx) 3")
print('Another examples for today:')
str = 'The rain in Spain'
print('', re.sub('\s', '::', str, 3))

# Match object & its methods
print('', re.search('in', str))
x = re.search(r"\bS\w+", str) #Search for an upper case 'S' character in the beginning of a word
print('', x.span()) #Print word's position
print('', x.string) #Return the search string
print('', x.group()) #Print the word if there is no match it will return 'None'
