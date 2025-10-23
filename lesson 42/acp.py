
from tkinter import*

# Crteate window
root = Tk()
root.title('Length Converter App')
root.geometry('400x400')

# Create a frame to organise elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets
# Add label
lbl1 = Label(frame, text="Enter measurement in inches:", bg = "#3895D3", fg = 'white', width = 25)

# Use Entry Widget to create a text boxfor user to enter details
name_entry = Entry(frame)

# Function to display message
def display():
    name = name_entry.get()
    greet = "Welcome "
    message = "\n" +name+" inches is approximately "+ str(float(name)*2.5)+"cm"
    textbox.insert(END, greet)
    textbox.insert(END, message)

#Textbox to display message
textbox = Text(bg = "#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text="Convert", command=display, bg="red")

# Arrange all widgets
frame.place(x=20, y=0)
lbl1.place(x=10, y= 20)
name_entry.place(x=230, y = 20)
btn.place(x=170, y=210)
textbox.place(y=250)

root.mainloop()