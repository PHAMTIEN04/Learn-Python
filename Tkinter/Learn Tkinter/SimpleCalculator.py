from tkinter import *

win = Tk()



def button_click(number):
    e.insert(END, str(number))

def button_ac():
    e.delete(0,END)
    
def button_del():
    e.delete(len(e.get())-1,END)


    
def button_add():
    global f_num
    global math 
    math = "addition"
    first_number = e.get()
    e.delete(0,END)
    f_num = int(first_number)
    e.delete(0,END)


def button_sub():
    global f_num
    global math 
    math = "sub"
    first_number = e.get()
    e.delete(0,END)
    f_num = int(first_number)
    e.delete(0,END)
    
def button_mul():
    global f_num
    global math 
    math = "mul"
    first_number = e.get()
    e.delete(0,END)
    f_num = int(first_number)
    e.delete(0,END)

def button_div():
    global f_num
    global math 
    math = "div"
    first_number = e.get()
    e.delete(0,END)
    f_num = int(first_number)
    e.delete(0,END)

    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    s_num = int(second_number)
    if math == "sub":
        e.insert(END,f_num - int(s_num))
    elif math == "addition":
        e.insert(END,f_num + int(s_num))
    elif math == "mul" :
        e.insert(END,f_num * int(s_num))
    elif math == "div" :
        e.insert(END,f_num / int(s_num))
        

        
win.title("Simple Caculator")
win.geometry
e = Entry(win,width=50,borderwidth=5)
e.grid(row = 0 ,column= 0,columnspan= 4, padx= 10 , pady= 10)    
    

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

Button_clearac = Button(win,text="AC",width=12,height=4,command=button_ac)
Button_cleardel = Button(win,text="Del",width=12,height=4,command=button_del)
Button_add = Button(win,text="+",width=12,height=4,command=button_add)
Button_sub = Button(win,text="-",width=12,height=4,command=button_sub)
Button_mul = Button(win,text="x",width=12,height=4,command=button_mul)
Button_div = Button(win,text="/",width=12,height=4,command=button_div)
Button_equal = Button(win,text="=",width=26,height=4,command=button_equal)

Button_add.grid(row=2,column=3,columnspan=1)
Button_sub.grid(row=3,column=3,columnspan=1)
Button_mul.grid(row=4,column=3,columnspan=1)
Button_div.grid(row=5,column=3,columnspan=1)

Button_cleardel.grid(row=1,column=2,columnspan=1)
Button_clearac.grid(row=1,column=3,columnspan=1)
Button_equal.grid(row=5,column=1,columnspan=2)

Button7.grid(row= 2,column= 0)
Button8.grid(row= 2,column= 1)
Button9.grid(row= 2,column= 2)

Button4.grid(row= 3,column= 0)
Button5.grid(row= 3,column= 1)
Button6.grid(row= 3,column= 2)

Button1.grid(row= 4,column= 0)
Button2.grid(row= 4,column= 1)
Button3.grid(row= 4,column= 2)

Button0.grid(row= 5,column= 0)


# win.geometry("500x500")



win.mainloop()