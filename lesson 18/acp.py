def check_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError ("Age cannot be negative.")
        elif age > 122 and age < 150:
            print("You have surpassed the age of the oldest person in history!")
        elif age > 150:
            raise ValueError ("Age cannot be that high (scientifically).")
        
        if age % 2 == 0:
            print(f"Your age {age} is even.")
        else:
            print(f"The age {age} is odd.")

    except ValueError as e:
        print(f"Invalid age entered: {e}")

user_input = input("Enter your age: ")
check_age(user_input)
