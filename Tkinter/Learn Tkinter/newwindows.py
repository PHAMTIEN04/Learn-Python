from tkinter import *

win = Tk()
win.title("Windows First")
win.geometry("200x100")

def open():
    top = Toplevel() # Create New Windows
    # top use as win
    top.title("Windows Second") 
    top.geometry("200x100")
    Label(top,text="FUCK YOU!!!").pack()
    bt1 = Button(top,text="Exit",command=top.destroy)
    bt1.pack()
    
bt = Button(win,text="Click",command=open)
bt.pack()


win.mainloop()
