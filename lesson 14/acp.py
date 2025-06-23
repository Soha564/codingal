import turtle

screen = turtle.Screen()
screen.title("Spiralling Homework")
screen.setup(500, 400)

t = turtle.Turtle()
t.pencolor("lavender")
t.pensize(5)
t.shape("arrow")
t.speed(10)
size = 2
while True: #iterate loop
    for i in range(4):
        t.fd(size + 1)
        t.left(90)
        size = size - 5
        size = size + 1