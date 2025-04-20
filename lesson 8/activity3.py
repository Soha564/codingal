#The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.

prev_mean = 38
total = 40
wrong_num = 36
right_num = 56

sum = prev_mean *  total
print("The sum of all 40 numbers is", sum)

correct_sum =  (sum - wrong_num) + right_num
print("The correct sum is", correct_sum)

correct_mean = correct_sum / total
print("The correct mean is", correct_mean)
