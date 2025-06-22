# Polygon
import turtle

# Screen
screen = turtle.Screen()
screen.title("Polygons using turtle")
screen.setup(500, 400) # (w, h)

# Turtle
t = turtle.Turtle()
t.pencolor("crimson")
t.pensize(8)
t.shape("arrow")
t.speed(10)

# Square
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.hideturtle()
turtle.done()