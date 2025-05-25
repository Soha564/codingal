correct_password = 'abc123'
attempts = 3

while attempts > 0:
    guess = input("Enter the password: ")
    if guess == correct_password:
        print("Access Granted")
    else:
        attempts = attempts - 1
        print(f"Incorrect. Attempts left: {attempts}")
    
    if attempts == 0:
        print(f"Access denied. Atempts left:{attempts}")