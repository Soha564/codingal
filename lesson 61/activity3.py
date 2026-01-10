#Roman numerals
def romanConverter(roman_input):
    roman = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V': 5, 'I' : 1}

    result = 0

    for i in range(0, len(roman_input)-1):
        if roman[roman_input[i]] < roman[roman_input[i+1]]:
            result -= roman[roman_input[i]]

        else:
            result += roman[roman_input[i]]
    return result + roman[roman_input[-1]]
roman = input("Enter a Roman Numeral: ")

print("Integer equivalent: ", romanConverter(roman))