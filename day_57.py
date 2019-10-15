#-------- DAY 57 "regular expressions (regEx)1" --------
import re #Built-in module for RegEx

# You can by RegEx searching a specified pattern from a string & check if it exist or not

print("Lesson 57: Regular Expressions (RegEx) 1")
txt = "This lesson is so important to understand it"
print(txt + "\n---------------------\nWe will do some checking for that statement:")
test1 = re.search("^This.*it$", txt)
if (test1):
    print("  YES! we have a match :)")
    print(' ', re.findall("s", txt)) #Return a list
    print(' ', re.findall("[e-m]", txt)) #Return a list contains a set of characters from e to m
    print(' ', re.split(" ", txt))
    print(' ', re.sub("\s", " -> ", txt, 2)) #Replace first 2 white-spaces
    print(' ', re.findall(r"\bTh", txt))
else:
    print('SORRY :( no match')
