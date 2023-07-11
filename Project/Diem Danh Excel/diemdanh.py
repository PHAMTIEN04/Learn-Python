from tkinter import *

win = Tk()
win.geometry("735x450")
lb_f = LabelFrame(win)
lb_f.grid(padx=10,pady=20)

lb_f1 = LabelFrame(lb_f)
lb_f1.grid(rowspan=3,columnspan= 9,column=4,row=1,sticky="nsew")

lb = Label(lb_f,text="",width=100)
lb.grid(columnspan=12,row=0,column=0)

lb_e = Entry(lb_f,width=30,border=5)
lb_e.grid(columnspan=2,row=1,column=0,padx=10)

bt_e = Button(lb_f,text="Enter",border=3,width=5)
bt_e.grid(columnspan=4,column=1,row=1)

bt_all = Button(lb_f,text="Button1",width=25,height=5)
bt_all.grid(columnspan=2,row=2,column=0,pady=50)

bt_q = Button(lb_f,text="Button2",width=25,height=5)
bt_q.grid(columnspan=2,row=3,column=0,pady=40)












win.mainloop()