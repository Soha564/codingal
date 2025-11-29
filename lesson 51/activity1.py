import turtle
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)