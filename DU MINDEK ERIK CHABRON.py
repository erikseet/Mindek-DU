import turtle
import random

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)

def trojuholnik(dlzka):
    for i in range(3):
        t.fd(dlzka)
        t.rt(120)

def kruh(dlzka):
    for i in range(360):
        t.fd(dlzka)
        t.rt(1)

def pohyb():
    t.pu()
    x = random.randrange(-320, 320)
    y = random.randrange(-320, 320)
    t.setpos(x, y)
    h = random.randrange(360)
    t.seth(h)
    t.pd()
def random_color():
    banan = ["gold", "royalblue", "teal", "red", "green", "purple", "black", "brown", "grey"]
    x = banan[random.randrange(9)]
    return x;
turtle.delay(0)
t = turtle.Turtle()
t.pensize(5)
for i in range(69):
    pohyb()
    x = random.randrange(0, 3)
    if x == 0:
        t.pencolor(random_color())
        stvorec(random.randrange(30, 69))
    elif x == 1:
        t.pencolor(random_color())
        trojuholnik(random.randrange(30,69))
    else:
        t.pencolor(random_color())
        kruh(random.randrange(1, 3))
turtle.exitonclick()