class Employee:
    def __init__(self): # constructor
        print("Employee has been hired.")
    
    def __del__(self): # destructor
        print("Employee has been fired.")

emp1 = Employee()
del emp1 # manually destruction