# # sử dụng thư viện requests trong Python để thực hiện các hoạt động khác nhau trên web.
import requests
import os

os.chdir(r'C:\Learn Python\Tool Python\Bài Tập')

# Sử dụng phương thức GET để gửi yêu cầu tới URL https://httpbin.org/get. 
# Nó chứa một payload được chuyển dưới dạng params, sau đó hiển thị Status Code và r_get.text.
url_get = "https://httpbin.org/get"
payload_get = {"first name" : "Nick" ,"birtday" : "17-11-2004"}
r_get = requests.get(url=url_get , params=payload_get)
print("Status Code",r_get.status_code)
print(r_get.text)