import sys
from tkinter import *
from tkinter import messagebox
from random import choice
while True:
    win = Tk()
    win.title("WARNNG!!!")
    win.geometry("300x200")
    win.iconbitmap("D:/Learn Python/Tkinter/Exercise Tkinter/Message Boxes Basic/favicon.ico")
    win["bg"] = "#BFEFFF"
    def warning():
        while True:
            messagebox.showwarning("WARNING!!!","warning cannot be turned off")
  



    b_my = Button(win,text="Click Me !",width=10,height=5,border=5,bg="#FF0000",fg="black",font=10,command=warning)
    b_my.pack(pady=50)



    win.mainloop()