from tkinter import *
from tkinter import messagebox

# Create main window
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        si = (p * r * t) / 100
        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# Labels and Entry widgets
Label(root, text="Principal (£):").place(x=50, y=50)
principal_entry = Entry(root)
principal_entry.place(x=200, y=50)

Label(root, text="Time (years):").place(x=50, y=100)
time_entry = Entry(root)
time_entry.place(x=200, y=100)

Label(root, text="Rate (%):").place(x=50, y=150)
rate_entry = Entry(root)
rate_entry.place(x=200, y=150)

# Button to calculate
Button(root, text="Calculate Interest", command=calculate_interest).place(x=140, y=200)

# Result display
result_label = Label(root, text="", fg="blue", font=("Arial", 12))
result_label.place(x=100, y=250)

root.mainloop()

