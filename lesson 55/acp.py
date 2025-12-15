class Expression:
    def __init__(self):
        pass
    def add(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        answer = num1+num2+num3
        return answer
    
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
    
exp = Expression()

choice = input("Would you like to find the sum (y/n): ").lower()
if choice == "y":
    answer = exp.add(num1, num2, num3)
    print("The sum is:", answer)
elif choice =="n":
    print("ok.")
else:
    print("Invalid output.")    