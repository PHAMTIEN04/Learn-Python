
from tkinter import *
from PIL import Image,ImageTk


root = Tk()
root.geometry("200x200")
filepath = "D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/hinhtron.png"
img = Image.open(filepath)
img = img.resize((100,100), Image.ADAPTIVE)
img = ImageTk.PhotoImage(img)
lb = Label(root,image=img)
lb.pack()


root.mainloop()
