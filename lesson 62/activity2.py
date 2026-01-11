num1= int(input("Enter the larger number: "))
num2 = int(input("Enter the smaller number: "))
while (num2):
    ns = num2
    num2 = num1%num2
    num1 = ns
print("The HCF is: ", num1)
    