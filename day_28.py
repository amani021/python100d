#-------- DAY 28 "loops (while loop)" --------
import turtle
terry = turtle.Turtle()
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
terry.width(3)
terry.speed(4)
terry.penup()
terry.back(100)
terry.pendown()
terry.hideturtle()
for coolpic in rainbow:
    line = 1
    terry.color(coolpic)
    while line < 7:
        terry.forward(70)
        terry.right(60)
        # if line == 4:
        #     break
        line += 1
    # else:
    #     terry.forward(60)
    #     terry.left(1)
    #     terry.pendown()
    terry.penup()
    terry.forward(90)
    terry.left(60)
    terry.pendown()
