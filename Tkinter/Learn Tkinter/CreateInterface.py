# tkinter là một module trong Python được sử dụng để tạo giao diện đồ họa. * đại diện cho tất cả các hàm, lớp và biến trong module tkinter sẽ được import vào chương trình Python.
from tkinter import *

# Tk() được sử dụng để tạo một đối tượng win đại diện cho cửa sổ giao diện
win = Tk()

# phương thức title() được sử dụng để đặt tiêu đề cho cửa sổ là "Giao Diện".
win.title("Giao Diện")

# Tạo một đối tượng nhãn (label) trong giao diện đồ họa với nội dung là chuỗi "Hello World!".
mylabel1 = Label(win, text="Hello World!").grid(row=0,column=0)
mylabel2 = Label(win, text="My Name Is TienDz").grid(row=5,column=0)
mylabel3 = Label(win, text="                  ").grid(row=1,column=0)

#  phương thức grid để sắp xếp các widget trong lưới, ta phải chỉ định vị trí của từng widget dựa trên chỉ số hàng (row) và cột (column). Ở đây, row=0 và column=0 
# là các tham số truyền vào phương thức grid để đặt widget vào hàng và cột tương ứng trong lưới.
#Cach 1: 
# mylabel1.grid(row=0,column=0)
# mylabel2.grid(row=5,column=0)
# mylabel3.grid(row=1,column=0)
#Cach 2:
mylabel1
mylabel2
mylabel3


# đặt nó vào giao diện bằng phương thức pack().
# mylabel.pack()


# Phương thức geometry() được sử dụng để thiết lập kích thước cửa sổ là 700 pixel theo chiều rộng và 500 pixel theo chiều cao.
win.geometry("700x500")

# Phương thức attributes() được sử dụng để thiết lập thuộc tính của cửa sổ. Trong đoạn code này, thuộc tính "-topmost" được thiết lập là True, 
# cho phép cửa sổ hiển thị trên đỉnh của các cửa sổ khác.
win.attributes("-topmost",True)

# win["bg"] = "#CCFFFF" thiết lập màu nền của cửa sổ giao diện là màu xanh nước biển nhạt. Điều này sẽ làm cho cửa sổ có màu nền khác với màu mặc định của hệ thống.
win["bg"] = "#CCFFFF"


# phương thức mainloop() được gọi để giữ cho cửa sổ hiển thị trên màn hình và cho phép người dùng tương tác với các thành phần trong giao diện.
win.mainloop()
