from tkinter import *
from PIL import Image, ImageTk

def create_circle_image(radius, color):
    width = radius * 2
    height = radius * 2
    image = Image.new("RGBA", (width, height))
    for y in range(height):
        for x in range(width):
            dx = abs(x - radius)
            dy = abs(y - radius)
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance <= radius:
                image.putpixel((x, y), color)
    return ImageTk.PhotoImage(image)

win = Tk()
win.title("Hình Tròn trong Tkinter")
win.geometry("300x300")

circle_radius = 100
circle_color = (0, 0, 0, 255)  # Màu đen

circle_image = create_circle_image(circle_radius, circle_color)

label = Label(win, image=circle_image, borderwidth=0, highlightthickness=0)
label.pack()

win.mainloop()
