from tkinter import *

win = Tk()

var = StringVar()

def check():        
    # Get the value of the variable and create a Label with the text
    lb_check = Label(win, text=var.get())
    lb_check.pack()

# Create a Checkbutton with 'Yes' and 'No' options
checkbox = Checkbutton(win, text="You Love Me?", variable=var, onvalue="Yes", offvalue="No")
checkbox.deselect()  # Deselect the Checkbutton initially
checkbox.pack()

# Create a Button to display the selected option
bt = Button(win, text="Click", command=check)
bt.pack()

win.mainloop()
