#-------- DAY 33 "exercise" --------
import turtle
import random

terry = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
terry.penup()
terry.back(100)
terry.pendown()
A = range(3, 18, 2)
B = range(2, 17, 2)

for x in A:
    for y in B:
        color = random.choice(colors)
        terry.width(x)
        terry.color(color)
        terry.forward(y*2)
    terry.penup()
    terry.right(x*4)
    terry.back(180)
    terry.pendown()
terry.hideturtle()
