import turtle
import random

color_set = ["red", "green", "blue", "green", "green"]

def koch_line(t, width, depth=0):
    if depth <= 0: # base case
        rand_color = random.choice(color_set)
        t.color(rand_color)
        t.forward(width)
    else:
        koch_line(t, width/3, depth-1)
        t.left(60)
        koch_line(t, width/3, depth-1)
        t.right(60*2)
        koch_line(t, width/3, depth-1)
        t.left(60)
        koch_line(t, width/3, depth-1)

t = turtle.Turtle()
t.pensize(5)
turtle.tracer(False)

for _ in range(3):
    koch_line(t, 300, 3)
    t.right(120)

turtle.update()
turtle.done()