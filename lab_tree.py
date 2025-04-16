import turtle
import random

def recursive_tree(branch_length, angle, t, s):
    """Draw a tree recursively"""
    if s < 1:
        t.pensize(1)
    else:
        t.pensize(s)

    if branch_length > 5:
        l_size = random.randint(6, 9) / 10
        r_size = random.randint(6, 9) / 10
        l_angle = random.randint(-5, 5)
        r_angle = random.randint(-5, 5)


        t.forward(branch_length)
        t.right(angle + l_angle)
        recursive_tree(branch_length * l_size, angle, t, s-1)
        t.left(angle * 2 + l_angle + r_angle)
        recursive_tree(branch_length * r_size, angle, t, s-1)
        t.right(angle + r_angle)
        t.backward(branch_length)

t = turtle.Turtle()
turtle.tracer(False) 
t.left(90)      
t.penup()
t.setposition(0, -200)
t.pendown()
recursive_tree(100, 20, t, 10)
turtle.update()
  
turtle.mainloop()