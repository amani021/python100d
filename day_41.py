#-------- DAY 41 "classes and objects1" --------
# Python is an OOP language
#Create a class, the syntax is: class className:
class special:
    #This __init__() function as a constructor in other languages
    #Usually use (self keyword) instead of (this) in other languages BUT you can use other names & it should be the first parameter
    def __init__(self, name, title):
        self.name = name
        self.title = title
    def newInfo(self): #Should have a parameter
        print("Lesson 41:", self.title, "1")
        print("Hello!\nI'm very proud of us to have come to this lesson :D")

#Create an object (obj) for special class
obj = special('amani', 'Classes and Objects')
obj.newInfo()
