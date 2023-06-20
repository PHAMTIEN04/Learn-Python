from tkinter import *

win = Tk()

win.title("Frames")
win.iconbitmap("D:/Learn Python/Tkinter/Learn Tkinter/Favicon/favicon.ico")

# Create a labeled frame with padding
Frammes = LabelFrame(win, padx=100, pady=100)
Frammes.grid(padx=50, pady=55)

# Create a button inside the labeled frame
b = Button(Frammes, text="Click!!!!")
b.grid(column=0, row=0)

# Create another button inside the labeled frame
b2 = Button(Frammes, text="YAHHHH")
b2.grid(column=1, row=1)

win.mainloop()
