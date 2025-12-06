import random

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

numbers = list(range(start, end + 1))

chosen_number = random.choice(numbers)

while True:
    guess = int(input("Enter your guess: "))
    
    if guess > chosen_number:
        print("Your guess is too high! Try again.")
    elif guess < chosen_number:
        print("Your guess is too low! Try again.")
    else:
        print("Congratulations! You guessed it right!")