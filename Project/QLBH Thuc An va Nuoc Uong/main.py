from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter import filedialog
# Create the main window
win = Tk()
win.title("Quản Lý Bán Hàng")
win.geometry("1200x700+200+20")
win.resizable(False, False) # Horizontal and vertical resizing is not allowed

# Function to clear a specific area
def clear_b():
    cl = Label(win, text="", width=150, height=100)
    cl.place(rely=0, relx=0.18)

# Function to fetch food product data from the database
def get_valueta_dtb(stt_ta):
    conn_ta = sqlite3.connect("QLBHTANU.db")
    c_ta = conn_ta.cursor()
    c_ta.execute(f"SELECT * FROM thucan WHERE stt = {stt_ta}")
    res_ta = c_ta.fetchall()
    vl_ta = res_ta[0][1]
    conn_ta.commit()
    conn_ta.close()
    return str(vl_ta)

# Function to fetch drink product data from the database
def get_valuenu_dtb(stt_nu):
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
    pass

# Global variables
check = False
i = 1

# Function to handle the 'Products' menu
def menu():
    global check
    check = True
    bt_home1 = Button(win, text="Thức Ăn", fg="white", bg="gray", border=0, command=thucan)
    bt_home1.place(relx=0.01, rely=0.22)
    bt_home2 = Button(win, text="Nước Uống", fg="white", bg="gray", border=0, command=nuocuong)
    bt_home2.place(relx=0.01, rely=0.26)
    if check == True:
        Button_add_data.place(relx=0, rely=0.3)
        win.update()
        check = False

# Function to display food products

def thucan():
    clear_b()
    # global list_img
    conn = sqlite3.connect("QLBHTANU.db")
    c = conn.cursor()
    c.execute("SELECT * FROM thucan")
    list_ta = c.fetchall()
    conn.commit()
    conn.close()

    # list_img = ["D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/banhuot.jpg", "D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/bunmannem.jpg"]
    # print(list_img)
    x_img = 0.23
    y_img = 0.1
    x_t = 0.28
    y_t = 0.18
    t = 1
    sl = 0
    for s, t, g,f in list_ta:
        stt = s 
        ten = t
        gia = g
        file = f
        if sl % 3 == 0:
            x_img = 0.23
            x_t = 0.28
            y_img = y_img + 0.2
            y_t = y_t + 0.15
        ta_img = resize_img(file, 200, 100)
        ta_lb_img = Label(win, image=ta_img)
        ta_lb_img.image = ta_img
        ta_lb_img.place(relx=x_img, rely=y_img)
        ta_lb_text = Label(win, text=get_valueta_dtb(stt))
        ta_lb_text.place(relx=x_t, rely=y_t)
        x_img = x_img + 0.25  # Increase y_img to adjust the vertical position of the next item
        x_t = (x_t + 0.30)-0.05 # Increase y_t similarly
        
        sl = sl + 1

# Function to display drink products
def nuocuong():
    clear_b()
    nm_img = resize_img("D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/nuocmia.jpg", 200, 100)
    nm_lb_img = Label(win, image=nm_img)
    nm_lb_img.image = nm_img
    nm_lb_img.place(relx=0.23, rely=0.1)
    nm_lb_text = Label(win, text=get_valuenu_dtb(1))
    nm_lb_text.place(rely=0.26, relx=0.28)

    nd_img = resize_img("D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong/nuocdua.jpg", 200, 100)
    nd_lb_img = Label(win, image=nd_img)
    nd_lb_img.image = nd_img
    nd_lb_img.place(relx=0.46, rely=0.1)
    nd_lb_text = Label(win, text=get_valuenu_dtb(2))
    nd_lb_text.place(rely=0.26, relx=0.51)
    
dt = StringVar()
dt.set(" ")
def add_data():
    clear_b()
    global a_d_stt_e,a_d_t_e,a_d_g_e
    a_d_stt_text = Label(win,text="Stt")
    a_d_stt_text.place(relx=0.2,rely=0.05)
    a_d_stt_e = Entry(win)
    a_d_stt_e.place(relx=0.225,rely=0.05)
    
    a_d_t_text = Label(win,text="Tên")
    a_d_t_text.place(relx=0.2,rely=0.1)
    a_d_t_e = Entry(win)
    a_d_t_e.place(relx=0.225,rely=0.1)
    
    a_d_g_text = Label(win,text="Giá")
    a_d_g_text.place(relx=0.2,rely=0.15)
    a_d_g_e = Entry(win)
    a_d_g_e.place(relx=0.225,rely=0.15)
    
    a_d_i_b = Button(win,text="Chọn ảnh",command=open_img)
    a_d_i_b.place(relx=0.2,rely=0.2)
    

    choose_ta = Radiobutton(win,text="Thức Ăn",variable=dt,value="Thức Ăn",command=on_selection_change)
    choose_ta.place(relx=0.2,rely=0.30)
    choose_nu = Radiobutton(win,text="Nước Uống",variable=dt,value="Nước Uống",command=on_selection_change)
    choose_nu.place(relx=0.2,rely=0.35)
    
    a_d_xn_b = Button(win,text="Xác Nhận",command=xacnhan)
    a_d_xn_b.place(relx=0.2,rely=0.4)
    
def xacnhan():
    global a_d_stt_e,a_d_t_e,a_d_g_e
    # dt.set(" ")
    global dt
    global filename_img
    if dt.get() == "Thức Ăn":
        conn = sqlite3.connect("QLBHTANU.db")
        c = conn.cursor()
        c.execute("INSERT INTO thucan VALUES(:stt,:ten,:gia,:file)",{
                "stt" : int(a_d_stt_e.get()),
                "ten" : a_d_t_e.get(),
                "gia" : int(a_d_g_e.get()),
                "file": filename_img
        })
        conn.commit()
        conn.close()
    dt.set(" ")
        # list_img.append(filename_img)
    
def on_selection_change():
    pass
def open_img():
    global filename_img
    win.filename = filedialog.askopenfilename(initialdir="D:/Learn Python/Project/QLBH Thuc An va Nuoc Uong",title="Select File",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    filename_img = win.filename
    Label(win,text="",width=55,height=1).place(relx=0.2,rely=0.25)
    Label(win,text=filename_img).place(relx=0.2,rely=0.25)
    # list_img.append(filename_img)
# Create a gray background label
labe_nen = Label(win, text="", bg="gray", width=30, height=60)
labe_nen.grid(column=0, rowspan=13)

# Create a logo button
Button_logo = Button(win, text="Logo", fg="white", bg="gray", border=0)
Button_logo.grid(column=0, row=0, rowspan=1, sticky="NW")

# Create a 'Home' button
Button_home = Button(win, text="Trang Chủ", fg="white", bg="gray", border=0, command=home)
Button_home.grid(column=0, row=1, rowspan=1, sticky="NW")

# Create a 'Products' button
Button_menu = Button(win, text="Sản Phẩm", fg="white", bg="gray", border=0, command=menu)
Button_menu.grid(column=0, row=1, rowspan=1, pady=40, sticky="NW")

# Create an 'Add Product' button
Button_add_data = Button(win, text="Thêm Sản Phẩm", fg="white", bg="gray", border=0,command=add_data)
Button_add_data.place(relx=0, rely=0.23)

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