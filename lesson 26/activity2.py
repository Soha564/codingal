import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100. ")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    if input("Play again (y/n): ").lower() == 'y':
        guess_game()

guess_game()
