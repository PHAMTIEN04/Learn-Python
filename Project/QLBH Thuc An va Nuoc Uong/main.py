from tkinter import *

win = Tk()
win.title("Quản Lý Bán Hàng")
win.geometry("1200x700+200+20")
labe_nen = Label(win,text="",bg="gray",width=40,height=60)
labe_nen.grid(column=0,rowspan=13)

label_test = Label(win,text="Test Font",fg="white",bg="gray")
label_test.grid(column=0,row=0,rowspan=1,sticky="N W")

label_test1 = Label(win,text="Test Font1",fg="white",bg="gray")
label_test1.grid(column=0,row=0,rowspan=1,sticky="N W",pady=30)








win.mainloop()


