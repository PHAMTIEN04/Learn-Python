import sys
from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Message Boxes")
win.geometry("500x500")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    rpmes = messagebox.askyesno("This is my Popup!", "Hello World")  # Syntax: messagebox.<method>(<title>, <content>)
    Label(win, text=rpmes).pack()
    if rpmes == "ok" or rpmes == "yes" or rpmes == 1: # Check if the user clicked "yes"
        Label(win, text="You clicked " + str(rpmes)).pack()
    else:
        sys.exit()  # Exit the program if the user clicked "no"
        
bt = Button(win, text="Popup", command=popup)
bt.pack()

win.mainloop()





win.mainloop()
