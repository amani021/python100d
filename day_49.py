#-------- DAY 49 "scope2" --------
print("Lesson 49: Scope 2")

num, value1 = 210, 290

def func():
    num = 30
    global value2 #Global keyword to be a global variable & access it from anywhere
    global value1 #Also you can use it to change the global variable's value inside function
    value1 = 20
    value2 = 12
    def innerFunc():
        print('Access the local number',num)
    innerFunc()
    print('Access the local number', num)

func()
print('---------------------\n', 'The sum of the global numbers',num, '+', value2, '+', value1, 'is:', num+value2+value1)
