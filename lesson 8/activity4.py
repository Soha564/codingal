#Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?

c1 = float(input("Enter the speed of the first cyclist:"))
c2 = float(input("Enter the speed of the second cyclist:"))
c3 = float(input("Enter the speed of the third cyclist:"))

avg_speed = (c1 + c2 + c3) / 3
print("The average speed is", avg_speed, "km/h")
if c1 < avg_speed:
    print("The Speed of the first cyclist is slower than the average with a difference of", avg_speed - c1)
if c2 < avg_speed:
    print("The Speed of the second cyclist is slower than the average with a difference of", avg_speed -c2)
if c3 < avg_speed:
    print("The Speed of the third cyclist is slower than the average with a difference of", avg_speed - c3)
