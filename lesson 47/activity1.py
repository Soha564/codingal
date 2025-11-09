name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in decimal format): "))
student = input("Enter whether you are a student or not (in yes or no format): ").lower()
if student == "yes":
    student = True
else:
    student = False
print("Name: ", name)
print("Age:", str(age))
print("Weight (in integer format): ", int(weight))
print("Student? ", student)