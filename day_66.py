#-------- DAY 66 "string formatting2" --------
print("Lesson 66: String Formatting 2")
# From lesson 9
# 1- a.format(x), has one argument.
#     In the text you will write like this: a = 'I love number {}'
# 2- a.format(x, y), has two or more arguments.
#     In the text you can write one of these:
#     1. a = 'I love number {} and {}{}'
#     2. a = 'I love number {1} and {1}{0}', with index to use it more than one!!
'''
Other ways to use - completing lesson 9:
3- If you want numbers with decimal point, you will write like this: a = 'The bag price is {:.2f}'
    This will be a number with two decimals.
4- Named indexes instead of index numbers.
'''
txt = 'The price of this {thing} is {price:.2f} dollars'
print(txt.format(thing = "bag", price = 56))
