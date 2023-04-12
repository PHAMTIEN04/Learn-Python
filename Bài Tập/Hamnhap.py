x = 1
name = int(input(x+1))
print("Hello!",name,sep=".")
print(type(name))

# Giới thiệu về hàm input trong Python

# Trong ngôn ngữ lập trình Python, bạn có thể yêu cầu người dùng nhập vào một giá trị bất kỳ bằng cách sử dụng
# hàm input(). Điều này cho phép người dùng hoạt động với chương trình khi nó đang chạy.

# Cú pháp: input([prompt])
# Phương thức input đọc một dòng từ người dùng, sau đó là chuyển đổi thành chuỗi và trả về nó. 
# Nếu giá trị prompt được cung cấp, nó sẽ được xuất ra cho người dùng.

# Ví dụ 1:

# Đoạn code sau sẽ yêu cầu người dùng nhập vào tên của họ và sau đó in tên đó ra trên cửa sổ console.


name = input("Nhập tên của bạn: ")
print("Tên của bạn là", name)

# Kết quả:

# Nhập tên của bạn: John
# Tên của bạn là John

# Ví dụ 2:

# Bạn cũng có thể yêu cầu người dùng nhập số nguyên.


age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là:", age)

# Kết quả:

# Nhập tuổi của bạn: 25
# Tuổi của bạn là: 25

# Lưu ý rằng hàm input() luôn trả về một chuỗi. 
# Vì vậy, nếu bạn muốn thực hiện bất kỳ phép toán toán học nào với giá trị nhập vào, 
# bạn cần phải chuyển đổi nó thành một số nguyên hoặc số thực bằng cách sử dụng các hàm int() hoặc float().

# Kết luận:

# Trong bài hướng dẫn này, chúng ta đã tìm hiểu cách yêu cầu người dùng nhập vào một giá trị bất kỳ trong 
# Python bằng cách sử dụng hàm input(). Chúng ta cũng đã thấy cách chuyển đổi chuỗi đầu vào thành số nguyên 
# hoặc số thực.

# Đọc Thêm Chi Tiết Tại: https://howkteam.vn/course/lap-trinh-python-co-ban/nhap-xuat-trong-python-ham-nhap-1574