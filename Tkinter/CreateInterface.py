# tkinter là một module trong Python được sử dụng để tạo giao diện đồ họa. * đại diện cho tất cả các hàm, lớp và biến trong module tkinter sẽ được import vào chương trình Python.
from tkinter import *

# Tk() được sử dụng để tạo một đối tượng win đại diện cho cửa sổ giao diện
win = Tk()

# phương thức title() được sử dụng để đặt tiêu đề cho cửa sổ là "Giao Diện".
win.title("Giao Diện")

# Phương thức geometry() được sử dụng để thiết lập kích thước cửa sổ là 700 pixel theo chiều rộng và 500 pixel theo chiều cao.
win.geometry("700x500")

# Phương thức attributes() được sử dụng để thiết lập thuộc tính của cửa sổ. Trong đoạn code này, thuộc tính "-topmost" được thiết lập là True, 
# cho phép cửa sổ hiển thị trên đỉnh của các cửa sổ khác.
win.attributes("-topmost",True)

# win["bg"] = "#CCFFFF" thiết lập màu nền của cửa sổ giao diện là màu xanh nước biển nhạt. Điều này sẽ làm cho cửa sổ có màu nền khác với màu mặc định của hệ thống.
win["bg"] = "#CCFFFF"


# phương thức mainloop() được gọi để giữ cho cửa sổ hiển thị trên màn hình và cho phép người dùng tương tác với các thành phần trong giao diện.
win.mainloop()
