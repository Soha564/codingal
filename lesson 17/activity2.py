# Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.

for x in range(10): #0-9
    if x % 20 == 0:   #condition 1
      print("twist")  #display result

    elif x % 15 == 0: #condition 2
      pass            #pass statement (no output)

    elif x % 5 == 0:  #condition 3
      print("fizz")   #display result

    elif x % 3 == 0:  #condition 4
       print("buzz")  #display result
    
    else:             #condition 5
       print(x)       #display result