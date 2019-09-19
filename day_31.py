#-------- DAY 31 "functions" --------
import turtle

def star(color="lightblue", sides=5, length=50, angle=0, distance=-28):
    galileo = turtle.Turtle()
    galileo.color(color)
    galileo.width(5)
    galileo.speed(3)
    galileo.penup()
    galileo.left(angle) #Away from center
    galileo.forward(distance)
    galileo.pendown() #Start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()

star() #Take a default parameters value

for angle in [180, 135, 90, 45, 0]:
    star("red", 5, 50, angle, 100)
for angle in [180, 135, 90, 45, 0]:
    star("pink", 5, 30, angle, 50)
