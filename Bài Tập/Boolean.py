# Boolean là một kiểu dữ liệu trong Python chỉ có giá trị True hoặc False. 
# Boolean thường được sử dụng để kiểm tra điều kiện đúng hoặc sai trong các câu lệnh điều khiển như if, while, for,...

# Có một số toán tử và phương thức chỉ định kiểu Boolean trong Python:

# Toán tử so sánh: (==, !=, >, >=, <, <=) trả về giá trị Boolean
x = 5
y = 10
print(x == y) #False
print(x != y) #True
print(x > y) #False
print(x < y) #True

# Toán tử logic: (and, or, not) trả về giá trị Boolean

a = True 
b = False
print(a and b) #False
print(a or b) #True
print(not a) #False

# Phương thức kiểm tra kiểu dữ liệu:
# isinstance() trả về giá trị True nếu biến được kiểm tra thuộc loại dữ liệu Boolean.
x = True 
print(isinstance(x, bool)) #True 

# Ngoài ra, một số giá trị khác như 0, None, chuỗi rỗng, danh sách/trống,... cũng có thể được chuyển đổi thành Boolean bằng hàm bool():

print(bool(0)) #False
print(bool(None)) #False
print(bool("")) #False
print(bool([])) #False

# Trong tổng quát, Boolean rất cần thiết trong việc kiểm soát luồng chương trình và xử lý dữ liệu từ điều kiện.

# Đọc thêm chi tiết tại https://howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-boolean-trong-python-2593