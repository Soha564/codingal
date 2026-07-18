def update_char(text, pos, new_char):
    if 0 <= pos < len(text):
        return text[:pos] + new_char + text[pos+1:]
    else:
        print("Invalid position for replacement.")
        return text

def delete_char(text, pos):
    if 0 <= pos < len(text):
        return text[:pos] + text[pos+1:]
    else:
        print("Invalid position for deletion.")
        return text

original = input("Enter a string: ")

pos_replace = int(input("Enter the position to replace: "))
new_char = input("Enter the new character: ")
modified = update_char(original, pos_replace, new_char)

pos_delete = int(input("Enter the position to delete: "))
modified = delete_char(modified, pos_delete)

print("Original string:", original)
print("Modified string:", modified)
