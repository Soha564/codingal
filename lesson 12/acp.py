# Rohit has got a school project where he has to make a program on the number system. There are four main types of the number system. So, to make their project more interesting they are making the project convert decimal number into binary.

num = int(input("Enter a positive number: "))
binary = ""
original_num = num 
while num > 0:
    if num % 2 == 0:
        binary = "0" + binary
    else: 
        binary = "1" + binary
    num = num // 2
print(f"The binary representation of {original_num} is {binary}." )
   

        
        


