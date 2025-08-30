def introduction(first_name, last_name = "Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("Henry")

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")

happy_new_year()


def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)

