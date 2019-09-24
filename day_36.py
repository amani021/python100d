#-------- DAY 36 "lambda2" --------
# 5. The power of lambda is better shown when you use them as an anonymous function inside another function
def func(n):
    return lambda x: x * n

result = func(3) #Call a function with an argument (3) & assigned to a variable result
lesson = func(6)
#Call lambda function using the variables & send a number as an argument
print('Lesson', lesson(6), ': Lambda 2\nThe result of 3 x 10 is:', result(10))
