# Write a function that accepts the beginning and end range of numbers, and find the square values of those numbers. Then filter the odd and even square values and print them.

            
start = int(input("Please enter the start of the range: "))
end = int(input("Please enter the end of the range: "))

square_numbers = []

for number in range(start, end + 1):
    square = number * number
    square_numbers.append(square)

even_squares = []
odd_squares = []

for square in square_numbers:
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("All square numbers:", square_numbers)
print("Even square numbers:", even_squares)
print("Odd square numbers:", odd_squares)

