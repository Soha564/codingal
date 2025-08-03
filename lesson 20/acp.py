# Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip


def hotel_cost(nights):
    return nights * 140

def plane_price(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475

def car_rental_cost(days):
    if days >= 7 :
        return 40*days - 50
    elif days >= 3 :
        return 40*days - 20
    else:
        return days * 40

def trip_cost(city, days, spending):
    return car_rental_cost(days) + hotel_cost(days) + plane_price(city) + spending

print("Cost of car rental: ",car_rental_cost(5))

print("Cost of plane ride: ",plane_price("Los Angeles"))

print("Cost of hotel room: ", hotel_cost(7))

print("Total cost of the trip:",trip_cost("Los Angeles",7,500))

print(trip_cost("Tampa",6,500))