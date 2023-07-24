import random
import os
from time import sleep
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pygame
import threading

win = Tk()

pygame.mixer.init()


pygame.mixer.music.load("./chaomung.mp3")
pygame.mixer.music.play(loops=1)


def play_other_music(file_path):
    # Phát âm thanh mới trên kênh 1 (không giới hạn lặp)
    sound = pygame.mixer.Sound(file_path)
    channel = pygame.mixer.Channel(1)
    channel.play(sound,loops=-1)

play_other_music("./nhacnen.mp3")


def resize_img(path,width,height): # Function Resize Image
    img = Image.open(path)
    img = img.resize((width,height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Width , Height
width = 70
height = 70

# Link Image bau,cua,tom,ca,ga,nai
img_bau = "./bau.jpg"
img_cua = "./cua.jpg"
img_tom= "./tom.jpg"
img_ca = "./ca.jpg"
img_ga = "./ga.jpg"
img_nai = "./nai.jpg"

# Link Image hop
img_hop = "./hop.jpg"

# Width , Height
width_m = 70
height_m = 20

# Link Image Money
img_50k = "./50k.jpg"
img_100k = "./100k.jpg"
img_500k = "./500k.jpg"

# Resize Image Money
rs_50k = resize_img(path=img_50k,width=width_m,height=height_m)
rs_100k = resize_img(path=img_100k,width=width_m,height=height_m)
rs_500k = resize_img(path=img_500k,width=width_m,height=height_m)

# Resize Image Hop
rs_hop = resize_img(path=img_hop,width=60,height=40)

win.geometry("520x600")
win["bg"] = "red"

win.title("Bầu Cua")
win.iconbitmap("./iconbaucua.ico")

# Resize Image Bau,cua,tom,ca,ga,nai
rs_b = resize_img(img_bau,width=width,height=height)
rs_c = resize_img(img_cua,width=width,height=height)
rs_t = resize_img(img_tom,width=width,height=height)
rs_ca = resize_img(img_ca,width=width,height=height)
rs_g = resize_img(img_ga,width=width,height=height)
rs_n = resize_img(img_nai,width=width,height=height)

# Label Random Default : Bau, Cua, Tom
lb_1 = Label(win,text="1",width=width,height=height,bg="white",image=rs_b)
lb_1.grid(column=1,row=0,padx=20,pady=10)
lb_2 = Label(win,text="1",width=width,height=height,bg="white",image=rs_c)
lb_2.grid(column=2,row=0,padx=20,pady=10)
lb_3 = Label(win,text="1",width=width,height=height,bg="white",image=rs_t)
lb_3.grid(column=3,row=0,padx=20,pady=10)

check = [] #list check names

animal_bet = [] #list containing names
global check_money

money_calculated = False # Check when starting the game must press the start button to play
sum_money = 0
check_sum_money = False # Check to see if you choose the right one, and if it is correct, the profit will be added

tien_nai = 0
def click_nai():
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    # Check if the money calculation has been performed
    if money_calculated == True:
        global check
        check.append("nai")
        global check_money
        global money_nai50
        global money_nai100
        global money_nai500
        global sodu
        global tien_nai
        global sum_money
        
        money_nai50 = Label(win,text="",image=rs_50k)
        money_nai100 = Label(win,text="",image=rs_100k)
        money_nai500 = Label(win,text="",image=rs_500k)
        
        # Check the selected bet amount and process accordingly
        if check_money == 50000 : 
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_nai50.grid(column=1,row=2)
                animal_bet.append(money_nai50)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_nai = tien_nai + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 100000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_nai100.grid(column=1,row=2)
                animal_bet.append(money_nai100)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_nai = tien_nai + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
        win.update()
        if check_money == 500000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_nai500.grid(column=1,row=2)
                animal_bet.append(money_nai500)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_nai = tien_nai + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        check_money = 0
    else:
        pygame.mixer.music.load("./canhbao1.mp3")
        pygame.mixer.music.play(loops=1)
        messagebox.showwarning("Cảnh báo","Vui lòng chọn bắt đầu trước khi đặt cược !!!",icon = messagebox.WARNING)
tien_bau = 0
def click_bau():
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    # Check if the money calculation has been performed
    if money_calculated == True:
        global check
        check.append("bau")
        global check_money
        global money_bau50
        global money_bau100
        global money_bau500
        global sodu
        global tien_bau
        global sum_money
        
        money_bau50 = Label(win,text="",image=rs_50k)
        money_bau100 = Label(win,text="",image=rs_100k)
        money_bau500 = Label(win,text="",image=rs_500k)
        # Check the selected bet amount and process accordingly
        if check_money == 50000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_bau50.grid(column=2,row=2)
                animal_bet.append(money_bau50)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_bau = tien_bau + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 100000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_bau100.grid(column=2,row=2)
                animal_bet.append(money_bau100)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_bau = tien_bau + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 500000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_bau500.grid(column=2,row=2)
                animal_bet.append(money_bau500)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_bau = tien_bau + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        check_money = 0
    else:
        pygame.mixer.music.load("./canhbao1.mp3")
        pygame.mixer.music.play(loops=1)
        messagebox.showwarning("Cảnh báo","Vui lòng chọn bắt đầu trước khi đặt cược !!!",icon = messagebox.WARNING)
tien_ga = 0
def click_ga():
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    # Check if the money calculation has been performed
    if money_calculated == True:
        global check
        check.append("ga")
        global check_money
        global money_ga50
        global money_ga100
        global money_ga500
        global sodu
        global tien_ga
        global sum_money
        
        money_ga50 = Label(win,text="",image=rs_50k)
        money_ga100 = Label(win,text="",image=rs_100k)
        money_ga500 = Label(win,text="",image=rs_500k)
        # Check the selected bet amount and process accordingly
        if check_money == 50000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_ga50.grid(column=3,row=2)
                animal_bet.append(money_ga50)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_ga = tien_ga + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 100000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_ga100.grid(column=3,row=2)
                animal_bet.append(money_ga100)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_ga = tien_ga + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 500000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_ga500.grid(column=3,row=2)
                animal_bet.append(money_ga500)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_ga = tien_ga + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        check_money = 0
    else:
        pygame.mixer.music.load("./canhbao1.mp3")
        pygame.mixer.music.play(loops=1)
        messagebox.showwarning("Cảnh báo","Vui lòng chọn bắt đầu trước khi đặt cược !!!",icon = messagebox.WARNING)
tien_ca = 0
def click_ca():
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    # Check if the money calculation has been performed
    if money_calculated == True:
        global check
        check.append("ca")
        global check_money
        global money_ca50
        global money_ca100
        global money_ca500
        global sodu
        global tien_ca
        global sum_money
        
        money_ca50 = Label(win,text="",image=rs_50k)
        money_ca100 = Label(win,text="",image=rs_100k)
        money_ca500 = Label(win,text="",image=rs_500k)
        # Check the selected bet amount and process accordingly
        if check_money == 50000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_ca50.grid(column=1,row=3)
                animal_bet.append(money_ca50)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_ca = tien_ca + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 100000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_ca100.grid(column=1,row=3)
                animal_bet.append(money_ca100)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_ca = tien_ca + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 500000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_ca500.grid(column=1,row=3)
                animal_bet.append(money_ca500)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_ca = tien_ca + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")   
            win.update()
        check_money = 0
    else: 
        pygame.mixer.music.load("./canhbao1.mp3")
        pygame.mixer.music.play(loops=1)
        messagebox.showwarning("Cảnh báo","Vui lòng chọn bắt đầu trước khi đặt cược !!!",icon = messagebox.WARNING)
tien_cua = 0
def click_cua():
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    # Check if the money calculation has been performed
    if money_calculated == True:
        global check
        check.append("cua")
        global check_money
        global money_cua50
        global money_cua100
        global money_cua500
        global sodu
        global tien_cua
        global sum_money
        
        money_cua50 = Label(win,text="",image=rs_50k)
        money_cua100 = Label(win,text="",image=rs_100k)
        money_cua500 = Label(win,text="",image=rs_500k)
        # Check the selected bet amount and process accordingly
        if check_money == 50000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_cua50.grid(column=2,row=3)
                animal_bet.append(money_cua50)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_cua = tien_cua + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")   
            win.update()
        if check_money == 100000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_cua100.grid(column=2,row=3)
                animal_bet.append(money_cua100)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_cua = tien_cua + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")   
            win.update()
        if check_money == 500000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_cua500.grid(column=2,row=3)
                animal_bet.append(money_cua500)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_cua = tien_cua + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")   
            win.update()
        check_money = 0
    else:
        pygame.mixer.music.load("./canhbao1.mp3")
        pygame.mixer.music.play(loops=1)
        messagebox.showwarning("Cảnh báo","Vui lòng chọn bắt đầu trước khi đặt cược !!!",icon = messagebox.WARNING)
tien_tom = 0
def click_tom():
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    # Check if the money calculation has been performed
    if money_calculated == True:
        global check
        check.append("tom")
        global check_money
        global money_tom50
        global money_tom100
        global money_tom500
        global sodu
        global tien_tom
        global sum_money
        money_tom50 = Label(win,text="",image=rs_50k)
        money_tom100 = Label(win,text="",image=rs_100k)
        money_tom500 = Label(win,text="",image=rs_500k)
        # Check the selected bet amount and process accordingly
        if check_money == 50000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_tom50.grid(column=3,row=3)
                animal_bet.append(money_tom50)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_tom = tien_tom + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 100000 :
            # Check if there is enough balance to place the bet
            if sodu >= check_money:
                money_tom100.grid(column=3,row=3)
                animal_bet.append(money_tom100)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_tom = tien_tom + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
            win.update()
        if check_money == 500000 :
            # Check if there is enough balance to place the bet     
            if sodu >= check_money:
                money_tom500.grid(column=3,row=3)
                animal_bet.append(money_tom500)
                sodu = sodu - check_money
                l_sodu.config(text=f"Số dư : {sodu} vnđ")
                tien_tom = tien_tom + check_money
                sum_money = sum_money - check_money
            else:
                pygame.mixer.music.load("./canhbao2.mp3")
                pygame.mixer.music.play(loops=1)
                messagebox.showwarning("Cảnh báo","Số dư không đủ..Vui lòng nạp tiền !")
                
            win.update()
        check_money = 0
    else:

        pygame.mixer.music.load("./canhbao1.mp3")
        pygame.mixer.music.play(loops=1)
        messagebox.showwarning("Cảnh báo","Vui lòng chọn bắt đầu trước khi đặt cược !!!",icon = messagebox.WARNING)

def click_50k(): # Function money 50k
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    global check_money 
    check_money = 50000
    
def click_100k(): # Function money 100k
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    global check_money 
    check_money = 100000

def click_500k(): # Function money 500k
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    global check_money 
    check_money = 500000


# Button nai,bau,ga,ca,cua,tom
bt_nai = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_n,command=click_nai,border=3)
bt_nai.grid(column=1, row= 2,padx=20,pady=20)
bt_bau = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_b,command=click_bau,border=3)
bt_bau.grid(column=2, row= 2,pady=20)
bt_ga = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_g,command=click_ga,border=3)
bt_ga.grid(column=3, row= 2,padx=20,pady=20)
bt_ca = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_ca,command=click_ca,border=3)
bt_ca.grid(column=1, row= 3,padx=20,pady=20)
bt_cua = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_c,command=click_cua,border=3)
bt_cua.grid(column=2, row= 3,pady=20)
bt_tom = Button(win,text="1",width=width+70,height=height+50,bg="white",image=rs_t,command=click_tom,border=3)
bt_tom.grid(column=3, row= 3,padx=20,pady=20)


    

    
list_check = []    

def update_rand(label1,label2,label3):
    global check
    
    # Load and resize the images for each animal
    resize_b = resize_img(path=img_bau,width=width,height=height)
    resize_c = resize_img(path=img_cua,width=width,height=height)
    resize_t = resize_img(path=img_tom,width=width,height=height)
    resize_ca = resize_img(path=img_ca,width=width,height=height)
    resize_g = resize_img(path=img_ga,width=width,height=height)
    resize_n = resize_img(path=img_nai,width=width,height=height)

    list_a = [resize_b,resize_c,resize_t,resize_ca,resize_g,resize_n]
    cnt = 1
    
    # Perform 20 random image changes to simulate dice rolling
    while cnt <= 20 :
        r_a = random.choice(list_a)
        r_b = random.choice(list_a)
        r_c = random.choice(list_a)
        # print(r_a,r_b,r_c)
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
        
    # Calculate winnings and update the balance        
    global sodu
    global tien_tom
    global tien_nai
    global tien_bau
    global tien_ca
    global tien_cua
    global tien_ga
    global check_sum_money
    global sum_money

    # Initialize variables for calculating winnings for each animal
    lai_b = 0
    lai_c = 0
    lai_ca = 0
    lai_ga = 0
    lai_t = 0
    lai_nai = 0
    count_b = 0
    multi_b = 0
    
    # Check if any of the images are "bau"
    if r_a == resize_b or r_b == resize_b or r_c == resize_b:
        check_sum_money = True
        if r_a == resize_b:
            count_b = count_b + 1
        if r_b == resize_b:
            count_b = count_b + 1
        if r_c == resize_b:
            count_b = count_b + 1
        if count_b == 1:
            multi_b = 2
        if count_b == 2:
            multi_b = 3 
        if count_b == 3:
            multi_b = 4
        
        # Calculate winnings for "bau" bets
        a_b = resize_b
        a_b = "bau"
        if a_b in check:
            list_check.append(money_bau50)
            list_check.append(money_bau100)
            list_check.append(money_bau500)
            lai_b = tien_bau * multi_b
            sodu = sodu + lai_b
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            # print("Thang Bau")
    # If there are winnings, update the total bet amount
    if check_sum_money == True:
        sum_money = sum_money + lai_b
        check_sum_money = False
    tien_bau = 0
    count_c = 0
    multi_c = 0
    
    # Check if any of the images are "cua"
    if r_a == resize_c or r_b == resize_c or r_c == resize_c:
        check_sum_money = True
        if r_a == resize_c:
            count_c = count_c + 1
        if r_b == resize_c:
            count_c = count_c + 1
        if r_c == resize_c:
            count_c = count_c + 1
        if count_c == 1:
            multi_c = 2
        if count_c == 2:
            multi_c = 3 
        if count_c == 3:
            multi_c = 4
        # Calculate winnings for "cua" bets
        a_c = resize_c
        a_c = "cua"
        if a_c in check:
            list_check.append(money_cua50)
            list_check.append(money_cua100)
            list_check.append(money_cua500)
            lai_c = tien_cua * multi_c
            sodu = sodu + lai_c
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            # print("Thang Cua")
    # If there are winnings, update the total bet amount
    if check_sum_money == True:
        sum_money = sum_money + lai_c
        check_sum_money = False
    tien_cua = 0
    count_t = 0
    multi_t = 0
    
    # Check if any of the images are "tom"
    if r_a == resize_t or r_b == resize_t or r_c == resize_t:
        check_sum_money = True
        if r_a == resize_t:
            count_t = count_t + 1
        if r_b == resize_t:
            count_t = count_t + 1
        if r_c == resize_t:
            count_t = count_t + 1
        if count_t == 1:
            multi_t = 2
        if count_t == 2:
            multi_t = 3 
        if count_t == 3:
            multi_t = 4
        # Calculate winnings for "tom" bets
        a_t = resize_t
        a_t = "tom"
        if a_t in check:
            list_check.append(money_tom50)
            list_check.append(money_tom100)
            list_check.append(money_tom500)
            lai_t = tien_tom * multi_t
            sodu = sodu + lai_t
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            # print("Thang Tom")
    # If there are winnings, update the total bet amount
    if check_sum_money == True:
        sum_money = sum_money + lai_t
        check_sum_money = False
    tien_tom = 0
    count_ca = 0
    multi_ca = 0
    
    # Check if any of the images are "ca"
    if r_a == resize_ca or r_b == resize_ca or r_c == resize_ca:
        check_sum_money = True
        if r_a == resize_ca:
            count_ca = count_ca + 1
        if r_b == resize_ca:
            count_ca = count_ca + 1
        if r_c == resize_ca:
            count_ca = count_ca + 1
        if count_ca == 1:
            multi_ca = 2
        if count_ca == 2:
            multi_ca = 3 
        if count_ca == 3:
            multi_ca = 4
        # Calculate winnings for "ca" bets
        a_ca = resize_ca
        a_ca = "ca"
        if a_ca in check:
            list_check.append(money_ca50)
            list_check.append(money_ca100)
            list_check.append(money_ca500)
            lai_ca = tien_ca * multi_ca
            sodu = sodu + lai_ca
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            # print("Thang Ca")
    # If there are winnings, update the total bet amount
    if check_sum_money == True:
        sum_money = sum_money + lai_ca
        check_sum_money = False
    tien_ca = 0
    count_ga = 0
    multi_ga = 0
    
    # Check if any of the images are "ga"
    if r_a == resize_g or r_b == resize_g or r_c == resize_g:
        check_sum_money = True
        if r_a == resize_g:
            count_ga = count_ga + 1
        if r_b == resize_g:
            count_ga = count_ga + 1
        if r_c == resize_g:
            count_ga = count_ga + 1
        if count_ga == 1:
            multi_ga = 2
        if count_ga == 2:
            multi_ga = 3 
        if count_ga == 3:
            multi_ga = 4
        # Calculate winnings for "ga" bets
        a_g = resize_g
        a_g = "ga"
        if a_g in check:
            list_check.append(money_ga50)
            list_check.append(money_ga100)
            list_check.append(money_ga500)
            lai_ga = tien_ga * multi_ga
            sodu = sodu + lai_ga
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
            # print("Thang Ga")
    # If there are winnings, update the total bet amount
    if check_sum_money == True:
        sum_money = sum_money + lai_ga
        check_sum_money = False
    tien_ga = 0
    count_nai = 0
    multi_nai = 0
    
    # Check if any of the images are "nai"
    if r_a == resize_n or r_b == resize_n or r_c == resize_n:
        check_sum_money = True
        if r_a == resize_n:
            count_nai = count_nai + 1
        if r_b == resize_n:
            count_nai = count_nai + 1
        if r_c == resize_n:
            count_nai = count_nai + 1
        if count_nai == 1:
            multi_nai = 2
        if count_nai == 2:
            multi_nai = 3 
        if count_nai == 3:
            multi_nai = 4
        # Calculate winnings for "nai" bets
        a_n = resize_n
        a_n = "nai"
        if a_n in check:
            list_check.append(money_nai50)
            list_check.append(money_nai100)
            list_check.append(money_nai500)
            # print("Thang Nai")
            lai_nai = tien_nai * multi_nai
            sodu = sodu + lai_nai
            l_sodu.config(text=f"Số dư : {sodu} vnđ")
    # If there are winnings, update the total bet amount
    if check_sum_money == True:
        sum_money = sum_money + lai_nai
        check_sum_money = False
    tien_nai = 0
    check = []
    
    
check_bd = False # Check that every time you play, you must press the start button to play
def run():

    global money_calculated
    global sum_money
    global check_bd
    
    # Check if money is already calculated
    if money_calculated == True:
        global list_n
        # Update the dice images    
        pygame.mixer.music.load("./xucxacsound.mp3")
        pygame.mixer.music.play(loops=0)
        update_rand(lb_1, lb_2, lb_3)
        
        # Remove widgets (animal bets) that are not checked
        for widget in animal_bet:
            if widget not in list_check:
                widget.grid_remove()

        # Update the window to show changes
        win.update()
        
        # Reset flags and total bet amount
        money_calculated = False
        
        # Update the total bet amount display label based on the result
        if sum_money > 0:
            ls.config(text=f"Tổng : + {sum_money} vnđ")
        elif sum_money < 0:
            ls.config(text=f"Tổng : - {abs(sum_money)} vnđ")
        else:
            ls.config(text=f"Tổng : {sum_money} vnđ")
        
        # Reset the check flag and total bet amount
        check_bd = False
        sum_money = 0
    else:
        # If money is not calculated, show a warning message
        messagebox.showwarning("Cảnh Báo", "Vui lòng bắt đầu trước khi đặt cược!!!", icon=messagebox.WARNING)
    
def batdau(): # Function start
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    global check_bd 
    if check_bd == False:
        global money_calculated
        money_calculated = True
        for widget in animal_bet: # Check if the value appears in the list, delete it
            widget.grid_remove()
        global tien_bau,tien_ca,tien_cua,tien_ga,tien_nai,tien_tom
        tien_bau = 0
        tien_ca = 0
        tien_cua = 0
        tien_ga = 0
        tien_nai = 0
        tien_tom = 0
        list_check.clear() # Delete List
        animal_bet.clear() # Delete List
        # bt_tt.config(text="Chơi Tiếp")
        win.update()
        check_bd = True

def naptien(): #Deposit function
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    global wnt
    global e_nt
    wnt = Toplevel() # New win deposit
    wnt["bg"] = "red"
    wnt.title("Nạp Tiền")
    wnt.geometry("220x70")
    wnt.iconbitmap("./iconmoney.ico")
    lb_nt = Label(wnt,text="Nhập số tiền cần nạp",bg="red",font=("Arial", 10, "bold")) # label 
    lb_nt.grid(column=0,row=0)
    e_nt = Entry(wnt,border=5,width=25) # Amount input 
    e_nt.grid(column=0,row=1,padx=5)
    nt_click = Button(wnt,text="Nạp",command=v_t) # finish button
    nt_click.grid(column=1,row=1)

def v_t(): #balance function
    pygame.mixer.music.load("./clickchuot.mp3")
    pygame.mixer.music.play(loops=1)
    global sodu
    sodu = sodu + int(e_nt.get())
    l_sodu.config(text=f"Số dư : {sodu} vnđ")
    wnt.destroy()
        
# Button Run
bt = Button(win,text="Run",command=run,image=rs_hop,border=5)
bt.grid(column=2,row=1,padx=10,pady=10)

# Choose Money
lb_money = Label(win,text="Chọn số tiền đặt cược :",bg="red",font=("Arial", 12, "bold"))
lb_money.grid(column=1,row=4,columnspan=1)

# Button Money
money_50k = Button(win,text="1",image=rs_50k,command=click_50k)
money_50k.grid(column=1,row=5,pady=10)
money_100k = Button(win,text="1",image=rs_100k,command=click_100k)
money_100k.grid(column=2,row=5,pady=10)
money_500k = Button(win,text="1",image=rs_500k,command=click_500k)
money_500k.grid(column=3,row=5,pady=10)

# info window
win1 = Toplevel()
win1["bg"] = "red"
win1.geometry("250x250")
win1.title("Thông Tin")
win1.iconbitmap("./iconbaucua.ico")

# số dư
sodu = 0

# Label for displaying the balance.
l_sodu = Label(win1, text=f"Số dư : {sodu} vnđ", font=("Arial", 12, "bold"))
l_sodu.grid(column=0, row=0, pady=10, columnspan=2, sticky="w")

# Button to 'Nạp Tiền'.
bt_nt = Button(win1, text="Nạp Tiền", font=("Arial", 12, "bold"), command=naptien)
bt_nt.grid(column=1, row=1, padx=10, pady=10, sticky="e")

# Button to 'bắt đầu'.
bt_tt = Button(win1, text="Bắt Đầu", font=("Arial", 12, "bold"), command=batdau)
bt_tt.grid(column=0, row=1, padx=20, pady=10, sticky="w")


# lich su

ls = Label(win1,text="Chưa có", font=("Arial", 10, "bold"))
ls.grid(column=0, row=2,padx=20,pady=10,sticky="w",columnspan=1000)

win.mainloop()

