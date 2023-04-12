# # sử dụng thư viện requests trong Python để thực hiện các hoạt động khác nhau trên web.
import requests
import os

os.chdir(r'C:\Learn Python\Tool Python\Bài Tập')

# Gửi một POST Request đến URL "https://httpbin.org/post" kèm với Header có thuộc tính "Content-Type" và giá trị của nó là "multipart/form-data". 
# Sau đó, biến "r_header" chứa Response từ server. Đoạn print được sử dụng để hiển thị Header mà Client(Gửi request) đã gửi lên Server.
# Cụ thể, với câu lệnh "print(r_header.request.headers)" sẽ hiển thị ra tất cả các thông số của Header được gửi từ Client đến Server (gồm có "Content-Type" ở đây).
# "print(r_header.request.headers["Content-Type"])", sẽ hiển thị giá trị của thuộc tính "Content-Type" trong Header của Request đã gửi đi.
header = {"Content-Type" : "multipart/form-data"}
url_header = "https://httpbin.org/post"
r_header = requests.post(url_header, headers=header)
print(r_header.request.headers["Content-Type"])

# "print(r_header.headers["Content-Type"])" sẽ hiển thị giá trị của thuộc tính "Content-Type" trong Header của Response nhận được từ Server (tương tự như Request).
print(r_header.headers["Content-Type"])