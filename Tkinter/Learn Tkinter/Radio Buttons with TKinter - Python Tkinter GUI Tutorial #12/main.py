from tkinter import *

win = Tk()

win.title("Radio Buttons")

# StringVar for the first group of radio buttons
r = StringVar()
r.set(" ")

# StringVar for the second group of radio buttons
r1 = StringVar()
r1.set("1")

def click(value):
    global mylabel
    mylabel.pack_forget()
    mylabel.destroy()
    mylabel = Label(win, text=value)
    mylabel.pack()

Topping = [
    ("Pizza", "Shushi"),
    ("EGG", "Sugar"),
    ("Origane", "Blue")
]

pz = StringVar()
pz.set("Pizza")

# Create radio buttons for the Topping group
for text, top in Topping:
    Radiobutton(win, text=text, variable=pz, value=top, command=lambda: click(pz.get())).pack()

# Create radio buttons for the Option group
Radiobutton(win, text="Option 1", variable=r, value="1", command=lambda: click(r.get())).pack()
Radiobutton(win, text="Option 2", variable=r, value="4", command=lambda: click(r.get())).pack()

Labelchoose = Label(win, text="Choose")
Labelchoose.pack()

mylabel = Label(win, text=r.get())
mylabel.pack()

win.mainloop()
