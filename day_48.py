#-------- DAY 48 "scope1" --------
print("Lesson 48: Scope 1")
# Local/General scope
# Function inside function
num1 = 210

def func():
    num2 = 30
    def innerFunc():
        print('Access the local number',num2)
    innerFunc()
    print('Access the global number', num1)

func()
print('---------------------\n',num1)
