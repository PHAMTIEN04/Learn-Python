# # sử dụng thư viện requests trong Python để thực hiện các hoạt động khác nhau trên web.
import requests
import os

os.chdir(r'C:\Learn Python\Tool Python\Bài Tập')


# Sử dụng phương thức GET để gửi yêu cầu tới url https://api.github.com/events. 
# Người dùng sẽ nhận được dữ liệu trong định dạng JSON và trích xuất từ URL repo đầu tiên trong sự kiện này.
url_json = "https://api.github.com/events"
r_json = requests.get(url=url_json)
json_check = r_json.json()
print(json_check[0]['repo']['url'])

# Sử dụng phương thức POST để gửi yêu cầu tới url https://httpbin.org/post. 
# Dữ liệu được gửi trong định dạng JSON và in ra r_json1.text."""
url_json1 = "https://httpbin.org/post"
data = {"fist name" : "Nick","Sex" : "Male"}
r_json1 = requests.post(url=url_json1, json=data)
print(r_json1.text)