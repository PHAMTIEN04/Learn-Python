from tkinter import *
from PIL import ImageTk, Image

i = 0
running = False  # Running/pause state
interval = 1000  # Time between images (ms)
image_width = 1000
image_height = 500

win = Tk()
win.iconbitmap("D:/Learn Python/Tkinter/Learn Tkinter/Favicon/favicon.ico")
win.geometry("1000x750")
win.title("View APP Basic")
image1 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/ashe.jpg"
image2 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/jhin.jpg"
image3 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/teemo.jpg"
image4 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/yasuo.jpg"
image5 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/poppy.jpg"
all_image = [image1, image2, image3, image4, image5]
def resize_image(img_path):
    img = Image.open(img_path)
    img = img.resize((image_width,image_height),Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)
    
def update_image():
    global i 
    lb_img = resize_image(all_image[i])
    my_label.config(image=lb_img)
    my_label.image = lb_img

def button_bf():
    global i 
    if i == 0:
        i = 4
    else:
        i = i-1
    update_image()

def button_af():
    global i
    if i == 4:
        i = 0
    else:
        i = i+1
    update_image()
def start_slideshow():
    global running
    running = True
    next_image()
    
def stop_slideshow():
    global running
    running = False

def next_image():
    if running:
        button_af()
        win.after(interval,next_image)




lb_img = resize_image(all_image[i])
my_label = Label(win, image=lb_img, width=image_width, height=image_height)
my_label.grid(column=0, row=0, columnspan=10)

# Image button before
bt_before_img = ImageTk.PhotoImage(Image.open("D:/Learn Python/Tkinter/Learn Tkinter/Image/before.png"))
button_before = Button(win, image=bt_before_img, command=button_bf)
button_before.grid(column=0, row=1)

# Image button after
bt_after_img = ImageTk.PhotoImage(Image.open("D:/Learn Python/Tkinter/Learn Tkinter/Image/after.png"))
button_after = Button(win, image=bt_after_img, command=button_af)
button_after.grid(column=9, row=1)

# Start button
button_start = Button(win, text="Start", command=start_slideshow)
button_start.grid(column=4, row=1)

# Stop button
button_stop = Button(win, text="Stop", command=stop_slideshow)
button_stop.grid(column=5, row=1)

win.mainloop()