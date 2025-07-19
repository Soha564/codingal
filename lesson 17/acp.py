def due_amount():
    bill = float(input("Enter the bill (in decimals): "))
    paid = float(input("Enter the amount paid (in decimals): "))
    if paid > bill:
        change = paid - bill
        print("Return £", change)
    elif paid < bill:
        amount_remaining = bill - paid
        print("You are still due to pay £", amount_remaining)
    else:
        print("You have paid the whole amount")

due_amount()
    