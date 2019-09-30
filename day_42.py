#-------- DAY 42 "classes and objects2" --------
class special:
    def __init__(self, name, title):
        self.name = name
        self.title = title
    def newInfo(self): #Should have a parameter
        print("Lesson 42:", self.title, "2")
        print("Hi!\nMy name is", obj.name, "^.^")

#Create an object (obj) for special class
obj = special('amani', 'Classes and Objects')
obj.name = 'aymn' #Modify object properties
# del obj.title #Dekete object properties
# del obj #Delete object
obj.newInfo()
