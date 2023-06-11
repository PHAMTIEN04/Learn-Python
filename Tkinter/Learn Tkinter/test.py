from tkinter import *

win = Tk()
# win.geometry("600x600")
Input = Entry(win,width=50,border=5)
Input.grid(column=0,row=0,columnspan=4, padx= 10 , pady= 10)

def buttonclick(num):
    Input.insert(END,str(num))

def buttonAC():
    Input.delete(0,END)

def buttonDel():
    Input.delete(len(Input.get())-1,END)
    
def buttonADD():
    global f_num
    global math 
    math = "ADD"
    first_num =Input.get()
    f_num = int(first_num)
    Input.delete(0,END)

def buttonSub():
    global f_num
    global math 
    math = "Sub"
    first_num =Input.get()
    f_num = int(first_num)
    Input.delete(0,END)

def buttonMul():
    global f_num
    global math 
    math = "Mul"
    first_num =Input.get()
    f_num = int(first_num)
    Input.delete(0,END)

def buttonDiv():
    global f_num
    global math 
    math = "Div"
    first_num =Input.get()
    f_num = float(first_num)
    Input.delete(0,END)
            
def buttonEqual():
    second_num = Input.get()
    s_num = int(second_num)
    Input.delete(0,END)
    if math == "ADD":
        Input.insert(END,f_num+s_num)
    elif math == "Sub":
        Input.insert(END,f_num-s_num)
    elif math == "Mul":
        Input.insert(END,f_num*s_num)
    elif math == "Div":
        Input.insert(END,float(f_num) / float(s_num))
        

ButtonEqual = Button(win,text = "=",height=4,width=45,command=buttonEqual)

ButtonADD = Button(win,text="+",width=10,height=4,command=buttonADD)
ButtonSub = Button(win,text="-",width=10,height=4,command=buttonSub)
ButtonMul = Button(win,text="x",width=10,height=4,command=buttonMul)
ButtonDiv = Button(win,text="/",width=10,height=4,command=buttonDiv)

ButtonAC= Button(win,text="AC",width=10,height=4,command=buttonAC)
ButtonDel = Button(win,text="Del",width=10,height=4,command=buttonDel)

Button7 = Button(win,text="7",width=10,height=4,command=lambda : buttonclick(7))
Button8 = Button(win,text="8",width=10,height=4,command=lambda : buttonclick(8))
Button9 = Button(win,text="9",width=10,height=4,command=lambda : buttonclick(9))

Button4 = Button(win,text="4",width=10,height=4,command=lambda : buttonclick(4))
Button5 = Button(win,text="5",width=10,height=4,command=lambda : buttonclick(5))
Button6 = Button(win,text="6",width=10,height=4,command=lambda : buttonclick(6))

Button1 = Button(win,text="1",width=10,height=4,command=lambda : buttonclick(1))
Button2 = Button(win,text="2",width=10,height=4,command=lambda : buttonclick(2))
Button3 = Button(win,text="3",width=10,height=4,command=lambda : buttonclick(3))

Button0 = Button(win,text="0",width=10,height=4,command=lambda : buttonclick(0))

ButtonEqual.grid(row=1,columnspan=4)

ButtonADD.grid(column=3,row=2)
ButtonSub.grid(column=3,row=3)
ButtonMul.grid(column=3,row=4)
ButtonDiv.grid(column=3,row=5)

ButtonAC.grid(column=2,row=5)
ButtonDel.grid(column=0,row = 5)

Button7.grid(column=0,row=2)
Button8.grid(column=1,row=2)
Button9.grid(column=2,row=2)

Button4.grid(column=0,row=3)
Button5.grid(column=1,row=3)
Button6.grid(column=2,row=3)

Button1.grid(column=0,row=4)
Button2.grid(column=1,row=4)
Button3.grid(column=2,row=4)

Button0.grid(column=1,row=5)
win.mainloop()