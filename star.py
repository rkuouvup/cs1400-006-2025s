import turtle
import random

t = turtle.Turtle()
#t.speed(0)
turtle.tracer(False)

for n in range(10):
    t.penup()
    t.setposition(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()

    size = random.randint(30, 100)
    for i in range(5):
        t.forward(size)
        t.right(144)



turtle.done()