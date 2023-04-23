from tkinter import *
def mysum():
    x = mylabel_i1.get()
    y = mylabel_i2.get()
    sum = int(x) + int(y)
    mycheck = Label(win,text=str(sum))
    mycheck.pack()

win = Tk()

win.geometry("1000x700")
label1 = Label(win,text="Nhập số ")
label1.pack()
mylabel_i1 = Entry(win)
mylabel_i1.pack()
mylabel_i2 = Entry(win)
mylabel_i2.pack()

mylabel1 = Button(win,text="Enter",command= mysum)
mylabel1.pack()


win.mainloop()