from turtle import Turtle

t = Turtle()
t.speed(0)

START_WIDTH = 90
START_X = 100
START_Y = 100

t.penup()
t.goto(START_X, START_Y)
t.pendown()
t.right(30)

def draw_square(size):
    if size < 5:
        return
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.left(90)
    t.forward(size)
    t.right(90)
    t.forward(size*0.125)
    draw_square(size*0.75)

x = START_X
y = START_Y

for i in range(6):
    x = t.xcor()
    y = t.ycor()
    draw_square(START_WIDTH)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(START_WIDTH)
    t.right(60)


    



input()
