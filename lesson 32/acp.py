# converting integers into ROman Numerals:
class RomanConverter:
    def __init__(self):
        self.TheRomanNumerals_ = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def int_to_roman(self, num):
        Roman = ''
        for value, symbol in self.TheRomanNumerals_:
            while num >= value:
                Roman += symbol
                num -= value
        return Roman

try:
    user_input = int(input("Enter an integer between 1 and 3999: "))
    if 1 <= user_input <= 3999:
        converter = RomanConverter()
        Roman_value = converter.int_to_roman(user_input)
        print(f"Roman numeral: {Roman_value}")
    else:
        print("Please enter a number within the valid range (1-3999): ")
except ValueError:
    print("Invalid input. Please enter a valid integer: ")