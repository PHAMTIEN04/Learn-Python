import os
from tkinter import *
import bs4
import requests
import re 
while True:
    win = Tk()
    os.chdir(r'D:\Learn Python\Tkinter\ProjectGetCoin')


    url = 'https://coinmarketcap.com/'
    response = requests.get(url=url)
    html_code = response.text   
    filename = 'codetxt.html'
        # Cho mã nguồn vào file 
    with open(file=filename,mode='w',encoding="utf8") as file_open:
        file_open.write(html_code)
        # Tách giá trị của mã nguồn cần tacgs
        soup = bs4.BeautifulSoup(html_code, 'html.parser')
        eles = soup.select('span')
        # Lấy giá trị vừa tách xong viết nó vào file mới
    with open(file='Checktxt.txt', mode='w', encoding='utf8') as filename_check:
        for elem in eles:
            text = elem.get_text()
            filename_check.write(text + ' ')
                # Đọc giá tri của File 
    filename_text = 'Checktxt.txt'
    with open(file=filename_text, mode='r', encoding='utf8') as file_text:
            check_regex = file_text.read()
            # Regex điều kiện
    regex_btc = re.compile(r'                    (.*?) ')
    regex_hb = re.compile(r'Huobi Token HT (.*?)     ')
    regex_ape = re.compile(r'ApeCoin APE (.*?)     ')
    regex_apt = re.compile(r'Aptos APT (.*?)     ')
    regex_agix = re.compile(r'SingularityNET AGIX (.*?)     ')
# Regex tìm kiếm giá trị đó cùng điều kiện 
    kq_btc = regex_btc.search(check_regex)
    kq_hb = regex_hb.search(check_regex)
    kq_ape = regex_ape.search(check_regex)
    kq_apt = regex_apt.search(check_regex)
    kq_agix = regex_agix.search(check_regex)
# Lấy giá trị của Regex vừa tìm kiếm được
    text_btc = kq_btc.group(1)
    text_hb = kq_hb.group(1)
    text_ape = kq_ape.group(1)
    text_apt = kq_apt.group(1)
    # text_agix = kq_agix.group(1)
# print(text_btc)



    win.title("Prices Coin")
    win.geometry("500x500")
    win["bg"] = "#FFCCFF"


    Get_input = Entry(win, width=50,border=5,fg= "green")
    Get_input.pack()

    def inputcoin():
        if Get_input.get() == "Bitcoin" or Get_input.get() == "BTC": 
            test_btc = Label(win,text=text_btc,width=10,fg= "red",bg="#FFCCCC")
            test_btc.pack()
    # Hủy bỏ các Label cũ
            for widget in win.winfo_children():
                if isinstance(widget, Label) and widget != test_btc:
                    widget.destroy()
        elif Get_input.get() == "Houbi" or Get_input.get() == "HB" : 
            test_hb = Label(win,text=text_hb,width=10,fg= "pink",bg="#FFCCCC")
            test_hb.pack()
    # Hủy bỏ các Label cũ
            for widget in win.winfo_children():
                if isinstance(widget, Label) and widget != test_hb:
                    widget.destroy()
        elif Get_input.get() == "Apecoin" or Get_input.get() == "APE" : 
            test_ape = Label(win,text=text_ape,width=10,fg= "green",bg="#FFCCCC")
            test_ape.pack()
    # Hủy bỏ các Label cũ
            for widget in win.winfo_children():
                if isinstance(widget, Label) and widget != test_ape:
                    widget.destroy()
        elif Get_input.get() == "Aptos" or Get_input.get() == "APT" : 
            test_apt = Label(win,text=text_apt,width=10,fg= "blue",bg="#FFCCCC")
            test_apt.pack()
    # Hủy bỏ các Label cũ
            for widget in win.winfo_children():
                if isinstance(widget, Label) and widget != test_apt:
                    widget.destroy()
        elif Get_input.get() == "SingularityNET AGIX" or Get_input.get() == "AGIX" : 
            test_agix = Label(win,text=text_agix,width=10,fg= "purple",bg="#FFCCCC")
            test_agix.pack()
    # Hủy bỏ các Label cũ
            for widget in win.winfo_children():
                if isinstance(widget, Label) and widget != test_agix:
                    widget.destroy()
        else:
            test1 = Label(win,text="Error!!! Vui Long Nhap Lai",fg= "red",bg="#FFCCCC")
            test1.pack()
    # Hủy bỏ các Label cũ
            for widget in win.winfo_children():
                if isinstance(widget, Label) and widget != test1:
                    widget.destroy()


    Button1 = Button(win,text="Exit",command=exit)
    Button1.pack()
    def getbutton():
        Get_button = Button(win,text="Enter",command=inputcoin ,width=20,height=5,border=3,fg = "red",bg = "#BBBBBB")
        Get_button.pack()

    getbutton()


   

 




    win.mainloop()

