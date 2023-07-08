from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Create the main window
win = Tk()

def open():
    # Declare the img variable as global to access it outside the function
    global img

    # Open the file dialog to select a file
    win.filename = filedialog.askopenfilename(initialdir="C:/Users/phamp/OneDrive/Hình ảnh/Cuộn phim",
                                              title="Select A File",
                                              filetypes=(("png files", "*.png"), ("all files", "*.*")))

    # Display the selected file path in a label
    lb = Label(win, text=win.filename)
    lb.pack()

    # Open the image using PIL and create an ImageTk object
    img = ImageTk.PhotoImage(Image.open(win.filename))

    # Display the image in a label
    lb_img = Label(win, image=img)
    lb_img.pack()

# Create a button to trigger the "open" function
bt = Button(win, text="Click", command=open)
bt.pack()

# Start the main event loop
win.mainloop()
