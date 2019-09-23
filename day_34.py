#-------- DAY 34 "functions2" --------
import turtle
# 1. The functions can return values
# 2. Also, it can call itself by something known as recursion
t = turtle.Turtle()
t.width(5)
def iLetter(size):
    t.color('green')
    t.penup() #
    t.left(size[1])
    t.forward(200)
    t.pendown()
    t.left(20)
    t.forward(50)
    t.penup() #
    t.back(25)
    t.pendown()
    t.left(size[2])
    t.forward(60)
    t.penup() #
    t.right(size[0])
    t.back(25)
    t.pendown()
    t.forward(50)
def heart(*items):
    t.color(items[1])
    t.begin_fill()
    t.fillcolor(items[1])
    t.left(items[0])
    t.forward(140)
    t.circle(-70, 200)
    t.setheading(items[2])
    t.circle(-70, 200)
    t.forward(140)
    t.end_fill()
def kLetter(arg1, arg2):
    t.color(arg2)
    t.penup() #
    t.left(90)
    t.forward(arg1)
    t.pendown()
    t.back(arg1)
    t.penup() #
    t.setheading(70)
    t.forward(arg1)
    t.left(170)
    t.pendown()
    t.forward(37)
    t.penup() #
    t.back(10)
    t.pendown()
    t.left(55)
    t.forward(40)
def sLetter():
    t.circle(20, 200)
    t.forward(10)
    t.circle(-20, 200)
def aLetter():
    t.left(75)
    t.forward(60)
    t.left(210)
    t.forward(60)
    t.penup() #
    t.back(20)
    t.setheading(180)
    t.pendown()
    t.forward(25)

iLetter([270, 160, 90]) #passing a list as a parameter
t.penup()
t.forward(120)
t.pendown()
heart(140, 'red', 60) #unknown how much arguments will passing to a function
t.penup()
t.right(220)
t.forward(120)
t.pendown()
kLetter(arg2='green', arg1=60) #keyword arguments (kwargs)
t.penup() #
t.left(200)
t.forward(50)
t.pendown()
sLetter()
t.penup()
t.setheading(360)
t.forward(60)
t.pendown()
aLetter()
