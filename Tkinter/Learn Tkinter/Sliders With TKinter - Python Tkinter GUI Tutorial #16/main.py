from tkinter import *

win = Tk()
win.geometry("400x400")

# Function to update the label and change the window's width based on the horizontal scale value
def sc_lb(v):
    # Create a label to display the current value of the horizontal scale
    mylabel = Label(win, text=horizontal.get())
    mylabel.pack()

    # Update the window's width based on the current value of the horizontal scale
    win.geometry(str(horizontal.get()) + "x400")

# Create a vertical scale widget ranging from 0 to 200, and bind it to the sc_lb function
vertical = Scale(win, from_=0, to=200, command=sc_lb)
vertical.pack()

# Create a horizontal scale widget ranging from 0 to 400, with a horizontal orientation,
# and bind it to the sc_lb function
horizontal = Scale(win, from_=0, to=400, orient=HORIZONTAL, command=sc_lb)
horizontal.pack()

# The following lines are commented out as they are not being used in this code snippet.
# You can uncomment them to add a button if needed.
# bt = Button(win, text="Click Me", command=sc_lb)
# bt.pack()

win.mainloop()
