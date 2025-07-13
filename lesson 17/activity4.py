def check_order(order):
    if order == "":                  # If nothing us entered
        pass                         # Do nothing
    elif order == "exit":
        return "stop"                # Use return to stop the program
    elif order == "water":
        print("We do not serve water unfortunately.")
        return                       # Just return without doing anything
    elif order == "spoiled juice": 
        print("Uh oh! Bad order found.")
        return "break"               # Signals to stop the loop
    else:
        print("Preparing your", order)

# Main loop
while True:
    order = input("Enter your juice order (or type 'exit' to leave): ")

    if order == "skip":
        print("Skipping...")
        continue                     # Skip to the next loop

    result = check_order(order)

    if result == "stop":
        print("Thank you! Come again.")
        break                        # Stop the loop
    elif result == "break":
        print("Something went wrong. Closing shop!")
        break                        # Stop the loop
    
