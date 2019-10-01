#-------- DAY 43 "inheritance1" --------
print("Lesson 43: Inheritance 1")
#Any class created can be a parent class
class weather:
    def __init__(self, date, day):
        self.date = date
        self.day = day
    def func(self):
        print(self.date, ',', self.day)

#Creat a child class, childName(parentName)
class rainy(weather):
    #__init__() is an override of parent's function
    def __init__(self, date, day):
        self.date = date
        self.day = day
    def funcR(self):
        print('It was a nice rainy day .^-^/\n---------------------')
    # pass #This keyword used when you don't want to add properties or methods to the class

class sunny(weather):
    def __init__(self, date, day):
        weather.__init__(self, date, day) #If you want to keep inheritance of the parent's __init__() function
    def funcS(self):
        print('Last days were rainy very good ^^)')

obj1 = rainy('1 Oct 2019', 'Tuesday')
obj2 = sunny('Muharram 1441', '')
obj1.func()
obj1.funcR()
obj2.func()
obj2.funcS()
