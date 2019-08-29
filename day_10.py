#-------- DAY 10 "operators 1" --------
print("Lesson 10: Operators 1")
text = """Python has 7 groups of operators used to perform operations on variables and values.
In this lesson, we will talk about some of them:
1- Arithmetic operators.
2- Assignment operators.
3- Comparison operators."""
print(text + "\n---------------------")
a, b, c, d, e, f = 5, 3, 23, -2.3, 7.5, 15
example1 = """Arithmetic operators
a. Addition: {4} + {2} = {6}          b. Subtraction: {3} - {5} = {7}
c. Multiplication: {0} * {1} = {8}         d. Division: {5} / {0} = {9}
e. Modulus: {2} % {1} = {10}                f. Exponentiation: {0} ** {1} = {11}
g. Floor division: {2} // {0} = {12}"""
#-------- Here we talk about another group which is Bitwise Operators --------
# a. And: a = 5        #00101
#         c = 23       #10111
#         a & c = 5    #00101
# ----------------------------------
# b. Or: a = 5         #00101
#        c = 23        #10111
#        a | c = 23    #10111
# ----------------------------------
# c. Xor: a = 5        #00101
#         c = 23       #10111
#         a ^ c = 18   #10010
# ----------------------------------
# d. Right-shift: b = 3
#                 c = 23       #10111
#                 c >> b = 2   #00010
# ----------------------------------
# e. Left-shift: b = 3
#                c = 23        #10111
#                c << b = 184  #10111000
example2 = """Assignment operators
As we always use it to assign values to variables BUT here with another operators
*** NOTE: the value of a is {1} and c is {0} ***
a += {0} is the same as a = a + {0}, so the output is: a = {7}
a &= {0}, the output is: a = {2}          a |= {0}, the output is: a = {5}
a ^= {0}, the output is: a = {3}         c >>= {8}, the output is: c = {6}
c <<= {8}, the output is: c = {4}"""
example3 = """Comparison operators
They return True or False values
a. Equal: {0} == {1}  {2}
b. Not equal: {0} != {1}  {3}
c. Greater than: {1} > {0}  {4}
d. Less than: {1} < {0}  {5}
e. Greater than or equal to: {0} >= {1}  {6}
f. Less than or equal to: {0} <= {1}  {7}"""
print(example1.format(a, b, c, d, e, f, e+c, d-f, a*b, f/a, c%b, a**b, c//a))
print("\n\n" + example2.format(c, a, a&c, a^c, c<<b, a|c, c>>b, a+c, b))
print("\n\n" + example3.format(d, e, d==e, d!=e, e>d, e<d, d>=e, d<=e))
