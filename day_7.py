#-------- DAY 7 "strings 1" --------
#Eg. for point number 2
print("Lesson 7: Strings 1")
#Eg. for point number 4 (use single quotation)
x = '''As we learned beginning, here in this lesson,
we will talk some of those informations as a confirmation for us'''
print(x)
#Eg. for point number 3 & 1 (use single quotation)
note = '*** NOTE: the point number 4 and 5 are new infos!! ***'
print(note)
#Eg. for point number 4 (use double quotation)
info = """1- Write string between two single (' ') or double (" ") quotation.
2- To display something as an output on the screen, using print() function.
3- The syntax for assign string to a variable is: Variable = "Any words you want to write"
4- To write multiline strings, use three single (''') or double (\""") quotation.
5- Strings are arrays, storing into memory as character by character and you can access it using []. *** NOTE: the first character has the position 0 ***
6- And to return a part of string, using this syntax: [start index : end index will not included]"""
print(info)
print("---------------------\nFor example:")
#Eg. for point number 5
print(x[22])
#Eg. for point number 6
print(note[4:8])
