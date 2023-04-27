from tkinter import *

win = Tk()

win.title("Simple Caculator")

e = Entry(win,width=45,borderwidth=5)
e.grid(row = 0 ,column= 0,columnspan= 3, padx= 10 , pady= 10)

def button_click(number):
    e.insert(END, str(number))

def button_clear():
    e.delete(0,END)
    
def button_add():
    truoc = int(e.get())
    e.delete(0, END)
    sau = int(e.get())
    sum = truoc + sau
    e.insert(END, str(sum))
    
    
    

Button7 = Button(win,text="7",width=12,height=4,command=lambda: button_click(7))
Button8 = Button(win,text="8",width=12,height=4,command=lambda: button_click(8))
Button9 = Button(win,text="9",width=12,height=4,command=lambda: button_click(9))

Button4 = Button(win,text="4",width=12,height=4,command=lambda: button_click(4))
Button5 = Button(win,text="5",width=12,height=4,command=lambda: button_click(5))
Button6 = Button(win,text="6",width=12,height=4,command=lambda: button_click(6))

Button1 = Button(win,text="1",width=12,height=4,command=lambda: button_click(1))
Button2 = Button(win,text="2",width=12,height=4,command=lambda: button_click(2))
Button3 = Button(win,text="3",width=12,height=4,command=lambda: button_click(3))

Button0 = Button(win,text="0",width=12,height=4,command=lambda: button_click(0))
Button_clear = Button(win,text="Clear",width=26,height=4,command=button_clear)
Button_add = Button(win,text="+",width=12,height=4,command=button_add)
Button_equal = Button(win,text="=",width=26,height=4,command=lambda: button_click())


Button7.grid(row= 1,column= 0)
Button8.grid(row= 1,column= 1)
Button9.grid(row= 1,column= 2)

Button4.grid(row= 2,column= 0)
Button5.grid(row= 2,column= 1)
Button6.grid(row= 2,column= 2)

Button1.grid(row= 3,column= 0)
Button2.grid(row= 3,column= 1)
Button3.grid(row= 3,column= 2)

Button0.grid(row= 4,column= 0)
Button_clear.grid(row=4,column=1,columnspan=2)
Button_add.grid(row=5,column=0)
Button_equal.grid(row=5,column=1,columnspan=2)

# win.geometry("500x500")



win.mainloop()