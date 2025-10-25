from tkinter import *

# Create main window
root = Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  # Alice Blue background

# Function to check password strength
def check_strength():
    password = entry.get()
    length = len(password)
    
    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "#E6860A"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "#6EBD6E"  # Light Green
    else:
        strength = "Very Strong"
        color = "#006400"  # Dark Green
    
    result_label.config(text=f"Password Strength: {strength}", fg=color)


# Add widgets
title_label = Label(root, text="Enter Password:", font=("Arial", 14), bg="#f0f8ff")
title_label.pack(pady=20)

entry = Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=10)

check_button = Button(root, text="Check Strength", command=check_strength, bg="#4682B4", fg="white", font=("Arial", 12))
check_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
result_label.pack(pady=20)

# Run the application
root.mainloop()