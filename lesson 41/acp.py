from tkinter import*
from datetime import datetime

# Crteate window
root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

# Create a frame to organise elements better
frame = Frame(master=root, height=300, width=360, bg="#d0efff")

# Add widgets
# Add label
lbl1 = Label(frame, text="Name:", bg = "#3895D3", fg = 'white', width=12)
lbl2 = Label(frame, text="DD", bg = "#3895D3", fg='white', width=12)
lbl3 = Label(frame, text= "MM", bg="#3895D3", fg = 'white', width=12)
lbl4 = Label(frame, text="YYYY", bg="#3895D3", fg = 'white', width=12)

# Use Entry Widget to create a text boxfor user to enter details
name_entry = Entry(frame)
D_entry = Entry(frame)
M_entry = Entry(frame)
Y_entry = Entry(frame)


# Function to display message
def display():
    name = name_entry.get()
    day = int(D_entry.get()) 
    month = int(M_entry.get())   
    year = int(Y_entry.get())

    birth_date = datetime(year, month, day)
    today = datetime.today() 
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    name = name_entry.get()
    greet = "Hello " + name
    age = "\nYou are "+str(age_years) +" years old."
    textbox.insert(END, greet)
    textbox.insert(END, age)

#Textbox to display message
textbox = Text(bg = "#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text="Create Account", command=display, bg="red")

# Arrange all widgets
frame.place(x=20, y=0)
lbl1.place(x=20, y= 20)
name_entry.place(x=150, y = 20)
lbl2.place(x=20, y=80)
D_entry.place(x=150, y=80)
lbl3.place(x=20, y= 140)
M_entry.place(x=150, y=140)
lbl4.place(x=20, y=200)
Y_entry.place(x=150, y=200)
btn.place(x=150, y=240)
textbox.place(y=280)


root.mainloop()