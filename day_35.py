#-------- DAY 35 "lambda1" --------
# 1. Lambda function is a small anonymous function
# 2. It can take any number of arguments BUT can only have one expression!!
# 3. The syntax is: lambda arguments: expression
# 4. It should be assigned to a variable to ease to call
x = lambda num1, num2: num1 * num2 + 3
print('Lesson', x(8, 4), ': Lambda 1')
