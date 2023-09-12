import requests

url = "http://student.husc.edu.vn/"
r_re = requests.get(url,allow_redirects=True)
print(r_re.url)
print(r_re.status_code)
print(r_re.history)

# Đoạn code này sử dụng thư viện requests trong Python để thực hiện HTTP requests đến trang web http://student.husc.edu.vn/.

# Ở dòng số 3: allow_redirects=True cho phép cập nhật địa chỉ URL khi xuất hiện redirection (chuyển hướng).

# Ở dòng số 4, in ra r_re.url để xem địa chỉ URL sau khi đã redirect.

# Ở dòng số 5, in ra r_re.status_code để xem mã trạng thái HTTP trả về.

# Ở dòng số 6, in ra r_re.history để xem lịch sử của các chuyển hướng nếu có.

# Với đoạn code này, ta sẽ gửi một request tới địa chỉ http://student.husc.edu.vn/, do trang này không yêu cầu chuyển hướng, nên r_re.url, r_re.status_code và r_re.history 
# đều sẽ trả về giá trị ban đầu mà không bị thay đổi.