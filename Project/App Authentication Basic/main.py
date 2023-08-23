from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import subprocess


# Tạo cửa sổ đăng nhập
root = Tk()
root.title("Đăng nhập")
root.geometry("350x200+580+300")
root.resizable(False,False)
root.iconbitmap("D:/Learn Python/Project/App Authentication Basic/favicon.ico")
def resizeimg(path,width,height):
    img = Image.open(path)
    img = img.resize((width,height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "171104":
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        root.destroy()  # Đóng cửa sổ đăng nhập
        subprocess.call("C:/Program Files/Google/Chrome/Application/chrome.exe")
    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)    
        messagebox.showerror("Error", "Login failed!!!")

# Tạo các widgets đăng nhập
username_label = Label(root, text="User Name",font=("bold",10),fg="black")
username_entry = Entry(root,width=25,border=2)
password_label = Label(root, text="Password",font=("bold",10),fg="black")
password_entry = Entry(root,width=25, show="*",border=2)
login_button = Button(root, text="Login", command=login,bg="light blue",fg="black",width=8,height=2)

# Định vị các widgets đăng nhập
username_label.grid(column=1,row=1,sticky="W")
username_entry.grid(column=1,row=2)
password_label.grid(column=1,row=3,sticky="W")
password_entry.grid(column=1,row=4)
login_button.grid(column=1,row=5,sticky="W",pady=10)

day_y = Label(root,text="")
day_y.grid(row=0,pady=5)

day_x = Label(root,text="")
day_x.grid(column=0,padx=20)

img = resizeimg("D:/Learn Python/Project/App Authentication Basic/khoa.png",100,100)
img_k = Label(root,image=img)
img_k.place(relx=0.6,rely=0.10)
root.mainloop()
