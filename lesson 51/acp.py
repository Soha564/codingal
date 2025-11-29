import turtle
turtle.Screen().bgcolor("Light Blue")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

turtle.color("Yellow")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.color("Orange")
for i in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.color("red")
for i in range(6):
    turtle.forward(100)
    turtle.left(60)