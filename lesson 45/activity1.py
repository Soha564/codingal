from tkinter import*
from tkinter import messagebox

# Create main window
root = Tk()
root.title("Restaurant Management System")
root.geometry("400x400")
root.configure(bg="light yellow")

# Menu Dictionary
menu = {
    "Pizza": 14,
    "Burger": 7,
    "Pasta" : 5,
    "Coffee" : 3 
    }

# Variables
item_var = StringVar(value = "Pizza")
qty_var=IntVar(value=1)
total_var=IntVar(value=0)

# Order Lists
orders = []

# Functions to add items
def add_item():
    item = item_var.get()
    qty = qty_var.get()
    cost = menu[item] * qty
    orders.append((item, qty, cost))
    total_var.set(total_var.get()+ cost)
    messagebox.showinfo("Item Added", f"Added {qty} x {item} = £{cost}")

# Function to show bill
def show_bill():
    bill = "-----BILL----\n"
    for item, qty, cost in orders:
        bill += f"{item} ({qty}) = £{cost}\n"
    bill == f"\nTotal Amount: £{total_var.get()}"
    messagebox.showinfo("Bill", bill)

# Heading
Label(root, text="Restaurant Management System", font=("Arial", 14, "bold"), bg="light yellow").pack(pady=10)

# Item selecyoon
Label(root, text="Select Item:", bg =  "light yellow").pack()
OptionMenu(root, item_var, *menu.keys()).pack()

# Quantity
Label(root, text="Enter Quantity:", bg = "light yellow").pack()
Entry(root, textvariable=qty_var).pack()

# Buttons
Button(root, text ="Add to Order", command=add_item, bg="light green").pack(pady=5)
Button(root, text ="Show Bill", command=show_bill, bg="light blue").pack(pady=5)
Button(root, text ="Exit", command=root.destroy, bg="red", fg="white").pack(pady=5)

# Run Window
root.mainloop()