# Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay

def total_calc(bill_amount, tip_perc):
    total = bill_amount + (bill_amount * tip_perc) // 100
    print(total)

total_calc(180, 10)