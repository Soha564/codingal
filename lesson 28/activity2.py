# Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented

class employee:

    def __init__(self):
        print("Employee has been hired.")

    def __del__(self):
        print("Desctructor called")

def create_obj():
    print("Making Object...")
    obj = employee()
    print("Funtion ended...")
    return obj

print("Calling create_obj() function...")
obj = create_obj()
print("Program End...")