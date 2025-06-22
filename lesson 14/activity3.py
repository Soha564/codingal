# Polygon
import turtle

# Screen
screen = turtle.Screen()
screen.title("Creating a star")
screen.setup(500, 400) # (w, h)

# Turtle
t = turtle.Turtle()
t.pencolor("orange")
t.pensize(2)
t.shape("turtle")
t.speed(5)
t.fillcolor("yellow")

# star
# upper triangle
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()
t.penup()
t.left(90)
t.forward(100)
t.right(90)

t.pendown()
# second triangle
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.right(120)
t.end_fill()

t.hideturtle()
turtle.done()