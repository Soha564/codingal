print("- Alphabet Character detecter -")
character = input("Please enter a character of your choice:")
character_str = str(character)
if character_str.isalpha():
    print("'", character, "' is part of the alphabet.")
else:
    print("'", character, "' is not part of the alphabet.")