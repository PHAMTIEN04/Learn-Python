# Import the required module from tkinter
from tkinter import *

# Create the main window
win = Tk()
win.geometry("250x250")

# Function to display the selected option
def show():
    Label(win, text=clicked.get()).pack()

# Create a StringVar to hold the selected option
clicked = StringVar()
clicked.set("CHOOSE")

# Define the available options for the drop-down menu
options = [
    "PIZZA",
    "COCA",
    "PEPSI",
    "CHICKEN"
]

# Create an OptionMenu widget to display the options
drop = OptionMenu(win, clicked, *options)
drop.pack()

# Create a button to show the selected option
bt = Button(win, text="Show Options", command=show)
bt.pack()

# Start the main event loop
win.mainloop()
