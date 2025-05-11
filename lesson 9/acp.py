#Write a program to check the age entered by the user is between 10 to 20 years or not?

print("THE AGE CLASSIFIER FOR THE RIDE")
age = int(input("Please enter your age:"))

if age <= 10 and age > 0:
    print(f"Your age is {age} so you are still a child, and are below the age range for the ride, so therefore are not permitted to enter the ride.")
elif age > 10 and age < 13:
    print(f"Your age is {age} so you are  classified as a preteen and are between the age range of 10 and 20 so therefore are permitted to enter the ride.")
elif age >= 13 and age < 20:
    print(f"Your age is {age} so you are classified as a teen and are between the age range of 10 to 20 so therefore are permitted to enter the ride.")
elif age <= 20:
    print(f"Your age is {age} so you are classified as an adult and are above the age range for the ride, so therefore are not permitted to enter the ride.")
else:
    print("Please enter your correct age.")