# Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.

t = (1, 0, 0, 0, 1, 1, 0)
rainy = 0
sunny = 0

for k in t:
    if k == 0:
      sunny += 1
    else:
      rainy += 1

print("Sunny count:", sunny)
print("Rainy count:", rainy)

if sunny > rainy:
   print("It's sunny. It's good weather.")
else:
   print("Please carry an umbrella.")
