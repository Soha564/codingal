# Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3.
def find_cube(num):
    return num ** 3

def divisible_by_3(num):
    if num % 3 == 0:
        cube = find_cube(num)
        return cube
    else:
        return False
    
print(divisible_by_3(8))
print(divisible_by_3(27))
print(divisible_by_3(9))
