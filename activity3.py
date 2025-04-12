
# You want to check a person’s BMI and give them feedback:

# A person is underweight if BMI is less than 18.5

# A person is normal if BMI is between 18.5 and 24.9

# A person is overweight if BMI is 25 or more

weight = float(input("Enter your weight in kilograms (please enter in decimal)"))
height = float(input("Enter your height in metres (please enter in decimals)"))
bmi = weight / (height **2 )
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You meet the average weight standards.")
elif bmi>= 25:
    print("You are overweight.")
else:
    print("The BMi calculation is wrong.")