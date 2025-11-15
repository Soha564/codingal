height = float(input("Enter your height in cm (decimal point): "))
weight = float(input("Enter your weight in kg (decimal point): "))

BMI = weight/(height/100)**2
print("Your BMI is: ", BMI)
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are average weight.")
elif BMI <= 34.9:
    print("You are overweight.")
elif BMI <= 39.5:
    print("You are obese.")
else:
    print("You are severly obese.")