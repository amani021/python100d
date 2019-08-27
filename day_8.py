#-------- DAY 8 "strings 2" --------
title = "Lesson 8: Strings 2"
print(title)
info1 = """ Python has many methods for string, such as:
1. strip()  2. len()  3. lower()  4. upper()  5. replace(,)  6. split() """
print(info1)
print("---------------------\nExamples:")
#Eg. for method number 1 - removes whitespace from beginning & end
print("a-\n" + info1.strip())
#Eg. for method number 2 - returns the length of a string
print("b- " + str(len(info1))) #We used it before in lesson 5 to split a string
#Eg. for method number 3 - returns the string in lower case
print("c- " + title.lower())
#Eg. for method number 4 - returns the string in upper case
print("d- " + title.upper())
#Eg. for method number 5 - replaces a string with another string
print("e- " + title.replace(': ', ' - ') + "\nf- ") #The syntax is: replace('old value', 'new value')
#Eg. for method number 6 - splits the string into substrings according to which you wrote to separate
#And it will return an array
print(title.split(': '))
print(title.split('8:'))
print(title.split('s'))
