# Write a program to display 1 to 10 numbers in reverse order and skip the number 5

var = 10           # initialise
while var > 0:     #iterate loop
    var = var - 1
    if var == 5:   #condition 1
        continue   #continue statement
        # display result
    print("/n Current variable value:", var)

print("/n Good Bye!")
