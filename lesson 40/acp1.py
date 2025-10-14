from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add labels
lbl = Label(text="Date of birth:", fg="white", bg="#072F5F", height = 1, width = 300)

# Add label for getting name as input from user
# Use entry widget to create text box for user to enter details
name_lb1 = Label(text="DD", bg = "#3895D3")
date_entry1 = Entry()
name_lb2 = Label(text="MM", bg = "#3895D3")
date_entry2 = Entry()
name_lb3 = Label(text="YYYY", bg = "#3895D3")
date_entry3 = Entry()
# Function to display message 
def display():
    # Read input given by user
    date1 = date_entry1.get()
    date2 = date_entry2.get()
    date3 = date_entry3.get()
    # Declaring a global variable
    # To make it accessible anywhere in the program
    global message
    message = "Welcome to the Application!\n"
    greet = "You D.o.B is: "+date1+"."+date2+"."+date3+"\n"
    # Display details in a text box
    # Specify where to add the details inside trhe textbox
    text_box.insert(END, message)
    text_box.insert(END,greet)

# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display funstion will be called automatically
btn = Button(text = "Begin", command=display, height=1, bg="#1261A0", fg="white")

# Organize all the widgets in the window
lbl.pack()
name_lb1.pack()
name_lb2.pack()
name_lb3.pack()
date_entry1.pack()
date_entry2.pack()
date_entry3.pack()
btn.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()