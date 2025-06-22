# Polygon
import turtle

# Screen
screen = turtle.Screen()
screen.title("Polygons using turtle")
screen.setup(500, 400) # (w, h)

# Turtle
t = turtle.Turtle()
t.pencolor("black")
t.pensize(8)
t.shape("turtle")
t.speed(10)
t.fillcolor("purple")

# Hexagon
t.begin_fill()
for i in range(6):
    t.forward(70)
    t.right(60)
t.end_fill()

t.hideturtle()
turtle.done()