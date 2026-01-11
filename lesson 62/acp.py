num1= int(input("Enter the larger number: "))
orig1 = num1
num2 = int(input("Enter the smaller number: "))
orig2 = num2
while (num2):
    ns = num2
    num2 = num1%num2
    num1 = ns
print("The HCF is: ", num1)
LCM = (orig2*orig2)/num1
print("The LCM is:", LCM)