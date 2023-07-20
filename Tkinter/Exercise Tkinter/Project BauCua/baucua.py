import random
import os
from time import sleep
from tkinter import *
from PIL import Image,ImageTk

win = Tk()
def resize_img(path,width,height):
    img = Image.open(path)
    img = img.resize((width,height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)
width = 60
height = 60
img_bau = "D:/Learn Python/Tkinter/Exercise Tkinter/Project BauCua/bau.jpg"
img_cua = "D:/Learn Python/Tkinter/Exercise Tkinter/Project BauCua/cua.jpg"
img_tom= "D:/Learn Python/Tkinter/Exercise Tkinter/Project BauCua/tom.jpg"
img_ca = "D:/Learn Python/Tkinter/Exercise Tkinter/Project BauCua/ca.jpg"
img_ga = "D:/Learn Python/Tkinter/Exercise Tkinter/Project BauCua/ga.jpg"
img_nai = "D:/Learn Python/Tkinter/Exercise Tkinter/Project BauCua/nai.jpg"

width_m = 70
height_m = 20

img_100k = "D:/Learn Python/Tkinter/Exercise Tkinter/Project BauCua/100k.jpg"
rs_100k = resize_img(path=img_100k,width=width_m,height=height_m)


win.geometry("500x500")
win["bg"] = "red"

rs_b = resize_img(img_bau,width=width,height=height)
rs_c = resize_img(img_cua,width=width,height=height)
rs_t = resize_img(img_tom,width=width,height=height)
rs_ca = resize_img(img_ca,width=width,height=height)
rs_g = resize_img(img_ga,width=width,height=height)
rs_n = resize_img(img_nai,width=width,height=height)

lb_1 = Label(win,text="1",width=width,height=height,bg="white",image=rs_b)
lb_1.grid(column=1,row=0,padx=20,pady=10)

lb_2 = Label(win,text="1",width=width,height=height,bg="white",image=rs_c)
lb_2.grid(column=2,row=0,padx=20,pady=10)

lb_3 = Label(win,text="1",width=width,height=height,bg="white",image=rs_t)
lb_3.grid(column=3,row=0,padx=20,pady=10)
check = []

def click_nai():
    global check
    check.append("nai")
    global check_money
    global money_nai
    money_nai = Label(win,text="",image=rs_100k)
    if check_money == 100 :
        money_nai.grid(column=1,row=2)
        win.update()
        
def click_bau():
    global check
    check.append("bau")
    global money_bau
    money_bau = Label(win,text="",image=rs_100k)
    if check_money == 100 :
        money_bau.grid(column=2,row=2)
        win.update()
def click_ga():
    global check
    check.append("ga")
    global money_ga
    money_ga = Label(win,text="",image=rs_100k)
    if check_money == 100 :
        money_ga.grid(column=3,row=2)
        win.update()
def click_ca():
    global check
    check.append("ca")
    global money_ca
    money_ca = Label(win,text="",image=rs_100k)
    if check_money == 100 :
        money_ca.grid(column=1,row=3)
        win.update()
def click_cua():
    global check
    check.append("cua")
    global money_cua
    money_cua = Label(win,text="",image=rs_100k)
    if check_money == 100 :
        money_cua.grid(column=2,row=3)
        win.update()
def click_tom():
    global check
    check.append("tom")
    global money_tom
    money_tom = Label(win,text="",image=rs_100k)
    if check_money == 100 :
        money_tom.grid(column=3,row=3)
        win.update()

def click_100k():
    global check_money 
    check_money = 100
    
bt_nai = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_n,command=click_nai)
bt_nai.grid(column=1, row= 2,padx=20,pady=20)
bt_bau = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_b,command=click_bau)
bt_bau.grid(column=2, row= 2,pady=20)
bt_ga = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_g,command=click_ga)
bt_ga.grid(column=3, row= 2,padx=20,pady=20)

bt_ca = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_ca,command=click_ca)
bt_ca.grid(column=1, row= 3,padx=20,pady=20)
bt_cua = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_c,command=click_cua)
bt_cua.grid(column=2, row= 3,pady=20)
bt_tom = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_t,command=click_tom)
bt_tom.grid(column=3, row= 3,padx=20,pady=20)


    

    
    

def update_rand(label1,label2,label3):
    global check
    print(check)
    resize_b = resize_img(path=img_bau,width=width,height=height)
    resize_c = resize_img(path=img_cua,width=width,height=height)
    resize_t = resize_img(path=img_tom,width=width,height=height)
    resize_ca = resize_img(path=img_ca,width=width,height=height)
    resize_g = resize_img(path=img_ga,width=width,height=height)
    resize_n = resize_img(path=img_nai,width=width,height=height)

    list_a = [resize_b,resize_c,resize_t,resize_ca,resize_g,resize_n]
    cnt = 1
    while cnt <= 20 :
        r_a = random.choice(list_a)
        r_b = random.choice(list_a)
        r_c = random.choice(list_a)
        print(r_a,r_b,r_c)
        # os.system("cls")
        label1.config(image=r_a,width=width,height=height)
        label1.image = r_a
        label2.config(image=r_b,width=width,height=height)
        label2.image = r_b
        label3.config(image=r_c,width=width,height=height)
        label3.image = r_c
        win.update()
        cnt = cnt + 1
        sleep(0.1)
    if r_a == resize_b or r_b == resize_b or r_c == resize_b:
        a_b = resize_b
        a_b = "bau"
        if a_b in check:
            print("Thắng Bầu")
    if r_a == resize_c or r_b == resize_c or r_c == resize_c:
        a_c = resize_c
        a_c = "cua"
        if a_c in check:
            print("Thắng Cua")
    if r_a == resize_t or r_b == resize_t or r_c == resize_t:
        a_t = resize_t
        a_t = "tom"
        if a_t in check:
            print("Thắng Tôm")
    if r_a == resize_ca or r_b == resize_ca or r_c == resize_ca:
        a_ca = resize_ca
        a_ca = "ca"
        if a_ca in check:
            print("Thắng Cá")
    if r_a == resize_g or r_b == resize_g or r_c == resize_g:
        a_g = resize_g
        a_g = "ga"
        if a_g in check:
            print("Thắng Gà")
    if r_a == resize_n or r_b == resize_n or r_c == resize_n:
        a_n = resize_n
        a_n = "nai"
        if a_n in check:
            print("Thắng Nai")
    check = []
    
    
    
def run():
    global money_nai
    global money_bau
    global money_ga
    global money_ca
    global money_cua
    global money_tom
    update_rand(lb_1,lb_2,lb_3)
    money_nai.grid_remove()
    money_bau.grid_remove()
    money_ga.grid_remove()
    money_ca.grid_remove()
    money_cua.grid_remove()
    money_tom.grid_remove()
    win.update()
    
    


bt = Button(win,text="Run",command=run)
bt.grid(column=2,row=1)

lb_money = Label(win,text="Chọn số tiền đặt cược :",bg="red",font=("Arial", 12, "bold"))
lb_money.grid(column=1,row=4,columnspan=1)


money_100k = Button(win,text="1",image=rs_100k,command=click_100k)
money_100k.grid(column=1,row=5,pady=10)


win.mainloop()