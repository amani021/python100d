#-------- DAY 29 "loops (for loop1)" --------
import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t = turtle.Turtle()
t.width(18)
t.speed(0)

for step in range(100):
    angle = random.randint(-96, 100)
    color = random.choice(colors)
    if color == 'orange':
        break
    t.color(color)
    t.right(angle*5)
    t.forward(10)
