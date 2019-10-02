#-------- DAY 44 "inheritance2" --------
print("Lesson 44: Inheritance 2")
class parent:
    def __init__(self, name):
        self.name = name
    def mainMethod(self):
        print('My name is', self.name)

class child(parent):
    def __init__(self, name, mood):
        super().__init__(name) #Will inherit all the properties & methods from its parent
        self.dayMood = mood #Add a property
    #Add a method
    def method(self):
        print("I'm so", self.dayMood, "today :)")

obj = child('Amal', 'happy')
obj.mainMethod()
obj.method()
