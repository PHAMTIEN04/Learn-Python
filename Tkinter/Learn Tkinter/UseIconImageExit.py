from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("Pham Phuoc Tien")

# Set the icon for the window
win.iconbitmap("D:/Learn Python/Tkinter/Learn Tkinter/Favicon/favicon.ico")

# Load the image
my_img = ImageTk.PhotoImage(Image.open("D:/Learn Python/Tkinter/Learn Tkinter/Image/2.jpg"))

# Create a label and display the image
my_label = Label(win, image=my_img)
my_label.pack()

# Create the "Enter" button with the loaded image and quit the window on click
Button1 = Button(win, text="Enter", width=20, height=20, image=my_img, command=win.quit)
Button1.pack()

# Create the "Exit" button and quit the window on click
Buttonexit = Button(win, text="Exit", command=win.quit)
Buttonexit.pack()

win.mainloop()
