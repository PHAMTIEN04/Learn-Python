from tkinter import *

def mysum():
    x = mylabel_i1.get()  # Lấy giá trị nhập vào từ mylabel_i1
    y = mylabel_i2.get()  # Lấy giá trị nhập vào từ mylabel_i2
    sum = int(x) + int(y)  # Tính tổng của x và y, đưa kết quả vào biến sum
    mycheck = Label(win, text=str(sum))  # Tạo Label để hiển thị kết quả sum
    mycheck.pack()  # Đưa Label vào cửa sổ

win = Tk()

win.geometry("1000x700")  # Thiết lập kích thước của cửa sổ
label1 = Label(win, text="Nhập số ")  # Tạo Label với nội dung là "Nhập số"
label1.pack()  # Đưa Label vào cửa sổ
mylabel_i1 = Entry(win)  # Tạo ô nhập liệu cho số thứ nhất
mylabel_i1.pack()  # Đưa ô nhập liệu vào cửa sổ
mylabel_i2 = Entry(win)  # Tạo ô nhập liệu cho số thứ hai
mylabel_i2.pack()  # Đưa ô nhập liệu vào cửa sổ

mylabel1 = Button(win, text="Enter", command=mysum)  # Tạo Button để tính tổng, đặt tên là "Enter"
mylabel1.pack()  # Đưa Button vào cửa sổ

win.mainloop()  # Bắt đầu vòng lặp chính của chương trình, xử lý các sự kiện được tạo ra bởi người dùng




