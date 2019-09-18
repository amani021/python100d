#-------- DAY 30 "loops (for loop2)" --------
import turtle
t = turtle.Turtle()
t.width(2)
t.penup()
t.back(220)
t.right(90)
t.pendown()
def polygon(sides, length):
  t.color("purple")
  t.speed(0)
  angle = 360 / sides
  for side in range(sides):
      t.forward(length)
      t.right(angle)
  else:
      for _ in range(2, 7, 4):
          t.color('orange')
          t.forward(length+12)
          t.right(angle-7)
          for _ in range(3):
              t.color('red')
              t.left(270/angle)
              t.forward(length-30)
  t.hideturtle()
for shape in range(12):
    polygon(shape + 2, 35)
