import random
print("The Coin Toss")

while True:
    choice = random.choice(["Heads", "Tails"])
    if choice == "Heads":
        print("You have got Heads")

    else:
        print("You have got Tails.")
    print("Do you want to toss again, answer with a yes or no.")

    response = input().lower()

    if response == "no":
        print("Ok, bye")
        break