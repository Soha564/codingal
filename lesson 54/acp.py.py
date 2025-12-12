class Introduction:
    Object = "robot"

    def __init__(self, name, age):
        self.name = name
        self.age = age
Tom = Introduction("Blu", 10)
Jerry = Introduction("Woo", 15)

print("Tom is a {}".format(Tom.Object))
print("Jerry is also a {}".format(Jerry.Object))

print("{} is {} years old.".format(Tom.name, Tom.age))
print("{} is {} years old.".format(Jerry.name, Jerry.age))