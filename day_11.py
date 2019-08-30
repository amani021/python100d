#-------- DAY 11 "operators 2" --------
print("Lesson 11: Operators 2")
text = """Today we will complete the groups of operators talking on previous lesson, which are:
4- Logical operators.
5- Identity operators.
6- Membership operators.
7- Bitwise operators.
*** NOTE: the point number 4, 5 & 6 return True or False values!! ***"""
print(text + "\n---------------------")
x, y, z = 5, 8, 13
a, b, c = ['red', 'blue', 'purple'], [45, 13, 53], ['people', 34]
example4 = """Logical operators
Combine conditional statements.
*** NOTE: the value of x is {0} and y is {1} ***
a. and: y < {2} and y > {0}  {3}            b. or: x < {1} or x > {2}  {4}
             c. not: not(y < {2} and y > {0})  {5}"""
example5 = """Identity operators
Compare two objects if they are in the same memory location or not.
a. is: {1} is {0}  {2}
b. is not: {0} is not {1}  {3}"""
example6 = """Membership operators
Test if an element or a sequence exists in an object or not.
a. in: {0} in {2}  {4}
b. not in: {1} not in {3}  {5}"""
# f. NOT: z = 13        #0000 1101
#       ~ z = -14       #1111 0010
# 14 is 0000 1110
# Its one's complement is: 1111 0001
# And the two's complement is: 1111 0001
#                             +        1
#                             -----------
#                              1111 0010 --> -14
example7 = """Bitwise operators
We talked about it in the previous lesson EXCEPT:
NOT: inverts all the bits, for example: ~ {} and the output will be {}"""
print(example4.format(x, y, z, y<z and y>x, x<y or x>z, not(y<z and y>x)))
print("\n" + example5.format(b, c, c is b, b is not c))
print("\n" + example6.format(a[1], y, a, b, a[1] in a, y not in b))
print("\n" + example7.format(z, ~ z))
