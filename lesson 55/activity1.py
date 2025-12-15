class Employee:
    def __init__(self):
        print("Employee hired.")
    
    def __del__(self):
        print("Destructor called, Employee fired.")

obj = Employee()
del obj