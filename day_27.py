#-------- DAY 27 "conditional statements (if...else)" --------
print("Lesson 27: Conditional Statements (if...else)\n---------------------\nExample:")
num1, num2, num3 = (12/2)*3, 5*6, 18
# 1- if elif else, nested if
if num1 > num2 or num1 == num2:
    print('This is true :)')
elif num2 != num3 and num2 > num3:
    # 2- One line if else statement: if (if keyword) & else has one statement
    print(num1, ' is greater than ', num2) if num1 > num2 else print(num1, ' is less than ', num2)
else:
    print('All statements are wrong!!')
# 3- One line if else statement, with 3 conditions:
print(num1) if num1 > num3 else print(num1, '=', num3) if num1 == num3 else print(num3)
#It's the same as:
# if num1 > num3:
#     print(num1)
# elif num1 == num3:
#     print('=')
# else:
#     print(num3)
