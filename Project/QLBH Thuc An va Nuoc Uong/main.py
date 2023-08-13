from tkinter import *
import sqlite3
from PIL import Image,ImageTk

win = Tk()
win.title("Quản Lý Bán Hàng")
win.geometry("1200x700+200+20")
win.resizable(False, False)  # Không cho phép thay đổi kích thước theo chiều ngang và dọc


def home():
    pass

def menu():
    bt_home1 = Button(win, text="Thức Ăn", fg="white", bg="gray", border=0)
    bt_home1.place(relx=0.01,rely=0.28)
    bt_home2 = Button(win, text="Đồ Uống", fg="white", bg="gray", border=0)
    bt_home2.place(relx=0.01,rely=0.33)

labe_nen = Label(win, text="", bg="gray", width=30, height=60)
labe_nen.grid(column=0, rowspan=13)

Button_logo = Button(win, text="Logo", fg="white", bg="gray", border=0)
Button_logo.grid(column=0, row=0, rowspan=1, sticky="NW")

Button_home = Button(win, text="Trang Chủ", fg="white", bg="gray", border=0, command=home)
Button_home.grid(column=0, row=1, rowspan=1, sticky="NW")

Button_menu = Button(win, text="Sản Phẩm", fg="white", bg="gray", border=0, command=menu)
Button_menu.grid(column=0, row=2, rowspan=1, sticky="NW")

# class ThucAn():
#     def
def resize_img(path,width,height):
    img = Image.open(path)
    rez_img = img.resize((width,height), Image.LANCZOS)
    return ImageTk.PhotoImage(rez_img)
def get_value_dtb(stt):
    conn = sqlite3.connect("QLBHTANU.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM thucan WHERE stt = {stt}")
    res = c.fetchall()
    vl = res[0][1]
    conn.commit()
    conn.close()
    return str(vl)
bu_img = resize_img("D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/banhuot.jpg",200,100)
bu_lb_img = Label(win,image=bu_img,borderwidth=0,highlightthickness=0)
bu_lb_img.place(relx=0.23,rely=0.1)
bu_lb_text = Label(win,text=get_value_dtb(1))
bu_lb_text.place(rely=0.26,relx=0.28)

win.mainloop()
# import sqlite3

# conn = sqlite3.connect("QLBHTANU.db")
# c = conn.cursor()
# c.execute("""CREATE TABLE thucan(
#         stt integer,
#         ten text,
#         gia integer    
#     )""")
# c.execute("INSERT INTO thucan VALUES(:stt,:ten,:gia)",{
#         'stt' : 1,
#         'ten' : "Bánh Ướt",
#         "gia" : 20000
# })
# c.execute("SELECT * FROM thucan")
# res = c.fetchall()
# print(res)
# conn.commit()
# conn.close()