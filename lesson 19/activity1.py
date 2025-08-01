import random
number = random.randint(1,20)

print("I will generate a number from 1 to 20, and you have to guess the number one at atime.")
print("The game ends once you get the number right!")

while True:
    guess = int(input("Give me your best guess! \n"))
    if number == guess:
        print("You win the game")
        print("The number was, ", number, "welldone!")
        break
    else:
        print("Your guess is not quite right, please try again. \n")
