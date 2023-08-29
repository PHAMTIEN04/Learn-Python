# Import necessary libraries
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

# Create the main window
win = Tk()
win.title("Quản Lý Bán Hàng")
win.geometry("1200x700+200+20")
win.resizable(False, False)  # Horizontal and vertical resizing is not allowed
win.iconbitmap("D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/icon.ico")
# Function to clear a specific area
def clear_b():
    cl = Label(win, text="", width=150, height=100)
    cl.place(rely=0, relx=0.18)

def vnd(str_c):
    str_n = str(str_c)
    i = len(str_n) - 1
    g = ""
    cnt = 0
    while i >= 0:
        g = str_n[i] + g
        if cnt % 3 == 2 and i > 0:
            g = "." + g
        i -= 1
        cnt += 1
    g_c = g + "đ"
    return str(g_c)

def get_value_g_ta_dtb(stt_ta):
    conn_ta = sqlite3.connect("QLBHTANU.db")
    c_ta = conn_ta.cursor()
    c_ta.execute(f"SELECT * FROM thucan WHERE stt = {stt_ta}")
    res_ta = c_ta.fetchall()
    g_ta = res_ta[0][2]
    conn_ta.commit()
    conn_ta.close()
    return str(g_ta)
    
def get_value_g_nu_dtb(stt_nu):
    conn_nu = sqlite3.connect("QLBHTANU.db")
    c_nu = conn_nu.cursor()
    c_nu.execute(f"SELECT * FROM nuocuong WHERE stt = {stt_nu}")
    res_nu = c_nu.fetchall()
    g_nu = res_nu[0][2]
    conn_nu.commit()
    conn_nu.close()
    return str(g_nu)
 

# Function to fetch food product data from the database
def get_value_t_ta_dtb(stt_ta):
    conn_ta = sqlite3.connect("QLBHTANU.db")
    c_ta = conn_ta.cursor()
    c_ta.execute(f"SELECT * FROM thucan WHERE stt = {stt_ta}")
    res_ta = c_ta.fetchall()
    vl_ta = res_ta[0][1]
    conn_ta.commit()
    conn_ta.close()
    return str(vl_ta)

# Function to fetch drink product data from the database
def get_value_t_nu_dtb(stt_nu):
    conn_nu = sqlite3.connect("QLBHTANU.db")
    c_nu = conn_nu.cursor()
    c_nu.execute(f"SELECT * FROM nuocuong WHERE stt = {stt_nu}")
    res_nu = c_nu.fetchall()
    vl_nu = res_nu[0][1]
    conn_nu.commit()
    conn_nu.close()
    return str(vl_nu)

# Function to resize an image
def resize_img(path, width, height):
    img = Image.open(path)
    rez_img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(rez_img)

# Placeholder for the 'Home' function
def home():
    clear_b()

# Global variables
check = 0
i = 1

# Function to handle the 'Products' menu
def menu():
    global check
    global bt_home1,bt_home2
    check = check + 1
    if check == 1:
        bt_home1 = Button(win, text="Thức Ăn", fg="white", bg="gray", border=0, command=thucan,font=("bold",9,"bold"))
        bt_home1.place(relx=0.037, rely=0.25)
        bt_home2 = Button(win, text="Nước Uống", fg="white", bg="gray", border=0, command=nuocuong,font=("bold",9,"bold"))
        bt_home2.place(relx=0.037, rely=0.3)
        Button_add_data.place(relx=0.03, rely=0.35)
        Button_edit_data.place(relx=0.03, rely=0.45)
        Button_del_data.place(relx=0.03,rely=0.55)

    elif check == 2:
        bt_home1.destroy()  # Xóa nút "Thức Ăn"
        bt_home2.destroy()  # Xóa nút "Nước Uống"
        Button_add_data.place(relx=0.03, rely=0.3)
        Button_edit_data.place(relx=0.03,rely=0.4)
        Button_del_data.place(relx=0.03,rely=0.5)      
        check = 0
    win.update()
# Function to display food products
def thucan():
    clear_b()
    conn = sqlite3.connect("QLBHTANU.db")
    c = conn.cursor()
    c.execute("SELECT * FROM thucan")
    list_ta = c.fetchall()
    conn.commit()
    conn.close()

    x_img = 0.23
    y_img = 0.1
    x_t = 0.23
    y_t = 0.36
    sl = 1  # Start the counter
    for s, t, g, f in list_ta:
        stt = s
        ten = t
        gia = g
        file = f

        ta_img = resize_img(file, 200, 180)
        ta_lb_img = Label(win, image=ta_img)
        ta_lb_img.image = ta_img
        ta_lb_img.place(relx=x_img, rely=y_img)
        ta_lb_text = Label(win, text=get_value_t_ta_dtb(stt),fg="blue",font=("bold",12,"bold"))
        ta_lb_text.place(relx=x_t, rely=y_t)

        ta_lb_g = Label(win,text=vnd(get_value_g_ta_dtb(stt)),fg="black",font=("bold",10,"bold"))
        ta_lb_g.place(relx=x_t,rely=y_t +0.03)
        
        buy_callback_ta = lambda stt=stt, ten=ten, gia=gia, file = file: buy_product_ta(stt, ten, gia, file)
        ta_bt_m = Button(win,text="Mua",border=3,bg="light green",font=("bold",10,"bold"),command=buy_callback_ta)
        ta_bt_m.place(relx=x_t+0.135,rely=y_t)
        
        if sl % 3 == 0:
            x_img = 0.23
            x_t = 0.23
            y_img += 0.4
            y_t += 0.4
        else:
            x_img += 0.25  # Increase x_img to adjust the horizontal position of the next item
            x_t = (x_t + 0.30) - 0.05  # Increase x_t similarly
        
        sl += 1  # Increment the counter


def buy_product_ta(stt, ten, gia,file):
    clear_b()
    global count_sl_ta,ta_sl_buy_bt_cong,ta_sl_buy_bt_tru,ta_sl_buy_lb_text,ta_sum_buy_lb,gia_c
    gia_c = gia
    count_sl_ta = 0
    ta_img_buy = resize_img(file,200,180)
    ta_img_buy_lb = Label(win,image=ta_img_buy)
    ta_img_buy_lb.image = ta_img_buy
    ta_img_buy_lb.place(relx=0.23,rely=0.1)
    
    frame1_ta = LabelFrame(win,width=200,height=35)
    frame1_ta.place(relx=0.44,rely=0.1)
    ta_stt_buy_lb = Label(frame1_ta,text=f"STT : {stt}",font=("bold",10,"bold"))
    ta_stt_buy_lb.place(relx=0.07,rely=0.13)
    
    frame2_ta = LabelFrame(win,width=200,height=35)
    frame2_ta.place(relx=0.44,rely=0.2)
    ta_t_buy_lb = Label(frame2_ta,text=f"Tên : {ten}",font=("bold",10,"bold"))
    ta_t_buy_lb.place(relx=0.07,rely=0.13)
    
    frame3_ta = LabelFrame(win,width=200,height=35)
    frame3_ta.place(relx=0.44,rely=0.3)
    ta_g_buy_lb = Label(frame3_ta,text=f"Giá : {vnd(gia)}",font=("bold",10,"bold"))
    ta_g_buy_lb.place(relx=0.07,rely=0.13)
    
    ta_sl_buy_lb = Label(win,text="Số Lượng:",font=("bold",10,"bold"))
    ta_sl_buy_lb.place(relx=0.44,rely=0.37)
    ta_sl_buy_bt_tru = Button(win,text="-",border=4,font=("bold",7,"bold"),command=tru_ta)
    ta_sl_buy_bt_tru.place(relx=0.51,rely=0.37)
    ta_sl_buy_lb_text = Label(win,text=count_sl_ta,font=("bold",11,"bold"))
    ta_sl_buy_lb_text.place(relx=0.528,rely=0.37)
    ta_sl_buy_bt_cong = Button(win,text="+",border=4,font=("bold",7,"bold"),command=cong_ta)
    ta_sl_buy_bt_cong.place(relx=0.55,rely=0.37)
    
    ta_sum_buy_lb = Label(win,text=f"Tổng Tiền: {vnd(int(gia_c)*count_sl_ta)}",font=("bold",10,"bold"))
    ta_sum_buy_lb.place(relx=0.44,rely=0.42)
    
    ta_xn_buy_bt = Button(win,text="Thanh Toán",font=("bold",10,"bold"),width=24,border=3,fg="white",bg="blue",command=xn_buy_ta)
    ta_xn_buy_bt.place(relx=0.44,rely=0.5)

def xn_buy_ta():
    messagebox.showinfo("Thanh Toán","Thanh Toán Thành Công!!!")
    global count_sl_ta,ta_sl_buy_lb_text,ta_sum_buy_lb,gia_c
    count_sl_ta = 0
    ta_sl_buy_lb_text.config(text=count_sl_ta)
    ta_sum_buy_lb.config(text=f"Tổng Tiền: {vnd(int(gia_c)*count_sl_ta)}")
    
def cong_ta():
    global count_sl_ta,ta_sl_buy_lb_text,ta_sum_buy_lb,gia_c
    if count_sl_ta <= 49:
        count_sl_ta = count_sl_ta + 1
        
    ta_sl_buy_lb_text.config(text=count_sl_ta)
    ta_sum_buy_lb.config(text=f"Tổng Tiền: {vnd(int(gia_c)*count_sl_ta)}")
    win.update()

def tru_ta():
    global count_sl_ta,ta_sl_buy_lb_text,ta_sum_buy_lb,gia_c
    if count_sl_ta > 0:
        count_sl_ta = count_sl_ta - 1
    ta_sl_buy_lb_text.config(text=count_sl_ta)
    ta_sum_buy_lb.config(text=f"Tổng Tiền: {vnd(int(gia_c)*count_sl_ta)}")
    win.update()
    
# Function to display drink products
def nuocuong():
    clear_b()
    conn = sqlite3.connect("QLBHTANU.db")
    c = conn.cursor()
    c.execute("SELECT * FROM nuocuong")
    list_nu = c.fetchall()
    conn.commit()
    conn.close()

    x_img = 0.23
    y_img = 0.1
    x_t = 0.23
    y_t = 0.36
    sl = 1  # Start the counter
    for s, t, g, f in list_nu:
        stt = s
        ten = t
        gia = g
        file = f

        nu_img = resize_img(file, 200, 180)
        nu_lb_img = Label(win, image=nu_img)
        nu_lb_img.image = nu_img
        nu_lb_img.place(relx=x_img, rely=y_img)
        nu_lb_text = Label(win, text=get_value_t_nu_dtb(stt),fg="blue",font=("bold",12,"bold"))
        nu_lb_text.place(relx=x_t, rely=y_t)

        nu_lb_g = Label(win,text=vnd(get_value_g_nu_dtb(stt)),fg="black",font=("bold",10,"bold"))
        nu_lb_g.place(relx=x_t,rely=y_t +0.03)
        
        buy_callback_nu = lambda stt=stt, ten=ten, gia=gia, file = file: buy_product_nu(stt, ten, gia, file)
        nu_bt_m = Button(win,text="Mua",border=3,bg="light green",font=("bold",10,"bold"),command=buy_callback_nu)
        nu_bt_m.place(relx=x_t+0.135,rely=y_t)

        if sl % 3 == 0:
            x_img = 0.23
            x_t = 0.23
            y_img += 0.4
            y_t += 0.4
        else:
            x_img += 0.25  # Increase x_img to adjust the horizontal position of the next item
            x_t = (x_t + 0.30) - 0.05  # Increase x_t similarly
        
        sl += 1  # Increment the counter

def buy_product_nu(stt, ten, gia,file):
    clear_b()
    global count_sl_nu,nu_sl_buy_bt_cong,nu_sl_buy_bt_tru,nu_sl_buy_lb_text,nu_sum_buy_lb,gia_b
    gia_b = gia
    count_sl_nu = 0
    nu_img_buy = resize_img(file,200,180)
    nu_img_buy_lb = Label(win,image=nu_img_buy)
    nu_img_buy_lb.image = nu_img_buy
    nu_img_buy_lb.place(relx=0.23,rely=0.1)
    
    frame1_nu = LabelFrame(win,width=200,height=35)
    frame1_nu.place(relx=0.44,rely=0.1)
    nu_stt_buy_lb = Label(frame1_nu,text=f"STT : {stt}",font=("bold",10,"bold"))
    nu_stt_buy_lb.place(relx=0.07,rely=0.13)
    
    frame2_nu = LabelFrame(win,width=200,height=35)
    frame2_nu.place(relx=0.44,rely=0.2)
    nu_t_buy_lb = Label(frame2_nu,text=f"Tên : {ten}",font=("bold",10,"bold"))
    nu_t_buy_lb.place(relx=0.07,rely=0.13)
    
    frame3_nu = LabelFrame(win,width=200,height=35)
    frame3_nu.place(relx=0.44,rely=0.3)
    nu_g_buy_lb = Label(frame3_nu,text=f"Giá : {vnd(gia)}",font=("bold",10,"bold"))
    nu_g_buy_lb.place(relx=0.07,rely=0.13)
    
    nu_sl_buy_lb = Label(win,text="Số Lượng:",font=("bold",10,"bold"))
    nu_sl_buy_lb.place(relx=0.44,rely=0.37)
    nu_sl_buy_bt_tru = Button(win,text="-",border=4,font=("bold",7,"bold"),command=tru_nu)
    nu_sl_buy_bt_tru.place(relx=0.51,rely=0.37)
    nu_sl_buy_lb_text = Label(win,text=count_sl_nu,font=("bold",11,"bold"))
    nu_sl_buy_lb_text.place(relx=0.528,rely=0.37)
    nu_sl_buy_bt_cong = Button(win,text="+",border=4,font=("bold",7,"bold"),command=cong_nu)
    nu_sl_buy_bt_cong.place(relx=0.55,rely=0.37)
    
    nu_sum_buy_lb = Label(win,text=f"Tổng Tiền: {vnd(int(gia_b)*count_sl_nu)}",font=("bold",10,"bold"))
    nu_sum_buy_lb.place(relx=0.44,rely=0.42)
    
    nu_xn_buy_bt = Button(win,text="Thanh Toán",font=("bold",10,"bold"),width=24,border=3,fg="white",bg="blue",command=xn_buy_nu)
    nu_xn_buy_bt.place(relx=0.44,rely=0.5)
    
def xn_buy_nu():
    messagebox.showinfo("Thanh Toán","Thanh Toán Thành Công!!!")
    global count_sl_nu,nu_sl_buy_lb_text,nu_sum_buy_lb,gia_b
    count_sl_nu = 0
    nu_sl_buy_lb_text.config(text=count_sl_nu)
    nu_sum_buy_lb.config(text=f"Tổng Tiền: {vnd(int(gia_b)*count_sl_nu)}")
    
def cong_nu():
    global count_sl_nu,nu_sl_buy_lb_text,nu_sum_buy_lb,gia_b
    if count_sl_nu <= 49:
        count_sl_nu = count_sl_nu + 1
        
    nu_sl_buy_lb_text.config(text=count_sl_nu)
    nu_sum_buy_lb.config(text=f"Tổng Tiền: {vnd(int(gia_b)*count_sl_nu)}")
    win.update()

def tru_nu():
    global count_sl_nu,nu_sl_buy_lb_text,nu_sum_buy_lb,gia_b
    if count_sl_nu > 0:
        count_sl_nu = count_sl_nu - 1
    nu_sl_buy_lb_text.config(text=count_sl_nu)
    nu_sum_buy_lb.config(text=f"Tổng Tiền: {vnd(int(gia_b)*count_sl_nu)}")
    win.update()
# Create a StringVar to store the selected value from the radio buttons
dt = StringVar()
dt.set(" ")

def add_data():
    # Add product data logic here
    clear_b()
    global a_d_stt_e, a_d_t_e, a_d_g_e
    a_d_stt_text = Label(win, text="Stt")
    a_d_stt_text.place(relx=0.2, rely=0.05)
    a_d_stt_e = Entry(win)
    a_d_stt_e.place(relx=0.225, rely=0.05)
    
    a_d_t_text = Label(win, text="Tên")
    a_d_t_text.place(relx=0.2, rely=0.1)
    a_d_t_e = Entry(win)
    a_d_t_e.place(relx=0.225, rely=0.1)
    
    a_d_g_text = Label(win, text="Giá")
    a_d_g_text.place(relx=0.2, rely=0.15)
    a_d_g_e = Entry(win)
    a_d_g_e.place(relx=0.225, rely=0.15)
    
    a_d_i_b = Button(win, text="Chọn Ảnh", command=open_img)
    a_d_i_b.place(relx=0.2, rely=0.2)
    
    choose_ta = Radiobutton(win, text="Thức Ăn", variable=dt, value="Thức Ăn", command=on_selection_change)
    choose_ta.place(relx=0.2, rely=0.30)
    choose_nu = Radiobutton(win, text="Nước Uống", variable=dt, value="Nước Uống", command=on_selection_change)
    choose_nu.place(relx=0.2, rely=0.35)
    
    a_d_xn_b = Button(win, text="Xác Nhận", command=xacnhan_add)
    a_d_xn_b.place(relx=0.2, rely=0.4)

def xacnhan_add():
    # Confirmation logic for adding data
    global a_d_stt_e, a_d_t_e, a_d_g_e
    global dt
    global filename_img
    if dt.get() == "Thức Ăn":
        conn = sqlite3.connect("QLBHTANU.db")
        c = conn.cursor()
        c.execute("INSERT INTO thucan VALUES(:stt,:ten,:gia,:file)", {
            "stt": int(a_d_stt_e.get()),
            "ten": a_d_t_e.get(),
            "gia": int(a_d_g_e.get()),
            "file": filename_img
        })
        conn.commit()
        conn.close()
    elif dt.get() == "Nước Uống":
        conn = sqlite3.connect("QLBHTANU.db")
        c = conn.cursor()
        c.execute("INSERT INTO nuocuong VALUES(:stt,:ten,:gia,:file)", {
            "stt": int(a_d_stt_e.get()),
            "ten": a_d_t_e.get(),
            "gia": int(a_d_g_e.get()),
            "file": filename_img
        })
        conn.commit()
        conn.close()
    dt.set(" ")
    a_d_stt_e.delete(0, END)
    a_d_t_e.delete(0, END)
    a_d_g_e.delete(0, END)
    Label(win, text="", width=55, height=1).place(relx=0.2, rely=0.25)

def on_selection_change():
    pass

def open_img():
    # Logic to open and display an image file
    global filename_img
    win.filename = filedialog.askopenfilename(initialdir="D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong", title="Select File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    filename_img = win.filename
    Label(win, text=filename_img).place(relx=0.2, rely=0.25)
    
ed = StringVar()
ed.set(" ")
def edit_data():
    # Edit product data logic here
    clear_b()
    global edit_d_stt_e, edit_d_t_e, edit_d_g_e
    edit_d_stt_text = Label(win, text="Stt")
    edit_d_stt_text.place(relx=0.2, rely=0.05)
    edit_d_stt_e = Entry(win)
    edit_d_stt_e.place(relx=0.225, rely=0.05)
    
    edit_d_t_text = Label(win, text="Tên")
    edit_d_t_text.place(relx=0.2, rely=0.1)
    edit_d_t_e = Entry(win)
    edit_d_t_e.place(relx=0.225, rely=0.1)
    
    edit_d_g_text = Label(win, text="Giá")
    edit_d_g_text.place(relx=0.2, rely=0.15)
    edit_d_g_e = Entry(win)
    edit_d_g_e.place(relx=0.225, rely=0.15)
    
    edit_d_i_b = Button(win, text="Chọn Ảnh",command=open_img)
    edit_d_i_b.place(relx=0.2, rely=0.2)
    
    choose_ta_edit = Radiobutton(win, text="Thức Ăn", variable=ed, value="Thức Ăn")
    choose_ta_edit.place(relx=0.2, rely=0.30)
    choose_nu_edit = Radiobutton(win, text="Nước Uống", variable=ed, value="Nước Uống")
    choose_nu_edit.place(relx=0.2, rely=0.35)
    
    edit_d_xn_b = Button(win, text="Xác Nhận", command=xacnhan_edit)
    edit_d_xn_b.place(relx=0.2, rely=0.4)

def xacnhan_edit():
    # Confirmation logic for edit data
    global ed
    global edit_d_stt_e,edit_d_t_e,edit_d_g_e
    global filename_img
    if ed.get() == "Thức Ăn":
        conn = sqlite3.connect("QLBHTANU.db")
        c = conn.cursor()
        c.execute("""UPDATE thucan SET
                  stt = :stt,
                  ten = :ten,
                  gia = :gia,
                  file = :file
                  
                  WHERE stt = :stt
                  """,{
                  'stt' : edit_d_stt_e.get(),
                  'ten' : edit_d_t_e.get(),
                  'gia' : edit_d_g_e.get(),
                  'file': filename_img 
                  })
        conn.commit()
        conn.close()
    elif ed.get() == "Nước Uống":
        conn = sqlite3.connect("QLBHTANU.db")
        c = conn.cursor()
        c.execute("""UPDATE nuocuong SET
                  stt = :stt,
                  ten = :ten,
                  gia = :gia,
                  file = :file
                  
                  WHERE stt = :stt
                  """,{
                  'stt' : edit_d_stt_e.get(),
                  'ten' : edit_d_t_e.get(),
                  'gia' : edit_d_g_e.get(),
                  'file': filename_img 
                  })
        conn.commit()
        conn.close()
    ed.set(" ")
    edit_d_stt_e.delete(0, END)
    edit_d_t_e.delete(0, END)
    edit_d_g_e.delete(0, END)
    Label(win, text="", width=55, height=1).place(relx=0.2, rely=0.25)


dd = StringVar()
dd.set(" ")
def del_data():
    # Delete product data logic here
    clear_b()
    global d_stt_e
    d_stt_text = Label(win, text="Stt")
    d_stt_text.place(relx=0.2, rely=0.05)
    d_stt_e = Entry(win)
    d_stt_e.place(relx=0.225, rely=0.05)
    
    choose_ta_d = Radiobutton(win, text="Thức Ăn", variable=dd, value="Thức Ăn")
    choose_ta_d.place(relx=0.2, rely=0.10)
    choose_nu_d = Radiobutton(win, text="Nước Uống", variable=dd, value="Nước Uống")
    choose_nu_d.place(relx=0.2, rely=0.15)
    
    a_d_xn_b = Button(win, text="Xác Nhận",command=xacnhan_del)
    a_d_xn_b.place(relx=0.2, rely=0.2)

    
def xacnhan_del():
    # Confirmation logic for deleting data
    global dd,d_stt_e
    if dd.get() == "Thức Ăn":
        conn = sqlite3.connect("QLBHTANU.db")
        c = conn.cursor()
        c.execute(f"DELETE FROM thucan WHERE stt = {int(d_stt_e.get())}")
        conn.commit()
        conn.close()
    elif dd.get() == "Nước Uống":
        conn = sqlite3.connect("QLBHTANU.db")
        c = conn.cursor()
        c.execute(f"DELETE FROM nuocuong WHERE stt = {int(d_stt_e.get())}")
        conn.commit()
        conn.close()
    d_stt_e.delete(0,END)
    dd.set(" ")
    
# Create a gray background label
labe_nen = Label(win, text="", bg="gray", width=30, height=60)
labe_nen.grid(column=0, rowspan=13)

# Create a logo button
logo_img = resize_img("D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/logo.png",210,50)
Button_logo = Button(win, text="Logo", fg="white", bg="gray", border=0,image=logo_img)
Button_logo.place(relx=0,rely=0)

# Create a 'Home' button
Button_home = Button(win, text="Trang Chủ", fg="white", bg="gray", border=0, command=home,font=("bold",12,"bold"))
Button_home.place(relx=0.03,rely=0.1)

# Create a 'Products' button
Button_menu = Button(win, text="Sản Phẩm", fg="white", bg="gray", border=0, command=menu,font=("bold",12,"bold"))
Button_menu.place(relx=0.03,rely=0.2)

# Create an 'Add Product' button
Button_add_data = Button(win, text="Thêm Sản Phẩm", fg="white", bg="gray", border=0, command=add_data,font=("bold",12,"bold"))
Button_add_data.place(relx=0.03, rely=0.3)

# Create an 'Edit Product' button
Button_edit_data = Button(win,text="Sửa Sản Phẩm",fg="white",bg="gray",border=0,command=edit_data,font=("bold",12,"bold"))
Button_edit_data.place(relx=0.03,rely=0.4)

# Create an 'Delete Product' button
Button_del_data = Button(win,text="Xóa Sản Phẩm", fg="white",bg="gray", border=0,command=del_data,font=("bold",12,"bold"))
Button_del_data.place(relx=0.03,rely=0.5)

# Start the GUI event loop
win.mainloop()

# import sqlite3
# conn = sqlite3.connect("QLBHTANU.db")
# c = conn.cursor()
# c.execute("""CREATE TABLE nuocuong(
#         stt integer,
#         ten text,
#         gia integer,
#         file text    
#     )""")
# c.execute("""CREATE TABLE thucan(
#         stt integer,
#         ten text,
#         gia integer,
#         file text
#     )""")
# c.execute("INSERT INTO nuocuong VALUES(:stt,:ten,:gia)",{
#         'stt' : 2,
#         'ten' : "Nước Dừa",
#         "gia" : 7000
# })
# c.execute("DELETE FROM thucan WHERE stt = 3")
# c.execute("SELECT * FROM thucan")
# res = c.fetchall()
# print(res)
# conn.commit()
# conn.close()