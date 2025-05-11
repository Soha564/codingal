#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.

units = int(input("Enter the units consumed:"))

if units < 50:
    per_unit_cost = 2.6 * units
    tax= 25
    total_cost = per_unit_cost + tax
elif units >= 50 and units < 100:
    per_unit_cost = 3.25 * units
    tax = 35
    total_cost = per_unit_cost + tax
elif units >= 100 and units < 200:
    per_unit_cost = 5.26 * units
    tax = 45
    total_cost = per_unit_cost + tax
elif units >= 200:
    per_unit_cost = 8.45 * units
    tax = 75
    total_cost = per_unit_cost + tax
else:
    print("Please enter the correct units consumed.")
print("The total cost:", round(total_cost, 3))
