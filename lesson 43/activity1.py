from tkinter import*

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    # Adding a label widget to TOp Window
    l2 = Label(top, text = "This is the Toplevel Window")
    l2.pack
    top.mainloop()

# Adding a label and button Widget to Root (Main Window)
l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

# Arranging elements
l.pack()
btn.pack()

root.mainloop()