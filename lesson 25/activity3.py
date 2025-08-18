# Write a program where the value of i begins from 1 and goes to 10. When the value of i becomes 5, force the interpreter to exit the program.

for i in range(1, 11):
    print(i)
    if i == 5:
        print("Exiting...")
        exit()