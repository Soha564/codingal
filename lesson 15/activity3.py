def add(P, Q):
    #this function is used for adding the two numbers
    return P + Q
def subtract(P, Q):
    #this function is used for subtracting the two numbers
    return P - Q
def multiply(P, Q):
    #this function is used for multiplying the two numbers
    return P * Q
def divide(P, Q):
    #this function is used for dividing the two numbers
    return P / Q

#Now we will take the input of the user

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter your choice (a/b/c/d).")
num1 = int(input("Please enter you first number."))
num2 = int(input("Please enter you second number."))

if choice =="a":
    print(num1, "+",num2, "=", add(num1, num2))

elif choice =="b":
    print(num1, "-",num2, "=", subtract(num1, num2))

elif choice =="c":
    print(num1, "x",num2, "=", multiply(num1, num2))

elif choice =="d":
    if num2 == 0:
        print("Undefined")
    else:
        print(num1, "/",num2, "=", divide(num1, num2))
    
else:
    print("This is an invalid input")