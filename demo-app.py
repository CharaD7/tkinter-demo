# Importing the tkinter module
from tkinter import *

# Creating an instance of the main window
win = Tk()

# Introducing a button
newBtn = Button(win, text="This is a Normal Button", fg="blue")
newBtn.place(x=80,
             y=100)  # Setting a specific location/geometry for our button

# Creating a label
lblLabel = Label(win,
                 text="Just some heading",
                 fg="red",
                 font=("Helvetica", 16))
lblLabel.place(x=80, y=50)

# Creating a textfield
txtText = Entry(win, text="A sample text field", bd=5)
txtText.place(x=80, y=150)

# Setting the custom window propterties
win.geometry("350x200+10+10")
win.title("Our Demo App")
win.mainloop()
