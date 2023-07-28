from tkinter import *
root = Tk()
# Creating a Label Widget
myLabe = Label (root, text=" Hello World!")
myLabe12 = Label(root, text= "My Name Is John Elder")
# Shoving it onto the screen
myLabe.grid(row = 0 , column= 0)
myLabe12.grid(row=1,column=5)
root. mainloop()