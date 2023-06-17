import random
from tkinter import *


win = Tk()

text1= Label(win,text="Account :")
text1.grid(column=0,row= 0,padx = 10,pady=10)
input_pass = Entry(win,border=2)
input_pass.grid(column=1,row=0)

text= Label(win,text="Password :")
text.grid(column=0,row= 1,padx=10)
input_pass = Entry(win,border=2)
input_pass.grid(column=1,row=1)

def checkpass():
    keyboard = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    keyboard_list = list(keyboard)
    password = input_pass.get()
    guess_pass = ''
    while True :
        guess_pass = random.choices(keyboard_list,k=len(password))
        print(guess_pass)
        if guess_pass == list(password) :
            text_pass = ''

            for i in guess_pass:
                text_pass = text_pass + i
            print("Susscess!!!")
            print("Password is :'",text_pass,"'",sep="",end="")
            break




Enter =Button(win,text="Login",width=5,height=2,border = 2,bg="red",fg="green",command=checkpass)
Enter.grid(column=1,row=2,pady =10)

win["bg"] = "blue"
win.geometry("259x150")






win.mainloop()