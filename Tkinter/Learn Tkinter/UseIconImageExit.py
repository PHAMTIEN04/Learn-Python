from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("Pham Phuoc Tien")

win.geometry("1000x700")
# Set the icon for the window
win.iconbitmap("D:/Learn Python/Tkinter/Learn Tkinter/Favicon/favicon.ico")

# Load the image
my_img = ImageTk.PhotoImage(Image.open("D:/Learn Python/Tkinter/Learn Tkinter/Image/2.jpg"))

# Create a label and display the image
my_label = Label(win, image=my_img,width=1000)
my_label.grid(column=0,row= 0,columnspan=5,padx=10,pady=10)

# Create the "Enter" button with the loaded image and quit the window on click
Button1 = Button(win,text="Enter",  command=win.quit)
Button1.grid(column=0,row=1)

# Create the "Exit" button and quit the window on click
Buttonexit = Button(win, text="Exit", command=win.quit)
Buttonexit.grid(column=4,row = 1)

win.mainloop()
