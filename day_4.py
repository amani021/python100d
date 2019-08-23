#-------- DAY 4 "numbers" --------
import random

print("Lesson 4: Numbers")
print("1- There are 3 types:\n1- Int   2- Float    3- Complex")
print("\n2- To know the type of number using type() function, such as:\na, b, c, d = -6543, 23.5, 46e3, 1+3j")
a, b, c, d = -6543, 23.5, 46e3, 3j #Assign value to variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("\n3- You can convert from int or float to other types BUT you can't convert the complix type to another one")
#Convert the type inside print function
print(float(a)) #From int to float
print(complex(b)) #From float to complex
print(int(c)) #From float to int
print("\n4- Python has a built-in module called 'random' to make random numbers")
print(random.randrange(0, 10))
