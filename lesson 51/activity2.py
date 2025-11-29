import turtle
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(3):
    turtle.forward(100)
    turtle.left(120)
for i in range(1):
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()

turtle.right(90)
turtle.forward(100)

for i in range(2):
    turtle.right(120)
    turtle.forward(100)
turtle.exitonclick()