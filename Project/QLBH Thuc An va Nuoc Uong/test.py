from tkinter import *
from tkinter import filedialog

win = Tk()
# def a():
#     if v.get()=="t":
#         my = Label(win,text=v.get())
#         my.pack()
# v = StringVar()
# v.set(" ")
# r = Radiobutton(win,text="MONO",variable=v,value="t")
# r.pack()
# rt = Button(win,text="Xác nhận",command=a)
# rt.pack()

# def f():
#     win.filename = filedialog.askopenfilename(initialdir="D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong",title="Select File",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
#     lb = Label(win,text=win.filename)
#     lb.pack()
# a = Button(win,text="Click",command=f)
# a.pack()
win.geometry("300x300")
dt = StringVar()
dt.set(" ")
def o():

    choose_ta = Radiobutton(win,text="Thức Ăn",variable=dt,value="a")
    choose_ta.place(relx=0.2,rely=0.25)
    choose_nu = Radiobutton(win,text="Nước Uống",variable=dt,value="b")
    choose_nu.place(relx=0.2,rely=0.35)
bt = Button(win,text="Click",command=o)
bt.pack()
win.mainloop()