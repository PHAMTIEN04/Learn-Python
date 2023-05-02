# tkinter là một module trong Python được sử dụng để tạo giao diện đồ họa. * đại diện cho tất cả các hàm, lớp và biến trong module tkinter sẽ được import vào chương trình Python.
from tkinter import *

# Tk() được sử dụng để tạo một đối tượng win đại diện cho cửa sổ giao diện
win = Tk()

# phương thức title() được sử dụng để đặt tiêu đề cho cửa sổ là "Giao Diện".
win.title("Creating Buttons")

# Phương thức geometry() được sử dụng để thiết lập kích thước cửa sổ là 1000 pixel theo chiều rộng và 700 pixel theo chiều cao.
win.geometry("1000x700")

# win["bg"] = "#CCFFFF" thiết lập màu nền của cửa sổ giao diện là màu xanh nước biển nhạt. Điều này sẽ làm cho cửa sổ có màu nền khác với màu mặc định của hệ thống.
win['bg'] = "#CCFFFF"

# Đoạn mã trên tạo một nút bấm trong một cửa sổ đồ họa với các thuộc tính sau:

# win là đối tượng cửa sổ mà nút bấm sẽ được đặt vào.
# "No!!! Click Me" là văn bản hiển thị trên nút bấm.
# padx và pady là lề đệm ngang và dọc của văn bản trên nút bấm.
# command=myClick là hàm sẽ được thực thi khi người dùng click vào nút.
# fg="red" là màu sắc chữ của văn bản trên nút là màu đỏ.
# bg='#00FF00' là màu nền của nút là màu xanh lá cây.
# Vì vậy, khi chạy đoạn mã trên, một nút bấm có văn bản "No!!! Click Me" với lề đệm lớn và màu sắc đỏ sẽ được hiển thị trong cửa sổ đồ họa và khi được click vào thì hàm myClick sẽ được gọi. Màu nền của nút là màu xanh lá cây.

def myClick():
    # x = int(input())
    # y = int(input())
    # test = x + y
    mylabel = Label(win,text = "FUCK!!!!!!",fg='#00FF00',bg='#CC0000')
    mylabel = Label(win,text = "rin bede",fg='#00FF00',bg='#CC0000',width=20,height=20)
    mylabel.pack()

mybutton = Button(win,text="No!!! Click Me",padx=100,pady=100,command=myClick,fg="red",bg='#00FF00')

# đặt nó vào giao diện bằng phương thức pack().
mybutton.pack()

# phương thức mainloop() được gọi để giữ cho cửa sổ hiển thị trên màn hình và cho phép người dùng tương tác với các thành phần trong giao diện.
win.mainloop()