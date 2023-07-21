import random
import os
from time import sleep
from tkinter import *
from PIL import Image,ImageTk

win = Tk()
def resize_img(path,width,height):
    img = Image.open(path)
    img = img.resize((width,height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)
width = 60
height = 60
img_bau = "./bau.jpg"
img_cua = "./cua.jpg"
img_tom= "./tom.jpg"
img_ca = "./ca.jpg"
img_ga = "./ga.jpg"
img_nai = "./nai.jpg"

width_m = 70
height_m = 20

img_50k = "./50k.jpg"
img_100k = "./100k.jpg"
img_500k = "./500k.jpg"

rs_50k = resize_img(path=img_50k,width=width_m,height=height_m)
rs_100k = resize_img(path=img_100k,width=width_m,height=height_m)
rs_500k = resize_img(path=img_500k,width=width_m,height=height_m)


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

animal_bet = []
global check_money
tien_nai = 0
def click_nai():
    global check
    check.append("nai")
    global check_money
    
    global money_nai50
    global money_nai100
    global money_nai500
    global sodu
    global tien_nai
    money_nai50 = Label(win,text="",image=rs_50k)
    money_nai100 = Label(win,text="",image=rs_100k)
    money_nai500 = Label(win,text="",image=rs_500k)
    if check_money == 50000 :
        
        if sodu >= check_money:
            money_nai50.grid(column=1,row=2)
            animal_bet.append(money_nai50)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_nai = tien_nai + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 100000 :

        if sodu >= check_money:
            money_nai100.grid(column=1,row=2)
            animal_bet.append(money_nai100)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_nai = tien_nai + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 500000 :

        if sodu >= check_money:
            money_nai500.grid(column=1,row=2)
            animal_bet.append(money_nai500)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_nai = tien_nai + check_money
        else:
            print("Hết Tiền")
        win.update()
    check_money = 0
tien_bau = 0
def click_bau():
    global check
    check.append("bau")
    global check_money
    global money_bau50
    global money_bau100
    global money_bau500
    global sodu
    global tien_bau
    money_bau50 = Label(win,text="",image=rs_50k)
    money_bau100 = Label(win,text="",image=rs_100k)
    money_bau500 = Label(win,text="",image=rs_500k)
    if check_money == 50000 :

        if sodu >= check_money:
            money_bau50.grid(column=2,row=2)
            animal_bet.append(money_bau50)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_bau = tien_bau + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 100000 :

        if sodu >= check_money:
            money_bau100.grid(column=2,row=2)
            animal_bet.append(money_bau100)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_bau = tien_bau + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 500000 :

        if sodu >= check_money:
            money_bau500.grid(column=2,row=2)
            animal_bet.append(money_bau500)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_bau = tien_bau + check_money
        else:
            print("Hết Tiền")
        win.update()
    check_money = 0
tien_ga = 0
def click_ga():
    global check
    check.append("ga")
    global check_money
    global money_ga50
    global money_ga100
    global money_ga500
    global sodu
    global tien_ga
    money_ga50 = Label(win,text="",image=rs_50k)
    money_ga100 = Label(win,text="",image=rs_100k)
    money_ga500 = Label(win,text="",image=rs_500k)
    if check_money == 50000 :
        
        if sodu >= check_money:
            money_ga50.grid(column=3,row=2)
            animal_bet.append(money_ga50)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_ga = tien_ga + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 100000 :

        if sodu >= check_money:
            money_ga100.grid(column=3,row=2)
            animal_bet.append(money_ga100)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_ga = tien_ga + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 500000 :
        
        if sodu >= check_money:
            money_ga500.grid(column=3,row=2)
            animal_bet.append(money_ga500)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_ga = tien_ga + check_money
        else:
            print("Hết Tiền")
        win.update()
    check_money = 0
tien_ca = 0
def click_ca():
    global check
    check.append("ca")
    global check_money
    global money_ca50
    global money_ca100
    global money_ca500
    global sodu
    global tien_ca
    money_ca50 = Label(win,text="",image=rs_50k)
    money_ca100 = Label(win,text="",image=rs_100k)
    money_ca500 = Label(win,text="",image=rs_500k)
    if check_money == 50000 :
        
        if sodu >= check_money:
            money_ca50.grid(column=1,row=3)
            animal_bet.append(money_ca50)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_ca = tien_ca + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 100000 :
        
        if sodu >= check_money:
            money_ca100.grid(column=1,row=3)
            animal_bet.append(money_ca100)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_ca = tien_ca + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 500000 :
        
        if sodu >= check_money:
            money_ca500.grid(column=1,row=3)
            animal_bet.append(money_ca500)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_ca = tien_ca + check_money
        else:
            print("Hết Tiền")   
        win.update()
    check_money = 0
tien_cua = 0
def click_cua():
    global check
    check.append("cua")
    global check_money
    global money_cua50
    global money_cua100
    global money_cua500
    global sodu
    global tien_cua
    money_cua50 = Label(win,text="",image=rs_50k)
    money_cua100 = Label(win,text="",image=rs_100k)
    money_cua500 = Label(win,text="",image=rs_500k)
    if check_money == 50000 :
        
        if sodu >= check_money:
            money_cua50.grid(column=2,row=3)
            animal_bet.append(money_cua50)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_cua = tien_cua + check_money
        else:
            print("Hết Tiền")   
        win.update()
    if check_money == 100000 :
        
        if sodu >= check_money:
            money_cua100.grid(column=2,row=3)
            animal_bet.append(money_cua100)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_cua = tien_cua + check_money
        else:
            print("Hết Tiền")   
        win.update()
    if check_money == 500000 :
        
        if sodu >= check_money:
            money_cua500.grid(column=2,row=3)
            animal_bet.append(money_cua500)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_cua = tien_cua + check_money
        else:
            print("Hết Tiền")   
        win.update()
    check_money = 0
tien_tom = 0
def click_tom():
    global check
    check.append("tom")
    global check_money
    global money_tom50
    global money_tom100
    global money_tom500
    global sodu
    global tien_tom
    money_tom50 = Label(win,text="",image=rs_50k)
    money_tom100 = Label(win,text="",image=rs_100k)
    money_tom500 = Label(win,text="",image=rs_500k)
    if check_money == 50000 :
        
        if sodu >= check_money:
            money_tom50.grid(column=3,row=3)
            animal_bet.append(money_tom50)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_tom = tien_tom + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 100000 :
        
        if sodu >= check_money:
            money_tom100.grid(column=3,row=3)
            animal_bet.append(money_tom100)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_tom = tien_tom + check_money
        else:
            print("Hết Tiền")
        win.update()
    if check_money == 500000 :
        
        if sodu >= check_money:
            money_tom500.grid(column=3,row=3)
            animal_bet.append(money_tom500)
            sodu = sodu - check_money
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            tien_tom = tien_tom + check_money
        else:
            print("Hết Tiền")
        win.update()
    check_money = 0

def click_50k():
    global check_money 
    check_money = 50000
    
def click_100k():
    global check_money 
    check_money = 100000

def click_500k():
    global check_money 
    check_money = 500000
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


    

    
list_check = []    

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
    global sodu
    global tien_tom
    global tien_nai
    global tien_bau
    global tien_ca
    global tien_cua
    global tien_ga
    if r_a == resize_b or r_b == resize_b or r_c == resize_b:
        a_b = resize_b
        a_b = "bau"
        if a_b in check:
            list_check.append(money_bau50)
            list_check.append(money_bau100)
            list_check.append(money_bau500)
            sodu = sodu + (tien_bau * 2)
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            print("Thang Bau")
    tien_bau = 0
    if r_a == resize_c or r_b == resize_c or r_c == resize_c:
        a_c = resize_c
        a_c = "cua"
        if a_c in check:
            list_check.append(money_cua50)
            list_check.append(money_cua100)
            list_check.append(money_cua500)
            sodu = sodu + (tien_cua * 2)
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            print("Thang Cua")
    tien_cua = 0
    if r_a == resize_t or r_b == resize_t or r_c == resize_t:
        a_t = resize_t
        a_t = "tom"
        if a_t in check:
            list_check.append(money_tom50)
            list_check.append(money_tom100)
            list_check.append(money_tom500)
            sodu = sodu + (tien_tom * 2)
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            print("Thang Tom")
    tien_tom = 0
    if r_a == resize_ca or r_b == resize_ca or r_c == resize_ca:
        a_ca = resize_ca
        a_ca = "ca"
        if a_ca in check:
            list_check.append(money_ca50)
            list_check.append(money_ca100)
            list_check.append(money_ca500)
            sodu = sodu + (tien_ca * 2)
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            print("Thang Ca")
    tien_ca = 0
    if r_a == resize_g or r_b == resize_g or r_c == resize_g:
        a_g = resize_g
        a_g = "ga"
        if a_g in check:
            list_check.append(money_ga50)
            list_check.append(money_ga100)
            list_check.append(money_ga500)
            sodu = sodu + (tien_ga * 2)
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            print("Thang Ga")
    tien_ga = 0
    if r_a == resize_n or r_b == resize_n or r_c == resize_n:
        a_n = resize_n
        a_n = "nai"
        if a_n in check:
            list_check.append(money_nai50)
            list_check.append(money_nai100)
            list_check.append(money_nai500)
            print("Thang Nai")
            sodu = sodu + (tien_nai * 2)
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
    tien_nai = 0
    check = []
    
    
    
def run():

    global list_n
    update_rand(lb_1,lb_2,lb_3)
    for widget in animal_bet:
        if widget not in list_check :
            widget.grid_remove()

    win.update()

    
def tinhtien():
    for widget in animal_bet:
        widget.grid_remove()
    global tien_bau,tien_ca,tien_cua,tien_ga,tien_nai,tien_tom
    tien_bau = 0
    tien_ca = 0
    tien_cua = 0
    tien_ga = 0
    tien_nai = 0
    tien_tom = 0
    list_check.clear()
    animal_bet.clear()
    win.update()

def naptien():
    global wnt
    global e_nt
    wnt = Toplevel()
    wnt["bg"] = "red"
    wnt.geometry("200x70")
    lb_nt = Label(wnt,text="Nhập số tiền cần nạp",bg="red")
    lb_nt.grid(column=0,row=0)
    e_nt = Entry(wnt,border=5)
    e_nt.grid(column=0,row=1,padx=5)
    nt_click = Button(wnt,text="Nạp",command=v_t)
    nt_click.grid(column=1,row=1)
def v_t():
    global sodu
    sodu = sodu + int(e_nt.get())
    l_sodu.config(text=f"Số dư : {sodu} vnđ")
    wnt.destroy()
        
bt = Button(win,text="Run",command=run)
bt.grid(column=2,row=1)

lb_money = Label(win,text="Chọn số tiền đặt cược :",bg="red",font=("Arial", 12, "bold"))
lb_money.grid(column=1,row=4,columnspan=1)


money_50k = Button(win,text="1",image=rs_50k,command=click_50k)
money_50k.grid(column=1,row=5,pady=10)

money_100k = Button(win,text="1",image=rs_100k,command=click_100k)
money_100k.grid(column=2,row=5,pady=10)

money_500k = Button(win,text="1",image=rs_500k,command=click_500k)
money_500k.grid(column=3,row=5,pady=10)

win1 = Toplevel()
win1["bg"] = "red"
win1.geometry("250x250")
sodu = 0
# Label for displaying the balance.
l_sodu = Label(win1, text=f"Số dư : {sodu} vnđ", font=("Arial", 12, "bold"))
l_sodu.grid(column=0, row=0, pady=10, columnspan=2, sticky="w")

# Button to 'Nạp Tiền'.
bt_nt = Button(win1, text="Nạp Tiền", font=("Arial", 12, "bold"), command=naptien)
bt_nt.grid(column=1, row=1, padx=10, pady=10, sticky="e")

# Button to 'Tính Tiền'.
bt_tt = Button(win1, text="Chơi Tiếp", font=("Arial", 12, "bold"), command=tinhtien)
bt_tt.grid(column=0, row=1, padx=20, pady=10, sticky="w")


win.mainloop()