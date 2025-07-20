def check_age(age):
    try:
        #convert the input to an integer
        age = int(age)
        #check if the age is positive integer
        if age < 0:
            raise ValueError ("Age cannot be negative.")
        # check if the age is even or odd
        if age % 2 == 0:
            print(f"Your age {age} is even.")
        else:
            print(f"The age {age} is odd.")

    except ValueError as e:
# Handle the exception if the input is not a valid integer or is negative
        print(f"Invalid age entered: {e}")

# Example usage:
user_input = input("Enter your age: ")
check_age(user_input)
