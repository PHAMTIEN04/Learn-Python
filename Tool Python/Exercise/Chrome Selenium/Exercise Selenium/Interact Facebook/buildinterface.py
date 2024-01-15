from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import sleep
def resize_img(path,width,height): # Function Resize Image
    img = Image.open(path)
    img = img.resize((width,height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)
win = Tk()
win.geometry("700x500")
win.resizable(False,False)
win.title("Interact Facebook")
win.iconbitmap("iconfb.ico")
treeview = ttk.Treeview(win)

treeview.configure(height=20)
treeview['columns'] = ("ID","Type","Status")

treeview.column("#0",width=50,anchor=W)
treeview.column("ID",anchor=CENTER,width=150)
treeview.column("Type",anchor=CENTER,width=70)
treeview.column("Status",anchor=CENTER,width=70)

treeview.heading("#0",text="STT",anchor=CENTER)
treeview.heading("ID",text="ID",anchor=CENTER)
treeview.heading("Type",text="Type",anchor=CENTER)
treeview.heading("Status",text="Status",anchor=CENTER)
def test():
    for i in range(100):
        treeview.insert(parent="", index="end", iid=i, text=i, values=(112312,"Like","Success"))
        


# treeview.su
treeview.place(relx=0.085,rely=0.08)

link_text = Label(win,text="Get Link",font=("Arial",10,"bold"))
link_text.place(relx=0,rely=0.02)

Link_entry = Entry(win,width=55)
Link_entry.place(relx=0.09,rely=0.025)

like_button = Button(win,text="Like",width=30,height=5,border=5,command=test)
like_button.place(relx=0.65,rely=0.35)

cmt_button = Button(win,text="Comment",width=30,height=5,border=5)
cmt_button.place(relx=0.65,rely=0.55)

all_button = Button(win,text="All",width=30,height=5,border=5)
all_button.place(relx=0.65,rely=0.75)
rz_img = resize_img("./add.png",215,160)
lb_img = Label(win,image=rz_img)
lb_img.place(relx =0.65,rely=0.01)
win.mainloop()