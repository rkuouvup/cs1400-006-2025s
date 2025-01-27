import turtle
import random

def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

t = turtle.Turtle()
t.speed(0)
#turtle.tracer(False)

for times in range(18):
    size = random.randint(20, 100)
    draw_square(size)
    t.right(20)

t.penup()
t.setposition(-200, -200)
t.pendown()

for times in range(10):
    draw_square(times * 10)
    t.right(36)


turtle.done()