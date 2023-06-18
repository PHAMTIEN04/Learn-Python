from tkinter import *
from PIL import ImageTk, Image

def click_run():
    # Destroy the root window (win0) and create the main window (win) to display the slideshow
    win0.destroy()
    
    def resize_image(path_img, width, height):
        # Open the image and resize it to the desired dimensions
        img = Image.open(path_img)
        img = img.resize((width, height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)

    def update_image():
        nonlocal i
        # Update the image label with the current image
        lb_img = resize_image(all_image[i], image_width, image_height)
        my_label.config(image=lb_img)
        my_label.image = lb_img

    def button_bf():
        nonlocal i
        # Move to the previous image in the list
        if i == 0:
            i = 4
        else:
            i = i - 1 

        name_label.config(text=name_labels[i])
        count_label.config(text="Image "+str(i+1)+ " of "+str(len(name_labels)))
        update_image()

    def button_af():
        nonlocal i
        # Move to the next image in the list
        if i == 4:
            i = 0
        else:
            i = i + 1
        name_label.config(text=name_labels[i])
        count_label.config(text="Image "+str(i+1)+ " of "+str(len(name_labels)))
        update_image()

    def start_slideshow():
        nonlocal running
        # Start the slideshow
        running = True
        next_image()

    def stop_slideshow():
        nonlocal running
        # Pause the slideshow
        running = False

    def next_image():
        if running:
            # Move to the next image and schedule the next update
            button_af()
            win.after(interval, next_image)

    # Main window
    win = Tk()
    win.iconbitmap("D:/Learn Python/Tkinter/Learn Tkinter/Favicon/favicon.ico")
    win.geometry("1000x750")
    win.title("View APP Basic LOL")
    win["bg"] = "#DDDDDD"
    # Configuration variables
    i = 0  # Current image index
    running = False  # Running/pause state
    interval = 1000  # Time between images (ms)
    image_width = 1000
    image_height = 450
    image_width_b = 100
    image_height_b = 100

    # Image paths
    image1 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/ashe.jpg"
    image2 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/jhin.jpg"
    image3 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/teemo.jpg"
    image4 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/yasuo.jpg"
    image5 = "D:/Learn Python/Tkinter/Learn Tkinter/Image/poppy.jpg"
    all_image = [image1, image2, image3, image4, image5]

    # Image label
    lb_img = resize_image(all_image[i], image_width, image_height)
    my_label = Label(win, image=lb_img, width=image_width, height=image_height)
    my_label.grid(column=0, row=0, columnspan=10)

    # Image button before
    bt_before_img = resize_image("D:/Learn Python/Tkinter/Learn Tkinter/Image/before.png", image_width_b, image_height_b)
    button_before = Button(win, image=bt_before_img, border=5,command=button_bf)
    button_before.grid(column=0, row=2,pady=40)

    # Image button after
    bt_after_img = resize_image("D:/Learn Python/Tkinter/Learn Tkinter/Image/after.png", image_width_b, image_height_b)
    button_after = Button(win, image=bt_after_img,border=5, command=button_af)
    button_after.grid(column=9, row=2,pady=40)

    # Start button
    button_start = Button(win, text="Start", bg="green", fg="white",border=2, width=7, height=3, command=start_slideshow)
    button_start.grid(column=3, row=2)

    # Stop button
    button_stop = Button(win, text="Stop", bg="green", fg="white",border=2, width=7, height=3, command=stop_slideshow)
    button_stop.grid(column=7, row=2)

    # Exit button
    button_exit = Button(win, text="Exit", bg="red", fg="white", border=2,width=10, height=3, command=exit)
    button_exit.grid(column=5, row=3)

    # Name label
    name_labels = ["Ashe", "Jhin", "Teemo", "Yasuo", "Poppy"]
    name_label = Label(win, text=name_labels[i], width=20, height=3, fg="#DD0000", border=20,font=20)
    name_label.grid(column=5, row=2)

    # Count Image
    count_label = Label(win,text="Image "+str(i+1)+ " of "+str(len(name_labels)),bd=1,relief=SUNKEN)
    # count_label = Label(win,text="Image "+str(i+1)+ " of "+str(len(name_labels)),bd=1,relief=SUNKEN,anchor=E)
    # count_label.grid(column=0,row=4,columnspan=10,sticky=W+E,padx=30)
    # relief=SUNKEN sets the visibility of the border to "SUNKEN", which means hide inside the label.
    # anchor=E sets the anchor position of the text in the label to East.
    
    # sticky=W+E sets the sticky label to the West (West) and East (East) of its grid cell. This helps the label to expand horizontally when the window is expanded or minimized.
    # count_label.grid(column=0, row=4, columnspan=10, sticky=W+E, padx=30)
    count_label.grid(column=9,row=4,columnspan=10,padx=30)
    
    win.mainloop()

# Root window
win0 = Tk()
win0.title("Run Programme")
win0.geometry("200x200")
win0["bg"] = "#DDDDDD"
# Run button
Button_click_run = Button(win0, text="Run Programme",border=5,fg="black", bg="#33FFFF",command=click_run)
Button_click_run.grid(column=1, row=0,padx=50,pady=30)

# Exit button
button_no_click_run = Button(win0, text="Exit Programme",border=5,fg="black",bg="#FF0000", command=win0.quit)
button_no_click_run.grid(column=1, row=1,padx=50,pady=30)

win0.mainloop()
