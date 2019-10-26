#-------- DAY 67 "exercise" --------
# 1. Enter the first & last letter of a name
fLetter = input('Enter the first letter of your name: ')
lLetter = input('Enter the last letter of your name: ')
print("\nHi dear :)\nYour name starts with '", fLetter, "' letter and ends with '", lLetter, "' letter")
# 2. String formatting
txt = "Dear {name}, Your current balance is {price:.2f} $"
print('\n---------------------\n\n', txt.format(name = 'Ahmad Ali', price = 53.4408))
