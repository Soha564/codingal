# Homeowrk 1
import math
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

# Homework 2 - extra

import random
import time

print("Rules: You first press enter and then their will be a waiting time, but as soon as the '💥 Press Enter NOW!' appears you press enter again - this is to test your reaction time limit.")

input("⏳ Press Enter to start...")
wait = random.uniform(3, 7)
time.sleep(wait)
start = time.time()
input("💥 Press Enter NOW!")
end = time.time()

reaction_time = round(end - start, 3)
print(f"Your reaction time was {reaction_time} seconds.")


