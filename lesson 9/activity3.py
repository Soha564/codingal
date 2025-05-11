#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
print("Choose your ride:")
print("1. Bike")
print("2. Car")
ride_choice = int(input("Enter you choice via the number options above"))

if ride_choice == 1:
    print("You have selected Bike.")
    print("What type of bike do you want?")
    print("1. Type 1")
    print("2. Type 2")

    choice = int(input("Enter you choice:"))

    if choice == 1:
        print("You have selected Type 1.")
    else:
        print("You have haev selected Type 2.")
else:
    print("You have selected Car.")
    print("What type of car do you want?")
    print("1. Type 1")
    print("2. Type 2")

    choice = int(input("Enter you choice:"))

    if choice == 1:
        print("You have selected Type 1")
    else:
        print("You have selected Type 2")

