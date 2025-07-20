try:
    num1, num2 = eval(input("Input 2 numbers seperated by a comma: "))
    result = num1 / num2
    print(result)

except ZeroDivisionError as z:
    print("Error", z)

except SyntaxError:
    print("Please use a comma. E.g 1, 2")

except:
    print("Input Error")

else: 
    print("No exception")

finally:
    print("This will be executed no matter what.")