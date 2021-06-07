# Importing tkinter

import tkinter as tk  # aliasing tkinter
from tkinter import ttk  # importing the components widget

# Creating an instance of tk
win = tk.Tk()

# Giving our window a title
win.title("Customer Sign Up Form")

# Creating an empty space
ttk.Label(win).grid(row=0)

# Setting our username labels and input boxes
lblUserName = ttk.Label(win, text="Username: ")
lblUserName.grid(column=1, row=1)

# Creating an empty space
ttk.Label(win).grid(row=2)

# Setting our username textbox
name = tk.StringVar()
txtUserName = ttk.Entry(win, width=16, textvariable=name)
txtUserName.grid(column=3, row=1)

# Setting our email labels and input boxes
lblEmail = ttk.Label(win, text="Email: ")
lblEmail.grid(column=1, row=3)

# Setting our email textbox
email = tk.StringVar()
txtEmail = ttk.Entry(win, width=25, textvariable=email)
txtEmail.grid(column=3, row=3)

# Creating an empty space
ttk.Label(win).grid(row=4)

# Setting our password labels and input boxes
lblPassword = tk.Label(win, text="Password: ")
lblPassword.grid(column=1, row=5)

# Setting our password text box
password = tk.StringVar()
txtPassword = ttk.Entry(win, width=20, textvariable=password)
txtPassword.grid(column=3, row=5)

# Creating an empty space
ttk.Label(win).grid(row=6)

# Setting up our submit button
btnSubmit = ttk.Button(win, width=15, text="Submit")
btnSubmit.grid(column=3, row=7)

# Invoking the GUI loop
win.mainloop()
