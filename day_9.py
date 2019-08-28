#-------- DAY 9 "string format" --------
a, b, c, d = 9, 34, 4, "Lesson {}: String Format"
print(d.format(a))
text = """In this lesson, you can concatenate or combine strings with numbers through format() method!
Previously, when we did like this: print("My age is: " + {1}), it will be an error!!
Then, we solved that error by using str() method to change from a type to string type
    print("My age is: " + str({0})) and this will be right
And now, I think format() method is the easiest way :D"""
'''
It has 2 ways to use:
1- a.format(x), has one argument.
    In the text you will write like this: a = 'I love number {}'
2- a.format(x, y), has two or more arguments.
    In the text you can write one of these:
    1. a = 'I love number {} and {}{}'
    2. a = 'I love number {1} and {1}{0}', with index to use it more than one!!
'''
print(text.format(c, b))
#Eg. of lesson 3
# print("My age is: " + 5) #It will be an error
#Eg. of lesson 6
# print("My age is: " + str(5)) #It will be right
